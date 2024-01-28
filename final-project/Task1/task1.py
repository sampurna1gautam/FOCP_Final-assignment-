pizza_cost = 12
total_price = 0
possible_input_list = ['n', 'no', 'y', 'yes']


def delivery_charge_calculator(number_of_pizza):
    """Calculates delivery charge if needed."""

    if (number_of_pizza >= 5):
        return 0 # No delivery charge if 5 or more pizzas are ordered.
    else:
        return 2.5


def tuesday_discount_calculator(total_price, tuesday_discount):
    """Calculates if the Tuesday discount needs to be applied."""

    if tuesday_discount == 'y' or tuesday_discount == 'yes':
        return total_price * 0.5 # Apply 50% discount on Tuesdays.
    else:
        return total_price # No discount if not Tuesday.


def app_discount_calculator(total_price, used_app):
    """Checks if the user used the pizza app and calculate total accordingly."""

    if used_app == 'y' or used_app =='yes':
        return total_price * 0.75
    else:
        return total_price


def total_price_calculator(number_of_pizza, need_of_delivery, tuesday_discount, used_app):
    """Calculates total cost based on all variables."""

    total_price = number_of_pizza * pizza_cost
    total_price = tuesday_discount_calculator(total_price, tuesday_discount)

    

    if need_of_delivery == 'y' or need_of_delivery == 'yes':
        delivery_cost = delivery_charge_calculator(number_of_pizza)
        total_price += delivery_cost  # Add delivery charge if applicable.
    else:
        total_price

    total_price = app_discount_calculator(total_price, used_app)
    return round(total_price, 2)

# Main function to handle user input and display the total price.

def main():
    """Validates all the inputs, and calculates the total."""

    print("""
BPP Pizza Price Calculator
==========================
          """)
    number_of_pizza = int(input("How many pizzas ordered? "))

    while number_of_pizza <= 0 or type(number_of_pizza) is not int:
        print("Please enter a positive integer")
        number_of_pizza = int(input("How many pizzas ordered? "))
    else:
        number_of_pizza

    need_of_delivery = str(input("Is delivery required? ")).lower()

    while need_of_delivery not in possible_input_list:
        print("Invalid input, please enter either 'y, n, yes, or no'")
        need_of_delivery = str(input("Is delivery required? ")).lower()
    else:
        need_of_delivery

    tuesday_discount = str(input("Is it Tuesday? ")).lower()

    while tuesday_discount not in possible_input_list:
        print("Invalid input, please enter either 'y, n, yes, or no'")
        tuesday_discount = str(input("Is it Tuesday? ")).lower()

    used_app = str(input("Did the customer use the app? ")).lower()

    while used_app not in possible_input_list:
        print("Invalid input, please enter either 'y, n, yes, or no'")
        used_app = str(input("Did the customer use the app? ")).lower()

    total_price = total_price_calculator(
        number_of_pizza, need_of_delivery, tuesday_discount, used_app)
    print(f"The total price of your order is: £{total_price:.2f}")


if __name__ == '__main__':
    main()