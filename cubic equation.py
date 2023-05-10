import pyfiglet
import cmath

title = pyfiglet.figlet_format("x^3 + ax^2 + bx + c = 0", font = "digital")
print(title)

# print("We can solve the cubic equation in the form: x^3 + ax^2 + bx + c = 0") #Solving the equation in a standard way
# print()
# print("Enter the coefficients: ")

def cubic_equation(a,b,c):

    p = b - a**2/3
    q = (2*a**3/27) - (a*b/3) + c
    Δ = (q**2/4) + (p**3/27)

    if Δ > 0 :
        x = (((-q/2) + (Δ**0.5))**(1/3)) + (((-q/2) - (Δ**0.5))**(1/3)) - (a/3)
        print("The equation has three identical roots:")
        print(x)

    elif Δ == 0:
        x1 = -2*(q/2)**(1/3) - (a/3)
        x2 = x3 = (q/2)**(1/3) - (a/3)
        print("The equation has three roots. A double root and a single root:")
        print("Double root is:", x2, "and single root is :", x1)

    else:
        x1 = (2/3**0.5)*((-p)**0.5)*(cmath.sin((1/3)*(cmath.asin((3*(3**0.5)*q))/(2*((-p)**(3/2)))))) - (a/3)
        x2 = -(2/3**0.5)*((-p)**0.5)*(cmath.sin((1/3)*(cmath.asin((3*(3**0.5)*q))/(2*((-p)**(3/2)))) + cmath.pi/3)) - (a/3)
        x3 = (2/3**0.5)*((-p)**0.5)*(cmath.cos((1/3)*(cmath.asin((3*(3**0.5)*q))/(2*((-p)**(3/2)))) + cmath.pi/6)) - (a/3)
        print("The equation has three different roots:")
        print("First root is: ", x1)
        print("second root is: ", x2)
        print("and the third root is: ", x3)

cubic_equation(-4,5,-2)