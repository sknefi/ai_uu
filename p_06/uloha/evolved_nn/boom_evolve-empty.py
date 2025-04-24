# -*- coding: utf-8 -*-


import pygame
import numpy as np
import random
import math
from deap import base, creator, tools
from constants import *
from classes import *

pygame.font.init()


#-----------------------------------------------------------------------------
# Parametry hry 
#-----------------------------------------------------------------------------


WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption(TITLE)

# Fonty
BOOM_FONT = pygame.font.SysFont("comicsans", 100)   
LEVEL_FONT = pygame.font.SysFont("comicsans", 20)   

# Obrázky
ENEMY_IMAGE  = pygame.image.load("../imgs/mine.png")
ME_IMAGE = pygame.image.load("../imgs/me.png")
SEA_IMAGE = pygame.image.load("../imgs/sea.png")
FLAG_IMAGE = pygame.image.load("../imgs/flag.png")

# Překreslení obrázků
ENEMY = pygame.transform.scale(ENEMY_IMAGE, (ENEMY_SIZE, ENEMY_SIZE))
ME = pygame.transform.scale(ME_IMAGE, (ME_SIZE, ME_SIZE))
SEA = pygame.transform.scale(SEA_IMAGE, (WIDTH, HEIGHT))
FLAG = pygame.transform.scale(FLAG_IMAGE, (ME_SIZE, ME_SIZE))






# -----------------------------------------------------------------------------    
# nastavení herního plánu    
#-----------------------------------------------------------------------------
    

# rozestavi miny v danem poctu num
def set_mines(num):
    l = []
    for i in range(num):
        m = Mine()
        l.append(m)
        
    return l
    

# inicializuje me v poctu num na start 
def set_mes(num):
    l = []
    for i in range(num):
        m = Me()
        l.append(m)
        
    return l

# zresetuje vsechny mes zpatky na start
def reset_mes(mes, pop):
    for i in range(len(pop)):
        me = mes[i]
        me.rect.x = 10
        me.rect.y = 10
        me.alive = True
        me.dist = 0
        me.won = False
        me.timealive = 0
        me.sequence = pop[i]
        me.fitness = 0
    

# -----------------------------------------------------------------------------    
# senzorické funkce 
# -----------------------------------------------------------------------------    

# Senzor pro detekci blízkých min
def detect_mines(me, mines, max_distance=200):
    sensors = [0, 0, 0, 0, 0, 0, 0, 0]  # 8 směrů (N, NE, E, SE, S, SW, W, NW)
    
    me_center_x = me.rect.x + me.rect.width/2
    me_center_y = me.rect.y + me.rect.height/2
    
    for mine in mines:
        mine_center_x = mine.rect.x + mine.rect.width/2
        mine_center_y = mine.rect.y + mine.rect.height/2
        
        dx = mine_center_x - me_center_x
        dy = mine_center_y - me_center_y
        distance = math.sqrt(dx*dx + dy*dy)
        
        if distance > max_distance:
            continue
            
        # Normalizovaný signál - čím blíže, tím silnější (1 = velmi blízko, 0 = daleko)
        signal = 1 - (distance / max_distance)
        
        # Určení směru
        angle = math.atan2(dy, dx)
        degrees = math.degrees(angle)
        if degrees < 0:
            degrees += 360
            
        # Určit, který senzor by měl reagovat
        sensor_idx = int((degrees + 22.5) / 45) % 8
        
        # Aktualizovat senzor pouze pokud je nová hodnota vyšší
        if signal > sensors[sensor_idx]:
            sensors[sensor_idx] = signal
    
    return sensors

# Senzor pro detekci vzdálenosti od cíle
def detect_flag(me, flag):
    me_center_x = me.rect.x + me.rect.width/2
    me_center_y = me.rect.y + me.rect.height/2
    
    flag_center_x = flag.rect.x + flag.rect.width/2
    flag_center_y = flag.rect.y + flag.rect.height/2
    
    dx = flag_center_x - me_center_x
    dy = flag_center_y - me_center_y
    
    # Vzdálenost k cíli
    distance = math.sqrt(dx*dx + dy*dy)
    max_possible_distance = math.sqrt(WIDTH*WIDTH + HEIGHT*HEIGHT)
    
    # Normalizovaná vzdálenost (0 = daleko, 1 = blízko)
    normalized_distance = 1 - (distance / max_possible_distance)
    
    # Směr k cíli (normalizovaný vektor)
    if distance > 0:
        dx_norm = dx / distance
        dy_norm = dy / distance
    else:
        dx_norm = 0
        dy_norm = 0
    
    return [normalized_distance, dx_norm, dy_norm]

