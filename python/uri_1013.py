def greatest(a, b):
	return (a + b + abs(a - b)) // 2

values = input().split()

for i in range(len(values)):
	values[i] = float(values[i])

greatest_num = values[0]
for i in range(len(values) - 1):
	greatest_num = greatest(greatest_num, values[i+1])

print("%d eh o maior" %greatest_num)