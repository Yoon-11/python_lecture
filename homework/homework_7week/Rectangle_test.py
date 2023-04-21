from Rectangle import Rectangle

Rectangle_test1 = Rectangle(4, 40)
Rectangle_test2 = Rectangle(3.5, 35.7)


Rectangle_test1_area = Rectangle_test1.getArea()
Rectangle_test2_area = Rectangle_test2.getArea()

Rectangle_test1_perimeter = Rectangle_test1.getPerimeter()
Rectangle_test2_perimeter = Rectangle_test2.getPerimeter()

print(f"Rectangle_test1의 width={Rectangle_test1.width} height={Rectangle_test1.height} area={Rectangle_test1_area} perimeter={Rectangle_test1_perimeter} \n"
      f"Rectangle_test2의 width={Rectangle_test2.width} height={Rectangle_test2.height} area={round(Rectangle_test2_area)} perimeter={Rectangle_test2_perimeter}")






