# Function to calculate equivalent moving average based on timeframe
def calculate_moving_average(timeframe, market_type="forex", num_days=5):
    if market_type == "stock":
        minutes_per_day = 390  # Stock market hours: 6.5 hours per day (390 minutes)
    elif market_type == "crypto":
        minutes_per_day = 24 * 60  # Crypto market: 24 hours per day, 7 days a week (1440 minutes)
        num_days = 7  # Crypto market operates continuously 7 days a week
    else:
        minutes_per_day = 24 * 60  # Forex market: 24 hours per day (1440 minutes)
    
    total_minutes = minutes_per_day * num_days  # Total minutes in the given number of days
    equivalent_ma = total_minutes / timeframe
    return equivalent_ma

# Function to get user input for market type and timeframe
def get_user_input():
    # Ask user if they are trading regular stock hours, Forex, or crypto
    market_type = input("Are you trading 'stock' (regular market hours), 'forex' (24-hour market), or 'crypto' (24/7 market)? ").lower()

    while market_type not in ["stock", "forex", "crypto"]:
        print("Invalid input. Please enter 'stock', 'forex', or 'crypto'.")
        market_type = input("Are you trading 'stock' (regular market hours), 'forex' (24-hour market), or 'crypto' (24/7 market)? ").lower()

    # Ask the user for their desired timeframe
    try:
        timeframe = int(input("Please enter the timeframe in minutes (e.g., 240 for 4-hour chart): "))
        if timeframe <= 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return get_user_input()  # Recursive call for re-input

    return market_type, timeframe

def main():
    while True:
        # Get user input
        market_type, timeframe = get_user_input()

        # Calculate equivalent moving average
        five_day_ma = calculate_moving_average(timeframe, market_type)

        # Display the result
        if market_type == "crypto":
            print(f"\nEquivalent 7-day Simple Moving Average for a {timeframe}-minute timeframe in the {market_type.upper()} market: {five_day_ma:.2f} periods")
        else:
            print(f"\nEquivalent 5-day Simple Moving Average for a {timeframe}-minute timeframe in the {market_type.upper()} market: {five_day_ma:.2f} periods")

        # Ask if the user wants to calculate again
        again = input("\nDo you want to calculate for another timeframe? (yes/no): ").lower()
        if again != "yes":
            print("Thank you for using the moving average calculator! Goodbye.")
            break

# Run the program
if __name__ == "__main__":
    main()
