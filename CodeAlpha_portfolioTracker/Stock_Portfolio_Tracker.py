stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

total_value = 0
portfolio = {}

print(" Stock Portfolio Tracker")

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    if stock == "DONE":
        break

    if stock in stock_prices:
        qty = int(input("Enter quantity: "))
        value = stock_prices[stock] * qty
        portfolio[stock] = value
        total_value += value
    else:
        print(" Stock not available")

print("\nYour Portfolio:")
for stock, value in portfolio.items():
    print(stock, value)

print("Total Investment: ", total_value)

# Save to file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio\n")
    for stock, value in portfolio.items():
        file.write(f"{stock}: {value}\n")
    file.write(f"Total Investment: {total_value}")

print("\nPortfolio saved to portfolio.txt")
