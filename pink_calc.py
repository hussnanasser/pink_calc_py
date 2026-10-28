
# ==========================================
#       💗 PINK MATH CALCULATOR 💗
# ==========================================

import math

# Terminal colours (ANSI escape codes)
PINK = "\033[95m"
LIGHT_PINK = "\033[38;5;218m"
PURPLE = "\033[94m"
WHITE = "\033[97m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

history = []

def display_header():
    print(PINK + BOLD)
    print("=" * 42)
    print("       💗 MATH PINK PYTHON CALCULATOR 💗")
    print("=" * 42 + RESET)
    print(LIGHT_PINK + "Calculate away! ✨" + RESET)


def get_number(prompt):
    while True:
        try:
            return float(input(LIGHT_PINK + prompt + RESET))
        except ValueError:
            print(RED + "Please enter a valid number!" + RESET)


def calculate(num1, op, num2=None):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            raise ZeroDivisionError
        return num1 / num2
    elif op == "**":
        return num1 ** num2
    elif op == "%":
        if num2 == 0:
            raise ZeroDivisionError
        return num1 % num2
    elif op == "//":
        if num2 == 0:
            raise ZeroDivisionError
        return num1 // num2
    elif op == "sqrt":
        if num1 < 0:
            raise ValueError("Cannot calculate the square root of a negative number.")
        return math.sqrt(num1)
    else:
        raise ValueError("Invalid operator!")


def show_history():
    print(PURPLE + "\n--- 💗 CALCULATION HISTORY 💗 ---" + RESET)

    if not history:
        print("No calculations yet!")
    else:
        for index, item in enumerate(history, start=1):
            print(f"{index}. {item}")

    print()


def main():
    display_header()

    operators = ["+", "-", "*", "/", "**", "%", "//", "sqrt"]

    while True:
        print(LIGHT_PINK + "Choose from the following operations:" + RESET)
        print(" +  Addition")
        print(" -  Subtraction")
        print(" *  Multiplication")
        print(" /  Division")
        print(" ** Powers")
        print(" %  Remainder")
        print(" // Floor division sqrt Square root")
        print("Type 'History' to view previous calculations.")
        print("Type 'Exit' to quit.")

        choice = input(LIGHT_PINK + "\nEnter your chosen operation here: " + RESET).strip().lower()

        if choice == "exit":
            break

        if choice == "history":
            show_history()
            continue

        if choice not in operators:
            print(RED + "Invalid operator. Please try again!" + RESET)
            continue

        num1 = get_number("Enter the first number: ")

        if choice == "sqrt":
            num2 = None
        else:
            num2 = get_number("Enter the second number: ")

        try:
            result = calculate(num1, choice, num2)

            # Reject results such as infinity or NaN
            if not math.isfinite(result):
                print(RED + "Result is outside the supported range!" + RESET)
                continue

            if choice == "sqrt":
                expression = f"sqrt({num1:g})"
            else:
                expression = f"{num1:g} {choice} {num2:g}"

            record = f"{expression} = {result:g}"
            history.append(record)

            print(LIGHT_PINK + BOLD + "\n✨ RESULT ✨" + RESET)
            print(LIGHT_PINK + f"{expression} = {result:g}" + RESET)

        except ZeroDivisionError:
            print(RED + "Cannot divide by zero!" + RESET)
        except (ValueError, OverflowError):
            print(RED + "Invalid calculation or result out of range!" + RESET)

    print(PINK + BOLD + "\nThank you for using my calculator! " + RESET)
    print(LIGHT_PINK + "Keep learning 💗✨" + RESET)


if __name__ == "__main__":
    main()