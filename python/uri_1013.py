def greatest(a, b):
	return (a + b + abs(a - b)) // 2

user_in = input().split()

for i in range(len(user_in)):
	user_in[i] = float(user_in[i])

greatest_num = user_in[0]
for i in range(len(user_in) - 1):
	greatest_num = greatest(greatest_num, user_in[i+1])

print("%d eh o maior" %greatest_num)