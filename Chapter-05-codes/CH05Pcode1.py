# This code finds the roots
# of: f(x) = x^2 - 2x - 3
# using 'Bisection Method'
def f(x):
    return x**2 - 2*x - 3
# First root in domain [0,4]
a1, b1 = 0, 4
tol= 1e-6 #Stoping tolerance
X2 = 500  #Maximum iterations
#Bisection Method for 1st root
iter_count = 0
while (b1 - a1) / 2 > tol:
    c1 = (a1 + b1) / 2
    if f(c1) == 0: break
    elif f(a1)*f(c1)<0: b1=c1
    else: a1 = c1
    iter_count += 1
    if iter_count > X2:
     print('Max iterations');break
root1 = (a1 + b1) / 2
print(f'First root: {root1}')
# Second root in domain [-4,0]
a2, b2 = -4, 0; iter_count =0
# for second root
while (b2 - a2) / 2 > tol:
    c2 = (a2 + b2) / 2
    if f(c2) == 0: break
    elif f(a2)*f(c2)<0: b2=c2
    else: a2 = c2
    iter_count += 1
    if iter_count > X2:
     print('Max iterations'); break
root2 = (a2 + b2) / 2
print(f'Second root: {root2}')
# End of Python script
