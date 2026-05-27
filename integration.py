"""
============================================================
  Symbolic Integration Calculator
  Author : Hanif Olayiwola
  Course : Mathematical Foundations of Computing
  Date   : May 2026
  Topic  : Integration (Antiderivatives & Definite Integrals)
============================================================

MATHEMATICS BACKGROUND:
  Integration is the reverse process of differentiation.
  Given a function f(x), the indefinite integral is:
      ∫ f(x) dx = F(x) + C
  where F'(x) = f(x) and C is the constant of integration.

  For a definite integral over [a, b]:
      ∫[a to b] f(x) dx = F(b) - F(a)     (Fundamental Theorem of Calculus)
"""

import sympy as sp  # SymPy is used for exact symbolic computation


def display_banner():
    """Print a welcome banner to the console."""
    print("=" * 55)
    print("       SYMBOLIC INTEGRATION CALCULATOR")
    print("=" * 55)
    print("Supported operators:  + - * / ** (power)")
    print("Supported functions:  sin, cos, tan, exp, log, sqrt")
    print("Variable: x")
    print("-" * 55)


def get_function_from_user():
    """
    Prompt the user to enter a mathematical function.
    Returns a SymPy expression if valid, or None on error.
    """
    raw = input("\nEnter a function of x  (e.g. x**2 + 3*x - 5): ").strip()

    # Define x as a symbolic variable so SymPy can work with it
    x = sp.Symbol('x')

    try:
        # sympify converts the user's string into a SymPy expression
        func = sp.sympify(raw)
        return func, x
    except sp.SympifyError:
        print("  ✗ Could not parse that expression. Please check your syntax.")
        return None, None


def compute_indefinite_integral(func, x):
    """
    Compute the indefinite integral ∫ f(x) dx.
    SymPy's integrate() returns the antiderivative without the + C,
    so we append it manually for mathematical correctness.
    """
    antiderivative = sp.integrate(func, x)
    return antiderivative


def compute_definite_integral(func, x, a, b):
    """
    Evaluate the definite integral ∫[a to b] f(x) dx.
    Uses the Fundamental Theorem of Calculus via SymPy.
    Returns both the exact symbolic result and a decimal approximation.
    """
    exact_result = sp.integrate(func, (x, a, b))

    # evalf() converts the symbolic result to a floating-point number
    decimal_result = exact_result.evalf()
    return exact_result, decimal_result


def display_results(func, x, antiderivative):
    """
    Neatly print the original function and its antiderivative.
    """
    print("\n" + "-" * 55)
    print("  INDEFINITE INTEGRAL RESULT")
    print("-" * 55)
    print(f"  f(x)         =  {func}")
    print(f"  ∫ f(x) dx    =  {antiderivative}  + C")
    print("-" * 55)


def ask_for_definite():
    """Ask the user whether they want to evaluate a definite integral."""
    choice = input("\nWould you like to evaluate a definite integral? (yes / no): ").strip().lower()
    return choice in ("yes", "y")


def get_limits():
    """
    Prompt for the lower bound (a) and upper bound (b).
    Accepts integers, decimals, or symbolic values like 'pi'.
    """
    print("Enter the limits of integration.")
    a_raw = input("  Lower limit a: ").strip()
    b_raw = input("  Upper limit b: ").strip()

    try:
        # sympify allows the user to type 'pi', 'E', etc.
        a = sp.sympify(a_raw)
        b = sp.sympify(b_raw)
        return a, b
    except sp.SympifyError:
        print("  ✗ Invalid limits. Please enter numbers or constants like pi.")
        return None, None


def main():
    """
    Main program loop.
    1. Show banner
    2. Get function from user
    3. Compute and display indefinite integral
    4. Optionally compute and display definite integral
    5. Ask if user wants to calculate again
    """
    display_banner()

    while True:
        # --- Step 1: Get the function ---
        func, x = get_function_from_user()
        if func is None:
            # Parsing failed; let the user try again
            continue

        # --- Step 2: Indefinite integral ---
        antiderivative = compute_indefinite_integral(func, x)
        display_results(func, x, antiderivative)

        # --- Step 3: Optional definite integral ---
        if ask_for_definite():
            a, b = get_limits()

            if a is not None and b is not None:
                exact, decimal = compute_definite_integral(func, x, a, b)

                print("\n" + "-" * 55)
                print("  DEFINITE INTEGRAL RESULT")
                print("-" * 55)
                print(f"  ∫[{a} to {b}] {func} dx")
                print(f"  Exact value   =  {exact}")
                print(f"  Decimal value ≈  {decimal:.6f}")
                print("-" * 55)

        # --- Step 4: Repeat or exit ---
        again = input("\nCalculate another integral? (yes / no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nThank you for using the Symbolic Integration Calculator. Goodbye!")
            break

        print()  # blank line before the next round


# Entry point
if __name__ == "__main__":
    main()
