# Constants
SERVICE_CHARGE = 2
TICKET_PRICE = 10

# Variable
tickets_remaining = 100

# Price calculation function


def calculate_price(number_of_tickets):
    # Create a new constant for the $2 service charge
    # Add the service charge to our result
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE


# Run this code continuously until we run out of tickets.
while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    customer_name = input("Please enter your name: ")
    number_of_tickets = input(
        "Hello {}, how many tickets are you purchasing: ".format(customer_name))
    # Expect ValueError to occur and handle appropriately
    try:
        number_of_tickets = int(number_of_tickets)
        # Raise a ValueError if the request are for more tickets than what is available
        if number_of_tickets > tickets_remaining:
            raise ValueError(
                "There are only {} tickets remaining.".format(tickets_remaining))
    except ValueError as err:
        print("Oh no!, {} Please try again.".format(err))
    else:
        order_amount = calculate_price(number_of_tickets)
        print("Total cost is ${}".format(order_amount))
        should_proceed = input("Do you want to proceed, Y/N ")
        if should_proceed.lower() == "y":
            # TODO: Gather credit card detail and process order
            print("SOLD!")
            # Reduce the tickets remaining by the number of tickets purchased.
            tickets_remaining -= number_of_tickets
        else:
            print("Thank you {} for visiting our site.".format(customer_name))
# Notify the customer that tickets are sold out.
print("Oh sorry, tickets are now sold out.")
