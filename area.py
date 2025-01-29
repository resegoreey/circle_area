#User provides the radius of the circle
radius = int(input("Provide the radius of the circle: "))

#stores the value of pi
PI = 3.14

#calculates the area using the formula Area = π * radius^2
area = PI * (radius ** 2)
print(f"""The radius of your circle is {radius}
The calculated area of your circle is {area}""")