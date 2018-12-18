## find a pattern in the data and then use that to calculate out the value

loop = [616,588,582,625,598,592,601,616,588,582,625,598,592,601]

t = 10000
i = 0

while t != 1000000000:
    t = t + 1000
    i = i + 1

print(t, loop[i % len(loop)] )

