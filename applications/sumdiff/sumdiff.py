"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
q = set(range(1, 100))
# q = (1, 3, 4, 7, 12)


def function(x):
    return x * 4 + 6


# Your code here
calculated = {}
solutionStringsArray = []


for a in q:
    e = 0
    if a in calculated:
        e = calculated[a]
    else:
        e = function(a)
        calculated[a] = e

    for b in q:
        f = 0
        if b in calculated:
            f = calculated[b]
        else:
            f = function(b)
            calculated[b] = f

        for c in q:
            g = 0
            if c in calculated:
                g = calculated[c]
            else:
                g = function(c)
                calculated[c] = g

            for d in q:
                h = 0
                if d in calculated:
                    h = calculated[d]
                else:
                    h = function(d)
                    calculated[d] = h
                if e + f == g - h:
                    solutionStringsArray.append([a, b, c, d])
                    # solutionStringsArray.append(
                    #     f"f({a}) + f({b}) = f({c}) - f({d})    {e} + {f} = {g} - {h}")
print(solutionStringsArray)
