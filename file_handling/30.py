# calculate_area() , accept --> base and height from main() and returns area of triangle to main()
def calculate_area(base,height):
    area=(1/2)*base*height 
    return area 
def main():
     b = int(input("Enter base of the triangle: "))
     h = int(input("Enter height of the triangle: "))

     result = calculate_area(b, h)
     print("Area of the triangle =", result)

main()