# Senzor pro detekci blízkosti stěn
def detect_walls(me):
    # Normalizované vzdálenosti od stěn (0 = u stěny, 1 = daleko)
    left_wall = me.rect.x / WIDTH
    right_wall = (WIDTH - (me.rect.x + me.rect.width)) / WIDTH
    top_wall = me.rect.y / HEIGHT
    bottom_wall = (HEIGHT - (me.rect.y + me.rect.height)) / HEIGHT
    
    return [left_wall, right_wall, top_wall, bottom_wall]

# Hlavní senzorická funkce, která kombinuje všechny senzory
def my_senzor(me, mines, flag):
    mine_sensors = detect_mines(me, mines)
    flag_sensors = detect_flag(me, flag)
    wall_sensors = detect_walls(me)
    
    # Spojení všech senzorů do jednoho vstupního vektoru
    sensors = mine_sensors + flag_sensors + wall_sensors
    
    return sensors


# ---------------------------------------------------------------------------
# funkce řešící pohyb agentů
# ----------------------------------------------------------------------------


# konstoluje kolizi 1 agenta s minama, pokud je kolize vraci True
def me_collision(me, mines):    
    for mine in mines:
        if me.rect.colliderect(mine.rect):
            #pygame.event.post(pygame.event.Event(ME_HIT))
            return True
    return False
            
            
# kolidujici agenti jsou zabiti, a jiz se nebudou vykreslovat
def mes_collision(mes, mines):
    for me in mes: 
        if me.alive and not me.won:
            if me_collision(me, mines):
                me.alive = False
            
            
# vraci True, pokud jsou vsichni mrtvi Dave            
def all_dead(mes):    
    for me in mes: 
        if me.alive:
            return False
    
    return True


# vrací True, pokud již nikdo nehraje - mes jsou mrtví nebo v cíli
def nobodys_playing(mes):
    for me in mes: 
        if me.alive and not me.won:
            return False
    
    return True


# rika, zda agent dosel do cile
def me_won(me, flag):
    if me.rect.colliderect(flag.rect):
        return True
    
    return False


# vrací počet živých mes
def alive_mes_num(mes):
    c = 0
    for me in mes:
        if me.alive:
            c += 1
    return c



# vrací počet mes co vyhráli
def won_mes_num(mes):
    c = 0
    for me in mes: 
        if me.won:
            c += 1
    return c

         
    
# resi pohyb miny        
def handle_mine_movement(mine):
        
    if mine.dirx == -1 and mine.rect.x - mine.velocity < 0:
        mine.dirx = 1
       
    if mine.dirx == 1  and mine.rect.x + mine.rect.width + mine.velocity > WIDTH:
        mine.dirx = -1

    if mine.diry == -1 and mine.rect.y - mine.velocity < 0:
        mine.diry = 1
    
    if mine.diry == 1  and mine.rect.y + mine.rect.height + mine.velocity > HEIGHT:
        mine.diry = -1
         
    mine.rect.x += mine.dirx * mine.velocity
    mine.rect.y += mine.diry * mine.velocity


# resi pohyb min
def handle_mines_movement(mines):
    for mine in mines:
        handle_mine_movement(mine)


#----------------------------------------------------------------------------
# vykreslovací funkce 
#----------------------------------------------------------------------------


