import matplotlib.pyplot as plt


def fx_square(x):
    return x * x


def fx_square_list(n):
    items = []
    for i in range(n):
        items.append(i * i)
    return items


def plot_f(n):
    plt.plot(range(n), fx_square_list(n))
    plt.show()


n = 88
print(fx_square_list(n))
plot_f(n)


def fx_square_list2(points):
    values = []
    for point in points:
        values.append(point * point)
    return values


points = range(-100, 100)
values = fx_square_list2(points)
plt.plot(points, values)
plt.show()
