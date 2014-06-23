import matplotlib.pyplot as plt
import random

t = 1000
x0 = random.uniform(0,1)
x1 = random.uniform(0,1)

x0_values = [x0]
x1_values = [x1]
profit = [(4,4),(0,3),(3,0),(2,2)] # [左上、右上、左下、右下]

for i in range(t):

    if profit[0][0]*(1-x0) + profit[1][0]*x0 > profit[2][0]*(1-x0) + profit[3][0]*x0:
         a0 = 0
    elif profit[0][0]*(1-x0) + profit[1][0]*x0 < profit[2][0]*(1-x0) + profit[3][0]*x0:
         a0 = 1
    else:
         a0 = random.choice([0,1])

    if profit[0][1]*(1-x1) + profit[2][1]*x1 > profit[1][1]*(1-x1) + profit[3][1]*x1:
         a1 = 0
    elif profit[0][1]*(1-x1) + profit[2][1]*x1 < profit[1][1]*(1-x1) + profit[3][1]*x1:
         a1 = 1
    else:
         a1 = random.choice([0,1])

    x0 = x0 + (a1 - x0)/(i + 2)
    x1 = x1 + (a0 - x1)/(i + 2)

    x0_values.append(x0)
    x1_values.append(x1)

plt.plot(x0_values, 'b-', label = 'x_0(t)')
plt.plot(x1_values, 'r-', label = 'x_1(t)')
plt.legend()
plt.show()