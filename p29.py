import numpy as np
x=np.array([0,2,4,5,7,9,15,20,22])
y=np.array([-3,-1,4,3,5,9,5,6,7])

from scipy.optimize import curve_fit
def f(x,a,b):
    return a*np.sqrt(x)+b
popt,pcov=curve_fit(f,x,y)
a,b=popt
ypred=f(x,a,b)

from sklearn.metrics import r2_score
print("r2 = ",r2_score(y,ypred))
import matplotlib.pyplot as plt
plt.scatter(x,y,label="data")
plt.plot(x,ypred,label="fit")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
