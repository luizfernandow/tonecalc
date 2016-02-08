#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import cycle
from random import randint
import random
import time
import sqlite3 as lite
import sys

print '---------------------------------------------------------'
print '------------- Tonecalc. Exercise your brain -------------'
print '---------------------------------------------------------'
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
timeTotal = (time.time() - start_time) + wrong * 25
print("--- %s seconds ---" % timeTotal)

try:
    con = lite.connect('points.db')
    con.row_factory = lite.Row
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Points(time_point FLOAT)")
    cur.execute("INSERT INTO Points (time_point) VALUES(?)", (timeTotal,))
    cur.execute("SELECT min(time_point) as best FROM Points")
    row = cur.fetchone()
    print("--- Your best is %s seconds ---" % row['best'])
    cur.execute("SELECT avg(time_point) as avg FROM Points")
    row = cur.fetchone()
    print("--- Your average is %s seconds ---" % row['avg'])

except lite.Error, e:

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:

    if con:
        con.close()
