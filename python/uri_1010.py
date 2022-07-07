total = 0

for i in range(2):
	code, units, price = input().split()
	total += int(units) * float(price)

print("VALOR A PAGAR: R$ %.2f" %total)
