#Method 1 — Calculate directly

principal = float(input("Enter the Principal Amount: "))
rate = float(input("Enter the Annual interest rate in percent: "))
time = int(input("Enter the Time in years: "))


simple_interest = (principal * rate * time) /100

print(f"Simple Interest: {simple_interest:.2f}")


#Method 2 — Separate the calculation into steps

principal = float(input("Enter principal: "))
rate = float(input("Enter annual interest rate (%): "))
time = int(input("Enter time in years: "))

product = principal * rate * time
simple_interest = product / 100

print(f"Simple Interest: {simple_interest:.2f}")
