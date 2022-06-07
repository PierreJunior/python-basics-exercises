# 6.5 - Challenge: Track Your Investments
# Solution to challenge
from decimal import Decimal

#Calculate interest to track the growth of an investment

def Invest(amount, rate, years):
    for years in range(1, years+1):
        interest = amount * rate
        investment = amount + interest
        amount = investment        
        print(f"year {years} : ${investment:,.2f}")

amount = float(input("Please enter an amount"))

rate = float(input("Please enter an interest rate").replace('%',''))

#get the decimal number of the percentage
rate = Decimal(rate /100)
#round it to two decimal places
rate = float(round(rate,2))

years = int(input("Please enter the years you would like to"))

Invest(amount, rate, years)
