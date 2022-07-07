import math

points = []

def dist_betw_points(a, b):
	return math.sqrt ( ((b['x'] - a['x']) ** 2) + ((b['y'] - a['y']) ** 2) )

for i in range(2):
	new_x, new_y = input().split()
	new_point = {'x': float(new_x), 'y': float(new_y)}
	points.append(new_point)

distance = dist_betw_points(points[0], points[1])

print("%.4f" %distance)