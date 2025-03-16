
RED = "\033[1;31m"
GREEN = "\033[1;32m"
ORANGE = "\033[1;33m"
YELLOW = "\033[1;34m"
RESET = "\033[0m"

PATH0 = 'graphs/small_graph0.col' # licha kruznica
NUM_COLORS0 = 3

PATH1 = 'graphs/small_graph1.col'
NUM_COLORS1 = 3

PATH2 = 'graphs/dsjc250.5.col'
NUM_COLORS2 = 38

PATH3 = 'graphs/dsjc500.1.col'
NUM_COLORS3 = 12

PATH4 = 'graphs/dsjc500.5.col'
NUM_COLORS4 = 48

PATH5 = 'graphs/star_graph.col' # hviezda
NUM_COLORS5 = 2

PATH6 = 'graphs/comple_graph.col'
NUM_COLORS6 = 2

P = 4

if P == 0:
    PATH = PATH0
    NUM_COLORS = NUM_COLORS0
elif P == 1:
    PATH = PATH1
    NUM_COLORS = NUM_COLORS1
elif P == 2:
    PATH = PATH2
    NUM_COLORS = NUM_COLORS2
elif P == 3:
    PATH = PATH3
    NUM_COLORS = NUM_COLORS3
elif P == 4:
    PATH = PATH4
    NUM_COLORS = NUM_COLORS4
elif P == 5:
    PATH = PATH5
    NUM_COLORS = NUM_COLORS5
elif P == 6:
    PATH = PATH6
    NUM_COLORS = NUM_COLORS6
    

MAX_ITER = 1000
RANDOM_WALK_PROB = 0.9
