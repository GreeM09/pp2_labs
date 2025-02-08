def Volume(r):
    return 4/3 * 3.14159 * r**3

result = Volume(float(input("Enter the radius of the sphere: ")))
print(f"The volume of the sphere is {result:.2f}")
