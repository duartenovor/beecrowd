prod = [ [],[] ]
total = 0

for i in range(2):
	prod[i] = input().split()
	total += (int(prod[i][1]) * float(prod[i][2]))

print("VALOR A PAGAR: R$ %.2f" %total)
