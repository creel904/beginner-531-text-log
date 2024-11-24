### Exercise Program
This creates 531 for beginners program that follows ABA-BAB
For upper-body movements it follows Second-Set-Last SSLx5 and last set as AMRAP + set.
For lower-body movements it follows First-Set-Last FSLx5 and last set as AMRAP + set.

Additionally, it adds accessories that are antagonists to that days movements (ie for bench press, horizontal rows would be a good antagonist accessory).

### Requirements:
shell with python3 


### Usages:

```
# get the code
git clone https://github.com/creel904/beginner-531-text-log.git`
cd beginner-531-text-log

# run program (enter your Training Maxes for each main lift):
python3 beginner531.py -s 265 -b 190 -d 250 -p 135 --start="B"

# or, alternatively:
python3 beginner531.py --squat=265 --bench=190 --deadlift=250 --press=135 --start="B"

# to show help
python3 beginner531.py -h
python3 beginner531.py --help

# start argument
allows 3-week 5/3/1 cycle to start on squat day or deadlift day
--start="A" or --start="B"

```

### Example output (start B):
```
===============================
5/3/1 Week 1 (65%(x16), 75%(x10), 85%(x6))

-------------------------------
W1d1

Press (TM 135: 65%(x16), 75%(x10), 85%(x6))
5 90
5 100
5+ 115
5 100
5 100
5 100
5 100
5+ 100

Deadlift (TM 250: 65%(x16), 75%(x10), 85%(x6))
5 160
5 190
5+ 210
5 160
5 160
5 160
5 160
5+ 160

Vertical Pull
Quad

-------------------------------
W1d2

Squat (TM 265: 65%(x16), 75%(x10), 85%(x6))
5 170
5 200
5+ 225
5 170
5 170
5 170
5 170
5+ 170

Bench (TM 190: 65%(x16), 75%(x10), 85%(x6))
5 125
5 140
5+ 160
5 140
5 140
5 140
5 140
5+ 140

Horizontal pull
Hamstrings

-------------------------------
W1d3

Press (TM 135: 65%(x16), 75%(x10), 85%(x6))
5 90
5 100
5+ 115
5 100
5 100
5 100
5 100
5+ 100

Deadlift (TM 250: 65%(x16), 75%(x10), 85%(x6))
5 160
5 190
5+ 210
5 160
5 160
5 160
5 160
5+ 160

Vertical Pull
Quad

===============================
5/3/1 Week 2 (70%(x12), 80%(x8), 90%(4))

-------------------------------
Wk2d1

Bench (TM 190: 70%(x12), 80%(x8), 90%(4))
3 135
3 150
3+ 170
5 150
5 150
5 150
5 150
5+ 150

Squat (TM 265: 70%(x12), 80%(x8), 90%(4))
3 185
3 210
3+ 240
5 185
5 185
5 185
5 185
5+ 185

Horizontal pull
Hamstrings

-------------------------------
Wk2d2

Press (TM 135: 70%(x12), 80%(x8), 90%(4))
3 95
3 110
3+ 120
5 110
5 110
5 110
5 110
5+ 110

Deadlift (TM 250: 70%(x12), 80%(x8), 90%(4))
3 175
3 200
3+ 225
5 175
5 175
5 175
5 175
5+ 175

Vertical Pull
Quad

-------------------------------
Wk2d3

Bench (TM 190: 70%(x12), 80%(x8), 90%(4))
3 135
3 150
3+ 170
5 150
5 150
5 150
5 150
5+ 150

Squat (TM 265: 70%(x12), 80%(x8), 90%(4))
3 185
3 210
3+ 240
5 185
5 185
5 185
5 185
5+ 185

Horizontal pull
Hamstrings


===============================
5/3/1 Week 3 (75%(x10), 85%(x6), 95%(x2))

-------------------------------
Wk3d1

Deadlift (TM 250: 75%(x10), 85%(x6), 95%(x2))
5 190
3 210
1+ 240
5 190
5 190
5 190
5 190
5+ 190

Press (TM 135: 75%(x10), 85%(x6), 95%(x2))
5 100
3 115
1+ 130
5 115
5 115
5 115
5 115
5+ 115

Vertical Pull
Quad

-------------------------------
Wk3d2

Bench (TM 190: 75%(x10), 85%(x6), 95%(x2))
5 140
3 160
1+ 180
5 160
5 160
5 160
5 160
5+ 160

Squat (TM 265: 75%(x10), 85%(x6), 95%(x2))
5 200
3 225
1+ 250
5 200
5 200
5 200
5 200
5+ 200

Horizontal pull
Hamstrings

-------------------------------
Wk3d3

Deadlift (TM 250: 75%(x10), 85%(x6), 95%(x2))
5 190
3 210
1+ 240
5 190
5 190
5 190
5 190
5+ 190

Press (TM 135: 75%(x10), 85%(x6), 95%(x2))
5 100
3 115
1+ 130
5 115
5 115
5 115
5 115
5+ 115

Vertical Pull
Quad
```

