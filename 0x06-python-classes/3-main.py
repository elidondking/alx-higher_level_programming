quare = __import__('3-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
        print(my_square_1.size)
except Exception as e:
        print(e)

        try:
                print(my_square_1.__size)
        except Exception as e:
                print(e)

