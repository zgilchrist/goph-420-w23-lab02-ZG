import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve, brentq

import root_finder as rf

def main():
    """Main function"""

    #constants
    rho1 = 1800
    rho2 = 2500
    beta1 = 1900
    beta2 = 3200
    H = 4000
    
    
    f = np.arange(0.1,10,0.5)
    
#zeta max = 1.693999104
#zeta min = 0

    love_fn = lambda x,f: rho2 / rho1 * np.sqrt(H**2 * (beta1**-2 - beta2**-2) - x**2) / x - np.tan(2*np.pi*f*x)

    love_fn_prime = lambda x,f: rho2 / rho1 * -(H**2 * (beta1**-2 - beta2**-2)) / (x**2 * np.sqrt(H**2 * (beta1**-2 - beta2**-2) - x**2)) - (2*np.pi*f)*(1/np.cos(2*np.pi*f*x))**2

    xk_arr = []
    guesses = np.arange(0.1,1.5,0.1)
    #for index, freq in enumerate(f):
       # for guess in guesses:
         #   xk, k, eps_a_arr = rf.root_newton_raphson(guess,love_fn,love_fn_prime,f[index])

         #   print(f"Guess for xk is {guess} Newton Raphson: At frequency {freq}Hz, the value of the root is: {xk} and it took {k} iterations to converge.")
         #   xk_arr.append(xk)
    love_fn_fsolve = lambda x: rho2 / rho1 * np.sqrt(H**2 * (beta1**-2 - beta2**-2) - x**2) / x - np.tan(2*np.pi*f[1]*x)
    print(fsolve(love_fn_fsolve,guesses[0]))
    print(brentq(love_fn_fsolve,-1.6,1.6))
    #xk, k, eps_a_arr = rf.root_secant_modified(0.3,0.2,love_fn)

    #print(f"Modified Secant: The value of the root is: {xk} and it took {k} iterations to converge.")
    

    plt.figure()
    plt.subplot(311)
    #plt.plot(dt,get_t_star(dt,H[0],'rk1'),'r-o',label = 'RK1')
   # plt.loglog(dt,get_t_star(dt,H[0],'rk4'),'b-o',label = 'RK4')
    #plt.title('Total drop time vs. time step at H = 10 in loglog space')
    plt.legend()
    plt.xlabel("Time Step (s)")
    plt.ylabel("Total Drop Time (s)")



def love(x,f):
    return None

def love_prime(x,f):
     return None

   

if __name__ == "__main__":
        main()