import math, sys, time
print("\033[32m"+time.ctime())
print(sys.version)

points = [(1, 2), (4, 2), (4, 6)]

print("\033[36mEuclidean Distance Calculator by theEMA-dev")
print("Running Python code in PyScript 2024.8.2")
print("\033[37mCoordinates:", points)

def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

distance_1_2 = euclideanDistance(points[0], points[1])
distance_1_3 = euclideanDistance(points[0], points[2])
distance_2_3 = euclideanDistance(points[1], points[2])

print(f"Distance between point 1 and point 2: {distance_1_2}")
print(f"Distance between point 1 and point 3: {distance_1_3}")
print(f"Distance between point 2 and point 3: {distance_2_3}")