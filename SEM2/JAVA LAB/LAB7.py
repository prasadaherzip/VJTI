import math

class QuadraticEquationSolver:

    def findRoot(self, a, b, c):
        print(f"\nSolving equation: {a}x² + {b}x + {c} = 0")

        d = b*b - 4*a*c

        if d > 0:
            r1 = (-b + math.sqrt(d)) / (2*a)
            r2 = (-b - math.sqrt(d)) / (2*a)
            print("Two real roots:", r1, "and", r2)

        elif d == 0:
            r = -b / (2*a)
            print("One real root:", r)

        else:
            real = -b / (2*a)
            imag = math.sqrt(-d) / (2*a)
            print("Complex roots:", real, "+", imag, "i and", real, "-", imag, "i")


solver = QuadraticEquationSolver()

# Example equations
solver.findRoot(1, -5, 6)   # x² - 5x + 6 = 0
solver.findRoot(1, 2, 1)    # x² + 2x + 1 = 0
solver.findRoot(1, 4, 8)    # x² + 4x + 8 = 0
