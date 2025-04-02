from prisoners import *

# Funkce pro výpočet skóre na základě tahů obou hráčů
def rozdej_skore(tah1, tah2):
    # 1 = zradi, 0 = nezradi
    skores = (0, 0)

    if (tah1 == 1) and (tah2 == 1):
        skores = (2, 2)

    if (tah1 == 1) and (tah2 == 0):
        skores = (0, 3)

    if (tah1 == 0) and (tah2 == 1):
        skores = (3, 0)

    if (tah1 == 0) and (tah2 == 0):
        skores = (1, 1)

    return skores

# Funkce pro simulaci hry mezi dvěma strategiemi
def play(f1, f2, MAX_ROUNDS):

    skore1 = 0
    skore2 = 0

    historie1 = []
    historie2 = []

    for i in range(MAX_ROUNDS):
        tah1 = f1(historie1, historie2)
        tah2 = f2(historie2, historie1)

        s1, s2 = rozdej_skore(tah1, tah2)
        skore1 += s1
        skore2 += s2

        historie1.append(tah1)
        historie2.append(tah2)

    return skore1, skore2, historie1, historie2

def tournament():
	ucastnici = [fk_solution, tit_for_tat]
	l = len(ucastnici)
	skores = [0 for _ in range(l)]

	print("=========================================")
	print("Turnaj")
	print("hra délky:", MAX_ROUNDS)
	print("-----------------------------------------")


	for i in range(l):
		for j in range(i+1, l):
			f1 = ucastnici[i]
			f2 = ucastnici[j]
			skore1, skore2, historie1, historie2 = play(f1, f2, MAX_ROUNDS)
			print(f1.__name__, "x", f2.__name__, " ", skore1, ":", skore2)
			print(f"historie: {historie1} \n\n {historie2}")
			skores[i] += skore1
			skores[j] += skore2


	print("=========================================")
	print("= Výsledné pořadí")
	print("-----------------------------------------")


	# setrideni indexu vysledku
	index = sorted(range(l), key=lambda k: skores[k])

	poradi = 1
	for i in index:
		f = ucastnici[i]
		print(poradi, ".", f.__name__, ":", skores[i])
		poradi += 1