# vykresleni okna
def draw_window(mes, mines, flag, level, generation, timer):
    WIN.blit(SEA, (0, 0))   
    
    t = LEVEL_FONT.render("level: " + str(level), 1, WHITE)   
    WIN.blit(t, (10  , HEIGHT - 30))
    
    t = LEVEL_FONT.render("generation: " + str(generation), 1, WHITE)   
    WIN.blit(t, (150  , HEIGHT - 30))
    
    t = LEVEL_FONT.render("alive: " + str(alive_mes_num(mes)), 1, WHITE)   
    WIN.blit(t, (350  , HEIGHT - 30))
    
    t = LEVEL_FONT.render("won: " + str(won_mes_num(mes)), 1, WHITE)   
    WIN.blit(t, (500  , HEIGHT - 30))
    
    t = LEVEL_FONT.render("timer: " + str(timer), 1, WHITE)   
    WIN.blit(t, (650  , HEIGHT - 30))
    
    WIN.blit(FLAG, (flag.rect.x, flag.rect.y))    
         
    # vykresleni min
    for mine in mines:
        WIN.blit(ENEMY, (mine.rect.x, mine.rect.y))
        
    # vykresleni me
    for me in mes: 
        if me.alive:
            WIN.blit(ME, (me.rect.x, me.rect.y))
        
    pygame.display.update()



