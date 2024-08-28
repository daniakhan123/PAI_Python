def area_of_trapezoid(base1, base2, height):
    
    area = 0.5 * (base1 + base2) * height
    return area

def area_of_parallelogram(base, height):
    
    area = base * height
    return area

def volume_and_surface_area_of_cylinder(radius, height):
    pi = 3.142 
    volume = pi * radius**2 * height
    surface_area = 2 * pi * radius * (radius + height)
    return volume, surface_area

print("Area of trapezoid:", area_of_trapezoid(5, 7, 10))  
print("Area of parallelogram:", area_of_parallelogram(6, 8)) 
volume, surface_area = volume_and_surface_area_of_cylinder(3, 9) 
print("Volume of cylinder:", volume)
print("Surface area of cylinder:", surface_area)

