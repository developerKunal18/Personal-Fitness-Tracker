from datetime import datetime


def get_valid_date(prompt):
    while True:
        value = input(prompt).strip()

        try:
            parsed = datetime.strptime(value, "%Y-%m-%d")
            return parsed.strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD format.")


def get_valid_number(prompt, minimum=0):
    while True:
        try:
            value = float(input(prompt))

            if value < minimum:
                print(f"Value must be at least {minimum}.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")


def get_valid_id(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value > 0:
                return value

            print("ID must be greater than zero.")

        except ValueError:
            print("Please enter a valid numeric ID.")


def format_number(value):
    return f"{value:g}"
