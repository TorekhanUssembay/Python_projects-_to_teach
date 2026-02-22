import math

def get_point(label):
    while True:
        try:
            x = float(input(f"Enter x for {label}: "))
            y = float(input(f"Enter y for {label}: "))
            return (x, y)
        except ValueError:
            print("Please inser valid numeric values.")
def calculate_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def main():
    print("Point 1: ")
    point1 = get_point("Point 1")

    print("Point 2: ")
    point2 = get_point("Point 2")

    distance = calculate_distance(point1, point2)

    print(f"\nDistance between points: {distance:.2f}")

if __name__ == "__main__":
    main()