my_income = float(input("What was your income?\r\n"))

tax_rate = 0.1

my_taxes = my_income * tax_rate

my_take_home = my_income - my_taxes
print(f"Initial income: ${my_income:.2f}")
print(f"Total Taxes taken out: ${my_taxes:.2f}")
print(f"Take home pay: ${my_take_home:.2f}")

