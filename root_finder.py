import numpy as np


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
    k=0
    eps_a_arr = []

    while eps_a > eps_s:
        dx = -f(xk) / dfdx(xk)
        xk += dx
    
    eps_a[k] = np.abs(dx/xk)
    return xk, k, eps_a_arr





def root_secant_modified(x0, dx, f):
    """Finds a root of a function using the Modified Secant Method
    
    Parameters
    ----------
    x0: float
        Initial guess of root location

    f: float
        function

    dx: float
        step size for derivative estimations 
   
    Returns
    -------
    root_value: float
        final estimate of the root
    
    n_iterations: int
        number of iterations to convergence
    
    eps_a: np.ndarray
        one-dimensional vector of the approximate relative error at each iteration 
    """