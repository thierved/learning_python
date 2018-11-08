
def func():
    global x, y
    x = 1
    y = x + 1
    z = y * x

    def non():
        nonlocal z
        z += 1

    non()

    print(z)

func()

print(x, y)
