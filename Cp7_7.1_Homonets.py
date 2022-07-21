import math

def my_sqrt (i, n, Epsilon):
   k = 2
   term1 = (i+n)/2
   term2 = (2/3)*term1+(i/(3*term1**2))
   while abs(term2-term1)>Epsilon:
       term1=term2
       term2 = 1/(((n-1)/n)*term1+i/(n*(term1**(n-1))))
       k += 2
       return term2

import itertools
Epsilon = 0.0001
a = 6
b = 8
print("----------------------------------------")
print("  x ", " : ", "    y ", " : ", "   yt ", "   : ", " error ")
print("----------------------------------------")

for i in itertools.count(start=a, step=0.2):
    if i >= b:
        break
    n = 2
    y = my_sqrt(i, n, Epsilon)
    y1 = 1/(math.pow(i,(1/2)))
    error = abs(y-y1)
    print("%.2f" %i, " : ", "%.4f" %y, " : ", '%4f' %y1, " : ", '%.4f' %error )

