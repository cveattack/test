import sympy as sp

def find_derivative(expr_str, var_str):
    x = sp.symbols(var_str)
    expr = sp.sympify(expr_str)
    der = sp.diff(expr, x)

    return der

def main():
    expr_str = input("Введите выражение: ").strip().lower()
    var_str = input("Введите переменную: ").strip().lower()

    try:
        print(f"Производная выражения {expr_str} по переменной {var_str} равна: \n{find_derivative(expr_str, var_str)}")

        
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
