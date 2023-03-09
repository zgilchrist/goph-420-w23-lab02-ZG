import numpy as np
from scipy.optimize import fsolve


def root_newton_raphson(x0, f, dfdx, eps_s = 1e-8):
    """Finds a root of a function using the Newton-Raphson Method
    
    Parameters
    ----------
    x0: float
        Initial guess of root location

    f: float
        function

    dfdx: float
        first derivative of the function
    
    eps_s: float
        tolerance for approximate relative error
   
    Returns
    -------
    root_value: float
        final estimate of the root
    
    n_iterations: int
        number of iterations to convergence
    
    eps_a: np.ndarray
        one-dimensional vector of the approximate relative error at each iteration 
    """
    xk = x0
    eps_a = 2 * eps_s
    k = 0
    eps_a_arr = np.zeros(0)

    while eps_a > eps_s:
        dx = -f(xk) / dfdx(xk)
        xk += dx
        eps_a = np.abs(dx/xk)
        eps_a_arr = np.append(eps_a_arr,eps_a)
        k += 1
    return xk, k, eps_a_arr





def root_secant_modified(x0, x1, f, eps_s = 1e-8):
    """Finds a root of a function using the Modified Secant Method
    
    Parameters
    ----------
    x0: floats
        Initial guess of root location

    f: float
        function

    dx: float
        step size for derivative estimations

    eps_s: float
        tolerance for approximate relative error
   
    Returns
    -------
    root_value: float
        final estimate of the root
    
    n_iterations: int
        number of iterations to convergence
    
    eps_a: np.ndarray
        one-dimensional vector of the approximate relative error at each iteration 
    """
    eps_a = 2 * eps_s
    k = 0
    eps_a_arr = np.zeros(0)
    
    while  eps_a > eps_s:
        x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))
        x0, x1 = x1, x2

        eps_a = np.abs(x1 - x0)
        eps_a_arr = np.append(eps_a_arr,eps_a)

        k += 1
    return x1, k, eps_a_arr






    xk_0 = x0
    xk_1 = dx + x0
    eps_a = 2 * eps_s
    k = 0
    eps_a_arr = np.zeros(0)

    while eps_a > eps_s:
        
        x_diff = xk_0 - xk_1
        dfdx_est = (f(xk_0) - f(xk_1)) / (x_diff)
        f_k0 = f(xk_1) + (dfdx_est * (x_diff))
        xk_2 += xk_1
        eps_a = np.abs(dx/xk)
        eps_a_arr = np.append(eps_a_arr,eps_a)
        k += 1
    return xk, k, eps_a_arr
