from itertools import cycle
from random import randint
import random
import time

tunes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
guitar = [2, 4, 7, 9, 11]
lenT = len(tunes)
correct = 0
wrong = 0
print 'Get the correct sum of semi tones'
start_time = time.time()
for x in range(0, 10):
    rand1 = random.choice(guitar)
    rand2 = randint(1,12)
    ans = raw_input('{0} + {1}: '.format(*(tunes[rand1 % lenT],rand2)))
    if (ans == tunes[(rand1 + rand2) % lenT]):
        correct += 1
    else:
        wrong += 1
print 'Has ', correct, 'corrects and ', wrong, 'wrongs'
print("--- %s seconds ---" % (time.time() - start_time))


