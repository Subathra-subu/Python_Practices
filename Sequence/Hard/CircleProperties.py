radius = float(input("Enter the radius of the circle:"))
angle = int(input("Enter the specific angle:"))
pi=3.14159
circumference = 2*radius*pi
diameter = 2*radius
area = radius*radius*pi

sector_area = (angle/360)*area
arc_length = (angle/360)*circumference

print("Diameter:",diameter)
print(area)
print(circumference)
print(f"Sector area for {angle} degrees:",sector_area)
print(f"Arc length for {angle} degrees:",arc_length)

