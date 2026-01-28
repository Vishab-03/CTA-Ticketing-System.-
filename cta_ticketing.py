# CTA Ticketing System
# Author: Vishab Vijayb Bagde
# Description: Calculates ticket fare based on starting and destination zones

BASE_FARE = 2.50
ZONE_RATE = 1.50
MIN_ZONE = 1
MAX_ZONE = 5

def calculate_fare(start_zone, end_zone):
    """
    Calculates the fare based on the difference between start and end zones.
    """
    zone_difference = abs(end_zone - start_zone)
    return BASE_FARE + (zone_difference * ZONE_RATE)

def get_zone_input(prompt):
    """
    Gets validated zone input from the user.
    Ensures input is an integer and within the allowed zone range.
    """
    while True:
        try:
            zone = int(input(prompt))
            if MIN_ZONE <= zone <= MAX_ZONE:
                return zone
            else:
                print(f"Zone must be between {MIN_ZONE} and {MAX_ZONE}. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def main():
    """
    Main program function.
    Handles user interaction, fare calculation, and repeat option.
    """
    print("="*40)
    print(" Welcome to the CTA Ticketing System ")
    print("="*40)

    while True:
        start_zone = get_zone_input("Enter starting zone (1-5): ")
        end_zone = get_zone_input("Enter destination zone (1-5): ")

        fare = calculate_fare(start_zone, end_zone)

        if start_zone == end_zone:
            print("You are travelling within the same zone.")

        print(f"Your ticket fare is: £{fare:.2f}")

        again = input("Would you like to calculate another fare? (y/n): ").lower()
        if again != "y":
            print("Thank you for using the CTA Ticketing System.")
            break

if __name__ == "__main__":
    main()
