def expression_calculator():
    print("Welcome to Expression Calculator!")
    print("Type 'exit' to quit.")

    while True:
        expr = input("Enter a math expression (e.g., 5 + 3 * 2): ")
        if expr.lower() == 'exit':
            print("Goodbye!")
            break
        try:
            result = eval(expr)
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except Exception as e:
            print(f"Invalid expression! {e}")

# Run the calculator
expression_calculator()
