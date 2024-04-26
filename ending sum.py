import math

n = 20
x = 0.2
k = 1
b = 1
c = x/6
a = b*c
s = a

for k in range (1, n+1):
    b = k*k
    c = c*x/(2*k*(2*k+1))
    a = b*c
    s = s + a
    y1 = ((x+1)/math.sqrt(x))*math.sinh(x)
    y2 = math.cosh(x)
    y = 0.25*(y1-y2)
print ('s =', s, 'y =', y) 
