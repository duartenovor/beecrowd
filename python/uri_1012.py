points = {}

a, b, c = input().split()
points = {'a': float(a), 'b': float(b), 'c': float(c)}

triangle = points['a'] * points['c'] / 2
circle = 3.14159 * points['c'] ** 2
trap = (points['a'] + points['b']) / 2 * points['c']
square = points['b'] * points['b']
rectangle = points['a'] * points['b']

print("TRIANGULO: %.3f" % triangle)
print("CIRCULO: %.3f" % circle)
print("TRAPEZIO: %.3f" % trap)
print("QUADRADO: %.3f" % square)
print("RETANGULO: %.3f" % rectangle)
