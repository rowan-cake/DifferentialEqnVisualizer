import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy import Function, dsolve, Derivative, checkodesol
from sympy.abc import t


def equationOfMotion(mass,damping,stiffness,x_atZero,xPrim_atZero):
    """
    # Effects: 
    ==============
    - Takes coeffiecents and intial coniditions of a second order homogenous ODE equation and returns its solution ploted values in a 
    numpy array. 
    
    # Paremeters: 
    ==============
    - mass(float): the mass of the spring?
    - damping(float): the friction on the system
    - stiffness(float): the stiffness of the spring
    - x_atZero(float): one intial condition (a x(t) value for t=0)
    - xPrim_atZero(float): another intial condition (a x'(t) value for t=0)

    # Returns:
    ============== 
    - equationOfMotion(Equation(SciPY)): returns a equation type from scipy?
    """
    x = Function('x')
    # Solve the ODE
    equationOfMotion = dsolve(mass*Derivative(x(t), t, 2) 
                    + damping*Derivative(x(t), t) 
                    +stiffness*x(t)
                    , x(t)
                    ,ics={x(0): x_atZero, x(t).diff(t).subs(t,0): xPrim_atZero})
    # RHS of the solved ODE
    rightHandSide = equationOfMotion.rhs
    # Now we have a function that can take inputs and turn them to proper outputs based on the RHS of the solved ODE
    numerical_function = sp.lambdify(t, rightHandSide, 'numpy')
    # Input points to the solved ODE (start,end,howManyPointsInBetween)
    t_vals = np.linspace(0, 10, 200)
    # Take inputs and turn them to outputs
    x_vals = numerical_function(t_vals)
    # print them just to see
    """for num in x_vals:
        print(num)"""
    naturalFrequency = np.sqrt((stiffness/mass)-(damping**2/(2*mass**2)))
    # return the x_vals the t_vals and the symbolic RHS (done for ploting purposes) in a tuple
    return x_vals,t_vals,rightHandSide,naturalFrequency

if __name__ == "__main__":
    eq = equationOfMotion(1,0,2,0,6)
    #rhs = eq.rhs
    #numerical_function = sp.lambdify(t, rhs, 'numpy')
    

    # Define the range of t values , 400 points between 0-100 (with some numerical errors)
    #t_vals = np.linspace(0, 100, 400)
    # Evaluate the numerical function this outputs a list of x points for every time value
    #x_vals = numerical_function(t_vals)

    print(eq[3])
    # Create the plot
    plt.figure(figsize=(8, 8))
    stringRHS = str(eq[2])
    plt.plot(eq[1], eq[0], label=r'$x(t) = '+stringRHS+'$')
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.title('Plot of the function $x(t) = ' + stringRHS + '$')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()

