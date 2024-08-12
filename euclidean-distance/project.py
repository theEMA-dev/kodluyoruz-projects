import math, sys, time
print("\033[32m"+time.ctime())
print(sys.version)
print("Euclidean Distance Calculator by theEMA-dev")
print("\033[37mEnter (x, y) coordinates of point1: 1,2")
print("Enter (x, y) coordinates of point2: 4,6")
points = [(1, 2), (4, 6)] # 3 4 5 Euclidean Distance

def euclideanDistance(point1, point2):
  return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

distances = []
for i in range(len(points)):
  for j in range(i + 1, len(points)):
    distance = euclideanDistance(points[i], points[j])
    distances.append(distance)

min_distance = min(distances)
print(f"Minimum distance: {min_distance}")