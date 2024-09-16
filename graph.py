import matplotlib.pyplot as plt
from matplotlib import pyplot as pltt

x = [ i for i in range(0, 11)]
y = [ y ** 2 for y in x]

print(x)
print(y)

pltt.plot(x, y)
pltt.show()