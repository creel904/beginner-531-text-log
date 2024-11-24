import argparse


# rounds to closest multiple of 5
def rd5(x, base=5):
  return base * round(x/base)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-s", "--squat", help="squat TM", type=int)
    parser.add_argument("-b", "--bench", help="bench TM", type=int)
    parser.add_argument("-d", "--deadlift", help="deadlift TM", type=int)
    parser.add_argument("-p", "--press", help="press TM", type=int)
    parser.add_argument("--start", help="enter A or B, start 3 week cycle day 1 with A squat&bench or B deadlift&press", type=str)

    args = parser.parse_args() 

    squat = args.squat
    bench = args.bench
    deadlift = args.deadlift
    press = args.press
    start = args.start

    week1 = [65, 75, 85]
    week2 = [70, 80, 90]
    week3 = [75, 85, 95]


    if start == "B":
        templateStr = '''\

===============================
5/3/1 Week 1 (65%(x16), 75%(x10), 85%(x6))

-------------------------------
W1d1

Press (TM {press}: 65%(x16), 75%(x10), 85%(x6))
5 {p11}
5 {p12}
5+ {p13}
5 {p12}
5 {p12}
5 {p12}
5 {p12}
5+ {p12}

Deadlift (TM {deadlift}: 65%(x16), 75%(x10), 85%(x6))
5 {d11}
5 {d12}
5+ {d13}
5 {d11}
5 {d11}
5 {d11}
5 {d11}
5+ {d11}

Vertical Pull
Quad



-------------------------------
W1d2

Squat (TM {squat}: 65%(x16), 75%(x10), 85%(x6))
5 {s11}
5 {s12}
5+ {s13}
5 {s11}
5 {s11}
5 {s11}
5 {s11}
5+ {s11}

Bench (TM {bench}: 65%(x16), 75%(x10), 85%(x6))
5 {b11}
5 {b12}
5+ {b13}
5 {b12}
5 {b12}
5 {b12}
5 {b12}
5+ {b12}

Horizontal pull
Hamstrings

-------------------------------
W1d3

Press (TM {press}: 65%(x16), 75%(x10), 85%(x6))
5 {p11}
5 {p12}
5+ {p13}
5 {p12}
5 {p12}
5 {p12}
5 {p12}
5+ {p12}

Deadlift (TM {deadlift}: 65%(x16), 75%(x10), 85%(x6))
5 {d11}
5 {d12}
5+ {d13}
5 {d11}
5 {d11}
5 {d11}
5 {d11}
5+ {d11}

Vertical Pull
Quad

===============================
5/3/1 Week 2 (70%(x12), 80%(x8), 90%(4))

-------------------------------
Wk2d1

Bench (TM {bench}: 70%(x12), 80%(x8), 90%(4))
3 {b21}
3 {b22}
3+ {b23}
5 {b22}
5 {b22}
5 {b22}
5 {b22}
5+ {b22}

Squat (TM {squat}: 70%(x12), 80%(x8), 90%(4))
3 {s21}
3 {s22}
3+ {s23}
5 {s21}
5 {s21}
5 {s21}
5 {s21}
5+ {s21}

Horizontal pull
Hamstrings

-------------------------------
Wk2d2

Press (TM {press}: 70%(x12), 80%(x8), 90%(4))
3 {p21}
3 {p22}
3+ {p23}
5 {p22}
5 {p22}
5 {p22}
5 {p22}
5+ {p22}

Deadlift (TM {deadlift}: 70%(x12), 80%(x8), 90%(4))
3 {d21}
3 {d22}
3+ {d23}
5 {d21}
5 {d21}
5 {d21}
5 {d21}
5+ {d21}

Vertical Pull
Quad

-------------------------------
Wk2d3

Bench (TM {bench}: 70%(x12), 80%(x8), 90%(4))
3 {b21}
3 {b22}
3+ {b23}
5 {b22}
5 {b22}
5 {b22}
5 {b22}
5+ {b22}

Squat (TM {squat}: 70%(x12), 80%(x8), 90%(4))
3 {s21}
3 {s22}
3+ {s23}
5 {s21}
5 {s21}
5 {s21}
5 {s21}
5+ {s21}

Horizontal pull
Hamstrings


===============================
5/3/1 Week 3 (75%(x10), 85%(x6), 95%(x2))

-------------------------------
Wk3d1

Deadlift (TM {deadlift}: 75%(x10), 85%(x6), 95%(x2))
5 {d31}
3 {d32}
1+ {d33}
5 {d31}
5 {d31}
5 {d31}
5 {d31}
5+ {d31}

Press (TM {press}: 75%(x10), 85%(x6), 95%(x2))
5 {p31}
3 {p32}
1+ {p33}
5 {p32}
5 {p32}
5 {p32}
5 {p32}
5+ {p32}

Vertical Pull
Quad

-------------------------------
Wk3d2

Bench (TM {bench}: 75%(x10), 85%(x6), 95%(x2))
5 {b31}
3 {b32}
1+ {b33}
5 {b32}
5 {b32}
5 {b32}
5 {b32}
5+ {b32}

Squat (TM {squat}: 75%(x10), 85%(x6), 95%(x2))
5 {s31}
3 {s32}
1+ {s33}
5 {s31}
5 {s31}
5 {s31}
5 {s31}
5+ {s31}

Horizontal pull
Hamstrings

-------------------------------
Wk3d3

Deadlift (TM {deadlift}: 75%(x10), 85%(x6), 95%(x2))
5 {d31}
3 {d32}
1+ {d33}
5 {d31}
5 {d31}
5 {d31}
5 {d31}
5+ {d31}

Press (TM {press}: 75%(x10), 85%(x6), 95%(x2))
5 {p31}
3 {p32}
1+ {p33}
5 {p32}
5 {p32}
5 {p32}
5 {p32}
5+ {p32}

Vertical Pull
Quad

    '''.format(squat=squat, bench=bench, deadlift=deadlift, press=press, 
    s11=rd5(squat*week1[0]/100), s12=rd5(squat*week1[1]/100), s13=rd5(squat*week1[2]/100),
    b11=rd5(bench*week1[0]/100), b12=rd5(bench*week1[1]/100), b13=rd5(bench*week1[2]/100),
    d11=rd5(deadlift*week1[0]/100), d12=rd5(deadlift*week1[1]/100), d13=rd5(deadlift*week1[2]/100),
    p11=rd5(press*week1[0]/100), p12=rd5(press*week1[1]/100), p13=rd5(press*week1[2]/100),

    s21=rd5(squat*week2[0]/100), s22=rd5(squat*week2[1]/100), s23=rd5(squat*week2[2]/100),
    b21=rd5(bench*week2[0]/100), b22=rd5(bench*week2[1]/100), b23=rd5(bench*week2[2]/100),
    d21=rd5(deadlift*week2[0]/100), d22=rd5(deadlift*week2[1]/100), d23=rd5(deadlift*week2[2]/100),
    p21=rd5(press*week2[0]/100), p22=rd5(press*week2[1]/100), p23=rd5(press*week2[2]/100),

    s31=rd5(squat*week3[0]/100), s32=rd5(squat*week3[1]/100), s33=rd5(squat*week3[2]/100),
    b31=rd5(bench*week3[0]/100), b32=rd5(bench*week3[1]/100), b33=rd5(bench*week3[2]/100),
    d31=rd5(deadlift*week3[0]/100), d32=rd5(deadlift*week3[1]/100), d33=rd5(deadlift*week3[2]/100),
    p31=rd5(press*week3[0]/100), p32=rd5(press*week3[1]/100), p33=rd5(press*week3[2]/100)
    )
    else:
        templateStr = '''\

===============================
5/3/1 Week 1 (65%(x16), 75%(x10), 85%(x6))

-------------------------------
W1d1

Bench (TM {bench}: 65%(x16), 75%(x10), 85%(x6))
5 {b11}
5 {b12}
5+ {b13}
5 {b12}
5 {b12}
5 {b12}
5 {b12}
5+ {b12}

Squat (TM {squat}: 65%(x16), 75%(x10), 85%(x6))
5 {s11}
5 {s12}
5+ {s13}
5 {s11}
5 {s11}
5 {s11}
5 {s11}
5+ {s11}

Horizontal pull
Hamstrings

-------------------------------
W1d2

Press (TM {press}: 65%(x16), 75%(x10), 85%(x6))
5 {p11}
5 {p12}
5+ {p13}
5 {p12}
5 {p12}
5 {p12}
5 {p12}
5+ {p12}

Deadlift (TM {deadlift}: 65%(x16), 75%(x10), 85%(x6))
5 {d11}
5 {d12}
5+ {d13}
5 {d11}
5 {d11}
5 {d11}
5 {d11}
5+ {d11}

Vertical Pull
Quad

-------------------------------
W1d3

Squat (TM {squat}: 65%(x16), 75%(x10), 85%(x6))
5 {s11}
5 {s12}
5+ {s13}
5 {s11}
5 {s11}
5 {s11}
5 {s11}
5+ {s11}

Bench (TM {bench}: 65%(x16), 75%(x10), 85%(x6))
5 {b11}
5 {b12}
5+ {b13}
5 {b12}
5 {b12}
5 {b12}
5 {b12}
5+ {b12}

Horizontal pull
Hamstrings

===============================
5/3/1 Week 2 (70%(x12), 80%(x8), 90%(4))

-------------------------------
Wk2d1

Deadlift (TM {deadlift}: 70%(x12), 80%(x8), 90%(4))
3 {d21}
3 {d22}
3+ {d23}
5 {d21}
5 {d21}
5 {d21}
5 {d21}
5+ {d21}

Press (TM {press}: 70%(x12), 80%(x8), 90%(4))
3 {p21}
3 {p22}
3+ {p23}
5 {p22}
5 {p22}
5 {p22}
5 {p22}
5+ {p22}

Vertical Pull
Quad

-------------------------------
Wk2d2

Bench (TM {bench}: 70%(x12), 80%(x8), 90%(4))
3 {b21}
3 {b22}
3+ {b23}
5 {b22}
5 {b22}
5 {b22}
5 {b22}
5+ {b22}

Squat (TM {squat}: 70%(x12), 80%(x8), 90%(4))
3 {s21}
3 {s22}
3+ {s23}
5 {s21}
5 {s21}
5 {s21}
5 {s21}
5+ {s21}

Horizontal pull
Hamstrings

-------------------------------
Wk2d3

Press (TM {press}: 70%(x12), 80%(x8), 90%(4))
3 {p21}
3 {p22}
3+ {p23}
5 {p22}
5 {p22}
5 {p22}
5 {p22}
5+ {p22}

Deadlift (TM {deadlift}: 70%(x12), 80%(x8), 90%(4))
3 {d21}
3 {d22}
3+ {d23}
5 {d21}
5 {d21}
5 {d21}
5 {d21}
5+ {d21}

Vertical Pull
Quad


===============================
5/3/1 Week 3 (75%(x10), 85%(x6), 95%(x2))

-------------------------------
Wk3d1

Squat (TM {squat}: 75%(x10), 85%(x6), 95%(x2))
5 {s31}
3 {s32}
1+ {s33}
5 {s31}
5 {s31}
5 {s31}
5 {s31}
5+ {s31}

Bench (TM {bench}: 75%(x10), 85%(x6), 95%(x2))
5 {b31}
3 {b32}
1+ {b33}
5 {b32}
5 {b32}
5 {b32}
5 {b32}
5+ {b32}

Horizontal pull
Hamstrings

-------------------------------
Wk3d2

Deadlift (TM {deadlift}: 75%(x10), 85%(x6), 95%(x2))
5 {d31}
3 {d32}
1+ {d33}
5 {d31}
5 {d31}
5 {d31}
5 {d31}
5+ {d31}

Press (TM {press}: 75%(x10), 85%(x6), 95%(x2))
5 {p31}
3 {p32}
1+ {p33}
5 {p32}
5 {p32}
5 {p32}
5 {p32}
5+ {p32}

Vertical Pull
Quad

-------------------------------
Wk3d3

Bench (TM {bench}: 75%(x10), 85%(x6), 95%(x2))
5 {b31}
3 {b32}
1+ {b33}
5 {b32}
5 {b32}
5 {b32}
5 {b32}
5+ {b32}

Squat (TM {squat}: 75%(x10), 85%(x6), 95%(x2))
5 {s31}
3 {s32}
1+ {s33}
5 {s31}
5 {s31}
5 {s31}
5 {s31}
5+ {s31}

Horizontal pull
Hamstrings

    '''.format(squat=squat, bench=bench, deadlift=deadlift, press=press, 
    s11=rd5(squat*week1[0]/100), s12=rd5(squat*week1[1]/100), s13=rd5(squat*week1[2]/100),
    b11=rd5(bench*week1[0]/100), b12=rd5(bench*week1[1]/100), b13=rd5(bench*week1[2]/100),
    d11=rd5(deadlift*week1[0]/100), d12=rd5(deadlift*week1[1]/100), d13=rd5(deadlift*week1[2]/100),
    p11=rd5(press*week1[0]/100), p12=rd5(press*week1[1]/100), p13=rd5(press*week1[2]/100),

    s21=rd5(squat*week2[0]/100), s22=rd5(squat*week2[1]/100), s23=rd5(squat*week2[2]/100),
    b21=rd5(bench*week2[0]/100), b22=rd5(bench*week2[1]/100), b23=rd5(bench*week2[2]/100),
    d21=rd5(deadlift*week2[0]/100), d22=rd5(deadlift*week2[1]/100), d23=rd5(deadlift*week2[2]/100),
    p21=rd5(press*week2[0]/100), p22=rd5(press*week2[1]/100), p23=rd5(press*week2[2]/100),

    s31=rd5(squat*week3[0]/100), s32=rd5(squat*week3[1]/100), s33=rd5(squat*week3[2]/100),
    b31=rd5(bench*week3[0]/100), b32=rd5(bench*week3[1]/100), b33=rd5(bench*week3[2]/100),
    d31=rd5(deadlift*week3[0]/100), d32=rd5(deadlift*week3[1]/100), d33=rd5(deadlift*week3[2]/100),
    p31=rd5(press*week3[0]/100), p32=rd5(press*week3[1]/100), p33=rd5(press*week3[2]/100)
    )




    print(templateStr)


if __name__=="__main__":
    main()
