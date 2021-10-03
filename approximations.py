def left(f, a, b, n):
    if a > b:
        print("Incorrect Bounds")
        return 0
    else:
        delta_x = (b - a) / n
        approx = 0
        for i in range(0, n):
            approx += f(a + (i * delta_x))
        return approx * delta_x


def right(f, a, b, n):
    if a > b:
        print("Incorrect Bounds")
        return 0
    else:
        delta_x = (b - a) / n
        approx = 0
        for i in range(1, n + 1):
            approx += f(a + (i * delta_x))
        return approx * delta_x


def midpoint(f, a, b, n):
    if a > b:
        print("Incorrect Bounds")
        return 0
    elif str(type(f)) == "<class 'function'>":
        delta_x = (b - a) / n
        approx = 0
        for i in range(1, n + 1):
            x_bar = ((a + ((i - 1) * delta_x)) + (a + (i * delta_x))) / 2
            approx += f(x_bar)
        return approx * delta_x
    elif str(type(f)) == "<class 'dict'>":
        print("No midpoint estimations are made from tables of value.")


def trapezoidal(f, a, b, n):
    if a > b:
        print("Incorrect Bounds")
        return 0
    elif str(type(f)) == "<class 'function'>":
        delta_x = (b - a) / n
        approx = f(a) + f(b)
        for i in range(1, n):
            approx += 2 * f(a + (i * delta_x))
        return approx * (delta_x / 2)
    elif str(type(f)) == "<class 'dict'>":
        delta_x = (b - a) / n
        approx = f['y'][0] + f['y'][-1] + (2 * sum(f['y'][1:-1]))
        return approx * (delta_x / 2)


def Simpson(f, a, b, n):
    if a > b:
        print('Incorrect bounds')
        return 0
    if n % 2 != 0:
        print("Simpson's rule requires that n be even")
        return 0
    elif str(type(f)) == "<class 'function'>":
        delta_x = (b - a) / n
        odd_indicies = 0
        for i in range(1, int(n / 2) + 1):
            odd_indicies += 4 * f(a + (2 * i - 1) * delta_x)
        even_indicies = 0
        for i in range(1, int(n / 2)):
            even_indicies += 2 * f(a + 2 * i * delta_x)
        approx = ((delta_x / 3) * (f(a) + f(b) + odd_indicies + even_indicies))
        return approx
    elif str(type(f)) == "<class 'dict'>":
        delta_x = (b - a) / n
        odd_sum = 4 * sum(f['y'][1:-1:2])
        even_sum = 2 * sum(f['y'][2:-1:2])
        approx = f['y'][0] + f['y'][-1] + odd_sum + even_sum
        return approx * (delta_x / 3)
