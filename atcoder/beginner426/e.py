import math

def uclid(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


t = int(input())
for _ in range(t):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

