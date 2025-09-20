# Hardcoded dictionary of stock prices (per share)
stock_prices = {
    "AAPL": 180,   # Apple
    "TSLA": 250,   # Tesla
    "AMZN": 140,   # Amazon
    "MSFT": 330,   # Microsoft
    "GOOGL": 125   # Alphabet
}

portfolio = {}  # To store user’s stock and quantity
total_value = 0

print("📊 Stock Portfolio Tracker")
print("Available stocks and prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break
    elif stock not in stock_prices:
        print("⚠️ Invalid stock symbol. Try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("⚠️ Please enter a valid number.")
        continue

    # Add to portfolio
    portfolio[stock] = portfolio.get(stock, 0) + quantity
    total_value += stock_prices[stock] * quantity

print("\n📌 Your Portfolio:")
for stock, qty in portfolio.items():
    print(f"{stock} → {qty} shares @ ${stock_prices[stock]} each = ${stock_prices[stock] * qty}")

print(f"\n💰 Total Investment Value: ${total_value}")

# Optional: Save to file
save_choice = input("\nDo you want to save this to a file? (yes/no): ").lower()

if save_choice == "yes":
    with open("portfolio.txt", "w") as f:
        f.write("📊 Stock Portfolio\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock} → {qty} shares @ ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
        f.write(f"\n💰 Total Investment Value: ${total_value}\n")
    print("✅ Portfolio saved to portfolio.txt")