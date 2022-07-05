user_in = input().split()

for i in range(len(user_in)):
	user_in[i] = float(user_in[i])

triangle = user_in[0] * user_in[2] / 2
circle = 3.14159 * user_in[2] ** 2
trap = (user_in[0] + user_in[1]) / 2 * user_in[2]
square = user_in[1] * user_in[1]
rectangle = user_in[0] * user_in[1]

print("TRIANGULO: %.3f" %triangle)
print("CIRCULO: %.3f" %circle)
print("TRAPEZIO: %.3f" %trap)
print("QUADRADO: %.3f" %square)
print("RETANGULO: %.3f" %rectangle)