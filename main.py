# Boardgame Tester
# by Chris Wilson

# This script provides statistics for a mathematical 
# representation of a Snakes and Ladders style game.

#-------------------

# Customisation patameters

start = 0
finish = 100

runs = 100000

ladders = {
    1 : 38,
    4 : 14,
    8 : 30,
    21 : 42,
    28 : 76,
    50 : 67,
    71 : 92,
    88 : 99,
    32 : 10,
    36 : 6,
    48 : 26,
    62 : 18,
    88 : 24,
    95 : 56,
    97 : 78
}

#-------------------

from random import randint
from matplotlib import pyplot as plt
from statistics import mean
from statistics import median
from statistics import mode
from statistics import stdev
from datetime import datetime

start_time = datetime.now()

position = 0

moves = 0

moves_taken = []

for run in range(runs):
    while position < finish:
        roll = randint(1, 6)
        moves += 1
        new_position = position + roll
        if new_position in ladders:
            adjusted_position = ladders[new_position]
            position = adjusted_position
        else:
            new_position = min(new_position, finish)
            position = new_position
	
    moves_taken.append(moves)
    position = 0
    moves = 0

# Print statistics
print(f"Games: {runs}\n\nStats for number of moves\n\nMean: {round(mean(moves_taken), 2)}\nSD: {round(stdev(moves_taken), 2)}\nMedian: {round(median(moves_taken), 2)}\nMode: {round(mode(moves_taken), 2)}\nMin: {min(moves_taken)}\nMax: {max(moves_taken)}")

# Histograms
bins = [x for x in range(max(moves_taken))]
plt.hist(moves_taken, bins=bins, edgecolor='none')
plt.title(f"Histogram of moves taken over {runs} games")
plt.ylabel(f"Number of games (total {runs})")
plt.xlabel("Moves per game")
plt.show()

finish_time = datetime.now()

print(f"Played the game {runs} times in {finish_time - start_time} seconds.")
