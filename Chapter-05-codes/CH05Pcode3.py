# This code finds density k 
# at which traffic flow is
# maximized for traffic flow q 
# f(k) = 100k - k^2 - 2500
# using Newton-Raphson Method
def newton_raphson(f, f_prime, k0,\
        epsilon, max_it):
  for iter in range(1, max_it + 1):
    f_k = f(k0)
    f_prime_k = f_prime(k0)
    k_next=k0-f_k/f_prime_k #Next value
    diff=abs(k_next-k0) #Convergence       
    if diff<epsilon:#Check convergence
      final=round(k_next)#Round answer
      print(f"Iterations = {iter}")
      print(f"Solution, k = {final}")
      return final      
    k0=k_next #Update k0   
  print("Maximum iterations")
  return None
#Define functions f(k),f'(k)
f=lambda k: 100*k-k**2-2500
f_prime= lambda k: 100-2*k
# Initial guess, parameters
k0 = 60
epsilon = 0.1
max_it = 500
# Perform Newton-Raphson method
solution=newton_raphson(f,f_prime,\
     k0, epsilon, max_it)
# End of Python script
