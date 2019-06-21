from scipy import integrate


def f(x):
    return (1 - x ** 2) ** (1 / 2)


w, err = integrate.quad(f, -1, 1)
print(w, err)

w, err = integrate.quad(lambda x: x * x, 0, 1)
print(w, err)

# 1.5707963267948983 1.0002354500215915e-09
# 0.33333333333333337 3.700743415417189e-15
