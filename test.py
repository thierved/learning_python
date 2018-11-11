x = 10
L = [0, 1]

def func(a, S):
    S[0] = 'he'    
    a = 4

func(x, L)

print(x, L)
## args

def func1(*val):
    for x in val:
        print(x)

def func2(**val):
    print(val)

func2(x=1, y='h0', z=0)