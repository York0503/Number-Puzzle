import numpy as np
from board_praticeTest import Board


# init
def case1():
    print("---------case1-------------\n")
    b = Board()
    b.show()
    print("\n")

# finish checking
def case2():
    print("---------case2-------------\n")
    b = Board()
    print(b.finish())
    print("\n")

# randomize
def case3():
    print("---------case3-------------\n")
    b = Board()
    b.premu()
    b.show()
    print("blank in : ",b.blank)
    print(b.finish())
    print("\n")

# swap 2 piece
def case4():
    print("---------case4-------------\n")
    b = Board()
    b.swap(1, 2)
    b.show()
    print(b.finish())
    print("\n")

# do a move
def case5():
    print("---------case5-------------\n")
    b = Board()
    print("Move up : ")
    b.move("w")
    b.show()
    print("Move down : ")
    b.move("s")
    b.show()
    print("Move left : ")
    b.move("a")
    b.show()
    print("Move right : ")
    b.move("d")
    b.show()
    print(b.finish())
    print("\n")

# sequencial playing
def case6():
    print("---------case6-------------\n")
    b = Board()
    b.play()

#     main test
case6()