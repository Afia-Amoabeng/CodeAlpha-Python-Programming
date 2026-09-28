print("STOCK TRACKER")
print("Enter your holdings to see total investment. Enter Check when done ")
#Predefined stock prices
prices = {"AAPL": 190, "TSLA": 260, "GOOG": 340, "AMZN": 230, "MSFT": 490}
holdings = []
total = 0

#Loop to take user's stock info
while True:
    stock = input("Input company stock symbol: ")
    if stock.lower() == "check":
        break

    #Warning for stocks not predefined  
    if stock not in prices:
        print("Not Applicable. Try another symbol")
        continue
    quant = int(input("Input quantity owned: "))
    
    #User investment calculation and storage
    subtotal = prices[stock] * quant
    holdings.append((stock,quant,subtotal))
    total += subtotal

#Display investments
for stock, quant, subtotal in holdings:
    print(f"{stock}: {quant} shares = ${subtotal}")

print(f"Total investment is ${total}")


#Write to txt
with open("holdings.txt", "w") as f:
    f.write("STOCK TRACKER REPORT\n")
    for stock, quant, subtotal in holdings:
        f.write(f"{stock}: {quant} shares = ${subtotal}\n")
    f.write(f"TOTAL: ${total}\n")

print("Saved to holdings.txt")