def draw_text(text):
    t = BOOM_FONT.render(text, 1, WHITE)   
    WIN.blit(t, (WIDTH // 2  , HEIGHT // 2))     
    
    pygame.display.update()
    pygame.time.delay(1000)







#-----------------------------------------------------------------------------
# funkce reprezentující neuronovou síť, pro inp vstup a zadané váhy wei, vydá
# čtveřici výstupů pro nahoru, dolu, doleva, doprava    
#----------------------------------------------------------------------------

def nn_function(inp, wei):
    """
    Jednoduchá feed-forward sieť:
      - 15 vstupov
      - 8 skrytých neurónov (ReLU)
      - 4 výstupy (softmax + argmax)
    """

    # 1) definujeme veľkosti vrstiev
    n_in = len(inp)        # n_in = 15, počet senzorov v inpute
    n_hidden = 8           # pevne 8 neurónov v skrytej vrstve
    n_out = 4              # 4 možné akcie: ↑, ↓, ←, →

    # 2) rozdelíme vektor váh wei na 4 bloky:
    #    a) váhy vstup→skrytá
    end1 = n_in * n_hidden
    # end1 = 15 * 8 = 120

    W1_flat = wei[0:end1]
    # W1_flat je zoznam dĺžky 120

    W1 = np.array(W1_flat).reshape(n_in, n_hidden)
    # W1 má tvar (15, 8), každá z 15 vstupných dimenzií má 8 váh

    #    b) biasy skrytej vrstvy
    start2 = end1
    end2   = start2 + n_hidden
    # end2 = 120 + 8 = 128

    b1 = np.array(wei[start2:end2])
    # b1 je 1D pole dĺžky 8

    #    c) váhy skrytá→výstup
    start3  = end2
    end3    = start3 + n_hidden * n_out
    # end3 = 128 + 8*4 = 160

    W2_flat = wei[start3:end3]
    # W2_flat je zoznam dĺžky 32

    W2 = np.array(W2_flat).reshape(n_hidden, n_out)
    # W2 má tvar (8, 4)

    #    d) biasy výstupnej vrstvy
    b2 = np.array(wei[end3:end3 + n_out])
    # b2 je pole dĺžky 4

    # 3) forward pass – skrytá vrstva
    inp_arr = np.array(inp)	# premena vstupu na numpy array
    # inp_arr má tvar (15,)

    hidden_linear = np.dot(inp_arr, W1) + b1
    # hidden_linear má tvar (8,)
    # každý z 8 neurónov dostane vážený súčet + bias

    hidden_activated = np.maximum(0, hidden_linear)
    # ReLU: všetky záporné hodnoty sa nastavia na 0
    # hidden_activated má tvar (8,)

    # 4) forward pass – výstupná vrstva
    output_linear = np.dot(hidden_activated, W2) + b2
    # output_linear má tvar (4,)
    # tieto 4 čísla sú „skryté skóre“ pre každú z akcií

    # 5) softmax – zmena na pravdepodobnosti
    shifted = output_linear - np.max(output_linear)
    # shifted má tvar (4,), posunuté o maximum, pretože exp(shifted) je stabilnejšie

    exp_vals = np.exp(shifted)
    # exp_vals má tvar (4,), každá zložka je exp(shifted[i])

    sum_exp = np.sum(exp_vals)
    # sum_exp je jediné číslo = ∑ exp_vals[i]

    probs = exp_vals / sum_exp
    # probs má tvar (4,), ∑ probs = 1

    # 6) vybereme index najväčšej pravdepodobnosti
    action = int(np.argmax(probs))
    # action je jedno z 0,1,2,3

    return action

# naviguje jedince pomocí neuronové sítě a jeho vlastní sekvence v něm schované
def nn_navigate_me(me, inp):
    # Získat kompletní senzorické vstupy
    
    # Vyhodnocení sítě s váhami z me.sequence
    ind = nn_function(inp, me.sequence)
    
    # Akce na základě výstupu neuronové sítě
    # nahoru, pokud není zeď
    if ind == 0 and me.rect.y - ME_VELOCITY > 0:
        me.rect.y -= ME_VELOCITY
        me.dist += ME_VELOCITY
    
    # dolu, pokud není zeď
    if ind == 1 and me.rect.y + me.rect.height + ME_VELOCITY < HEIGHT:
        me.rect.y += ME_VELOCITY  
        me.dist += ME_VELOCITY
    
    # doleva, pokud není zeď
    if ind == 2 and me.rect.x - ME_VELOCITY > 0:
        me.rect.x -= ME_VELOCITY
        me.dist += ME_VELOCITY
        
    # doprava, pokud není zeď    
    if ind == 3 and me.rect.x + me.rect.width + ME_VELOCITY < WIDTH:
        me.rect.x += ME_VELOCITY
        me.dist += ME_VELOCITY
    
    
        

# updatuje, zda me vyhrali 
def check_mes_won(mes, flag):
    for me in mes: 
        if me.alive and not me.won:
            if me_won(me, flag):
                me.won = True
    


# resi pohyb mes
def handle_mes_movement(mes, mines, flag):
	for me in mes:
		if me.alive and not me.won:
			sensors_input = my_senzor(me, mines, flag)
			nn_navigate_me(me, sensors_input)



# updatuje timery jedinců
def update_mes_timers(mes, timer):
    for me in mes:
        if me.alive and not me.won:
            me.timealive = timer



# ---------------------------------------------------------------------------
# fitness funkce výpočty jednotlivců
#----------------------------------------------------------------------------



# funkce pro výpočet fitness všech jedinců
def handle_mes_fitnesses(mes, flag):   
    for me in mes:
        
        if me.won:
            # Pokud agent dosáhl cíle, dostane bonus k fitness
            # Bonus je inverzně proporcionální k vzdálenosti, kterou musel urazit
            # Čím méně kroků potřeboval, tím vyšší bonus
            efficiency_bonus = 10000 / (me.dist + 1)  # +1 aby se vyhnulo dělení nulou
            me.fitness = me.timealive + 5000 + efficiency_bonus
        else:
            # Pokud agent nedosáhl cíle, fitness závisí na tom, jak blízko se k němu dostal
            me_center_x = me.rect.x + me.rect.width/2
            me_center_y = me.rect.y + me.rect.height/2
            
            flag_center_x = flag.rect.x + flag.rect.width/2
            flag_center_y = flag.rect.y + flag.rect.height/2
            
            dx = flag_center_x - me_center_x
            dy = flag_center_y - me_center_y
            
            distance_to_flag = math.sqrt(dx*dx + dy*dy)
            max_distance = math.sqrt(WIDTH*WIDTH + HEIGHT*HEIGHT)
            
            # Normalizujeme vzdálenost a odečteme od 1, takže čím blíže k cíli, tím vyšší hodnota
            proximity_factor = 1 - (distance_to_flag / max_distance)
            
            # Přidáme bonus za přiblížení se k cíli
            proximity_bonus = proximity_factor * 1000
            
            me.fitness = me.timealive + proximity_bonus
    
    

# uloží do hof jedince s nejlepší fitness
def update_hof(hof, mes):
    l = [me.fitness for me in mes]
    ind = np.argmax(l)
    hof.sequence = mes[ind].sequence.copy()
    

# ----------------------------------------------------------------------------
# main loop 
# ----------------------------------------------------------------------------

def main():
    
    
    # =====================================================================
    # <----- ZDE Parametry nastavení evoluce !!!!!
    
    VELIKOST_POPULACE = 50
    EVO_STEPS = 5  # pocet kroku evoluce
    DELKA_JEDINCE = 164   # upraveno podle naší architektury neuronové sítě
    NGEN = 30        # počet generací
    CXPB = 0.6          # pravděpodobnost crossoveru na páru
    MUTPB = 0.2        # pravděpodobnost mutace
    
    SIMSTEPS = 1000
    
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)
    
    toolbox = base.Toolbox()

    toolbox.register("attr_rand", random.uniform, -1.0, 1.0)  # Random weights between -1 and 1
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_rand, DELKA_JEDINCE)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    # vlastni random mutace
    def mutRandom(individual, indpb):
        for i in range(len(individual)):
            if random.random() < indpb:
                individual[i] = random.uniform(-1.0, 1.0)
        return individual,

    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", mutRandom, indpb=0.05)
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("selectbest", tools.selBest)
    
    pop = toolbox.population(n=VELIKOST_POPULACE)
        
    # =====================================================================
    
    clock = pygame.time.Clock()

    
    
    # =====================================================================
    # testování hraním a z toho odvození fitness 
   
    
    mines = []
    mes = set_mes(VELIKOST_POPULACE)    
    flag = Flag()
    
    hof = Hof()
    
    
    run = True

    level = 3   # <--- ZDE nastavení obtížnosti počtu min !!!!!
    generation = 0
    
    evolving = True
    evolving2 = False
    timer = 0
    
    while run:  
        
        clock.tick(FPS)
        
               
        # pokud evolvujeme pripravime na dalsi sadu testovani - zrestartujeme scenu
        if evolving:           
            timer = 0
            generation += 1
            reset_mes(mes, pop) # přiřadí sekvence z populace jedincům a dá je na start !!!!
            mines = set_mines(level) 
            evolving = False
            
        timer += 1    
            
        check_mes_won(mes, flag)
        handle_mes_movement(mes, mines, flag)
        
        
        handle_mines_movement(mines)
        
        mes_collision(mes, mines)
        
        if all_dead(mes):
            evolving = True
            #draw_text("Boom !!!")"""

            
        update_mes_timers(mes, timer)        
        draw_window(mes, mines, flag, level, generation, timer)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    

        
        
        
        
        # ---------------------------------------------------------------------
        # <---- ZDE druhá část evoluce po simulaci  !!!!!
        
        # druhá část evoluce po simulaci, když všichni dohrají, simulace končí 1000 krocích

        if timer >= SIMSTEPS or nobodys_playing(mes): 
            
            # přepočítání fitness funkcí, dle dat uložených v jedinci
            handle_mes_fitnesses(mes, flag)   # <--------- ZDE funkce výpočtu fitness !!!!
            
            update_hof(hof, mes)
            
            
            #plot fitnes funkcí
            #ff = [me.fitness for me in mes]
            
            #print(ff)
            
            # přiřazení fitnessů z jedinců do populace
            # každý me si drží svou fitness, a každý me odpovídá jednomu jedinci v populaci
            for i in range(len(pop)):
                ind = pop[i]
                me = mes[i]
                ind.fitness.values = (me.fitness, )
            
            
            # selekce a genetické operace
            offspring = toolbox.select(pop, len(pop))
            offspring = list(map(toolbox.clone, offspring))            

            for child1, child2 in zip(offspring[::2], offspring[1::2]):
                if random.random() < CXPB:
                    toolbox.mate(child1, child2)

            for mutant in offspring:
                if random.random() < MUTPB:
                    toolbox.mutate(mutant)  
            
            pop[:] = offspring
            
            
            evolving = True
                   
        
    # po vyskočení z cyklu aplikace vytiskne DNA sekvecni jedince s nejlepší fitness
    # a ukončí se
    
    pygame.quit()    


if __name__ == "__main__":
    main()