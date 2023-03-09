import matplotlib.pyplot as plt
import numpy as np

import root_finder as rf

def main():
    """Main function"""

    #constants
    rho1 = 1800
    rho2 = 2500
    beta1 = 1900
    beta2 = 3200
    H = 4000
    f=1
    #f=range(0.1,10,.1)

    love_fn = lambda x: rho2 / rho1 * np.sqrt(H**2 * (beta1**-2 - beta2**-2) - x**2) / x - np.tan(2*np.pi*f*x)

    love_fn_prime = lambda x: rho2 / rho1 * -(H**2 * (beta1**-2 - beta2**-2)) / (x**2 * np.sqrt(H**2 * (beta1**-2 - beta2**-2) - x**2)) - (2*np.pi*f)*(1/np.cos(2*np.pi*f*x))**2

    xk, k, eps_a_arr = rf.root_newton_raphson(0.3,love_fn,love_fn_prime)

    print(f"Newton Raphson: The value of the root is: {xk} and it took {k} iterations to converge.")

    xk, k, eps_a_arr = rf.root_secant_modified(0.3,0.2,love_fn)

    print(f"Modified Secant: The value of the root is: {xk} and it took {k} iterations to converge.")

def love(x,f):
    return None

def love_prime(x,f):
     return None

if __name__ == "__main__":
        main()