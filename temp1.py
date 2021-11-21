import matplotlib.pyplot as plt
import math

N = 20

def f(x, coeff):
    sum = 0
    for i in range(N//2):
        sum += coeff[i] * math.cos(i*x)
        sum += coeff[N//2+i] * math.sin((N//2+i)*x)
    return sum

a = [0, -15, 2, -20, 17, -24, -17, -1, 20, 7, 1, 15, -27, 23, -12, 19, -10, 13, 6, -13]
e = [-0.002111083188755525, -14.968627082279665, 2.0367368228386047, -19.98295193675899, 17.001636128366673, -23.991490725855293, -16.989448155682997, -1.003071355595473, 20.010716977706664, 6.9886182669122725, 0.999590651132873, 14.976791037653294, -26.974557821944714, 22.995559514817984, -11.997615521287951, 18.984197232651606, -9.973204372424583, 12.988092423558152, 5.994103773113304, -12.995669156969832]


x =  list(range(-50, 50))
y_a = [f(i, a) for i in x]
y_e = [f(i, e) for i in x]

plt.plot(x, y_a, 'k')
#plt.plot(x, y_e, 'g--', label='estimated function')
#plt.legend(fontsize='small')
plt.show()