import math

points = [ [],[] ]

def dist_betw_points(a, b):
	x1, y1 = a
	x2, y2 = b

	return math.sqrt ( ((x2 - x1) ** 2) + ((y2 - y1) ** 2) )


for i in range(2):
	points[i] = input().split()

for i in range(2):
	for j in range(2):
		points[i][j] = float(points[i][j])


distance = dist_betw_points(points[0], points[1])

print("%.4f" %distance)