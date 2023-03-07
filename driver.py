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

    love_fn = lambda x: rho2 / rho1 * np.sqrt(H**2 * (beta1**-2 - beta2**-2) - x**2) / x

    love_fn_prime = lambda x: rho2 / rho1 * -(H**2 * (beta1**-2 - beta2**-2)) / (x**2 * np.sqrt(H**2 * (beta1**-2 - beta2**-2) - x**2))

    xk, k, eps_a_arr = rf.root_newton_raphson(1.5,love_fn,love_fn_prime)

    print(f"The value of the root is: {xk} and it took {k} iterations to converge.")

    xk, k, eps_a_arr = rf.root_secant_modified(1,1.5,love_fn)

    print(f"The value of the root is: {xk} and it took {k} iterations to converge.")

def love():
    return None

if __name__ == "__main__":
        main()