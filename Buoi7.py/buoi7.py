# ex1:
# def area_of_circle(radious):
#     import math
#     area_of_circle = math.pi * (radious)**2
#     return area_of_circle

# def perimeter_of_circle(radious):
#     import math
#     perimeter_of_circle = 2 * radious * math.pi
#     return perimeter_of_circle

# def area_of_rectangle( w, h):
#     area_of_rectangle = w * h
#     return area_of_rectangle

# def perimeter_of_rectangle(w,h):
#     perimeter_of_rectangle= ( w + h) * 2
#     return perimeter_of_rectangle

# def volumn_of_sphere(radious):
#     import math
#     volumn_of_sphere = (4 / 3) * math.pi * (radious**3)
#     return volumn_of_sphere

# def volumn_of_rectangular_prism(w,l,h):
#     volumn_of_rectangular_prism= w * l * h
#     return volumn_of_rectangular_prism

# command = input("What do you want to calculate (volumn, perimeter, area)?: ")
# while command.lower() == "volumn" or "perimeter" or "area" or "quit":
#     if command.lower() == "volumn":
#         print("If you want to exit: type Quit")
#         shape = input("Which shape do you want to calculate? ( sphere, rectangular prism ): ")
#         if shape.lower() == "sphere":
#             radious = int(input("Enter the radious: "))
#             volumnofsphere = volumn_of_sphere(radious)
#             print(volumnofsphere)
#         elif shape.lower() == "rectangular prism":
#             w = int(input("Enter the width: "))
#             l = int(input("Enter the length: "))
#             h = int(input("Enter the height: "))
#             volumnofrectangularprism = volumn_of_rectangular_prism(w,l,h)
#             print(volumnofrectangularprism)
#         elif shape.lower()== "quit":
#             break
#     elif command.lower() == "perimeter":
#         print("If you want to exit: type Quit")
#         shape = input("Which shape do you want to calculate? ( circle, rectangle ): ")
#         if shape.lower() == "circle":
#             radious = int(input("Enter the radious: "))
#             perimeterofcircle = perimeter_of_circle(radious)
#             print(perimeterofcircle)
#         elif shape.lower() == "rectangle":
#             l = int(input("Enter the length: "))
#             w = int(input("Enter the width: "))
#             perimeterofrectangle = perimeter_of_rectangle(w,h)
#             print(perimeterofrectangle)
#         elif shape.lower()== "quit":
#             break
#     elif command.lower() == "area":
#         print("If you want to exit: type Quit")
#         shape = input("Which shape do you want to calculate? ( rectangle, circle ): ")
#         if shape.lower() == "circle":
#             radious = int(input("Enter the radious: "))
#             areaofcircle = area_of_circle(radious)
#             print(areaofcircle)
#         if shape.lower() == "rectangle":
#             w = int(input("Enter the width: "))
#             l = int(input("Enter the length: "))
#             areaofrectangle = area_of_rectangle( w, h)
#             print(areaofrectangle)
#         elif shape.lower()== "quit":
#             break
#     else:
#         print("Error")

# ex2:
def print_board(board):
    # Input: A board configuration
    # Output: Return None, print the board in human readable form
    for row in range(8):
        print(row + 1, end=' ')
        for col in range(8):
            if board[row][col] == 0:
                print('|  ', end=' ')
            elif board[row][col] == 1:
                print('| B', end=' ')
            elif board[row][col] == 2:
                print('| W', end=' ')
        print('|', '\n', '-----------------------------------')
    print('  | a | b | c | d | e | f | g | h |')


def new_board():
    new_board =
    [[0,0,0],
    [0,0,0],
    [0,0,0]]
    return new_board

def print_board(board):
    for row in range(0,4):
        print(row, end=" ")
        for col in range(4):
            if board[row][col] == 0:
                print("|  ", end = " ")
            elif board[row][col] == 1:
                print("| X", end=" ")
            elif board[row][col] == 2:
                print("| O", end=" ")
    print('|', '\n', '-----------------------------')
    print('  | a | b | c | d |')

def move(player, row, col):
    if player == 1:
        
