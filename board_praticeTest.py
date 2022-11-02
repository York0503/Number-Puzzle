from calendar import c
import numpy as np

class Board:
    a = [[0, 0, 0, 0]for i in range(4)]
    blank = 0
    n = 0

    def __init__(self):
        # set initial board and find blank location
        # goal : 
        # a:  0  1  2  3
        #  0| 1  2  3  4
        #  1| 5  6  7  8
        #  2| 9 10 11 12
        #  3|13 14 15  0
        # 
        # a[0][1] = 2 , a[0][2] = 3 , a[1][2] = 7
        # 
        # blank:
        #     15
        
        for r in range(4):
            for c in range(4):
                self.a[r][c] = (4*r + c+1)
        self.n = 0
        self.a[3][3] = 0
        self.blank = 15

        

    def show(self):
        for r in range(4):
            for c in range(4):
                print('|{:2d}'.format(self.a[r][c]), end='')
            print("|")
        print('\n')

    def finish(self):
        valid = True
        # check if board is complete
        # if finish , return True
        # else , return False
        for i in range(15):
            r = int(i/4)
            c = i%4
            if self.a[r][c] != i+1:
                valid = False
        return valid

    def premu(self):
        premu = np.random.permutation(16)
        # put premu value into board
        # premu : random premutation [0 1 ... 15]
        for i in range(16):
            r = int(i/4)
            c = i%4
            self.a[r][c] = premu[i]
            if premu[i] == 0:
                self.blank = i

    
    def swap(self, idx1, idx2):
        # exchange 2 special piece on board
        r1 = int(idx1/4)
        r2 = int(idx2/4)
        c1 = idx1%4
        c2 = idx2%4
        num = self.a[r1][c1]
        self.a[r1][c1] = self.a[r2][c2]
        self.a[r2][c2] = num

        

    def move(self, direct):
        # move down : exchange blank and piece at its downside
        # hint : your can call swap(target, self.blank) to help implement
        #        and remember to renew position of blank
        
        if direct == "w":
            # target piece legal or not
            r = int(self.blank/4)
            if r == 0:
                print("Illegal move! Please re-enter a legal move\n")
                return
            self.n = self.blank
            self.blank -= 4
            self.swap(self.n, self.blank)

        if direct == "s":
            # target piece legal or not
            r = int(self.blank/4)
            if r == 3:
                print("Illegal move! Please re-enter a legal move\n")
                return
            self.n = self.blank
            self.blank += 4
            self.swap(self.n, self.blank)
                
        if direct == "a":
            # target piece legal or not
            c = int(self.blank%4)
            if c == 0:
                print("Illegal move! Please re-enter a legal move\n")
                return
            self.n = self.blank    
            self.blank -= 1
            self.swap(self.n, self.blank)
            
        if direct == "d":
            # target piece legal or not
            c = int(self.blank%4)
            if c == 3:
                print("Illegal move! Please re-enter a legal move\n")
                return
            self.n = self.blank
            self.blank += 1
            self.swap(self.n, self.blank)

        
            # passing illegal checking and do swap
        
            
    def play(self):
        self.premu()
        self.show()
        print("There are 4 legal move :\n up: w, down: s, left: a, right: d\n")
        # ask for next move until finish
        
        while self.finish() != True:
            self.move(input("Please move: "))
            print(self.show())
        print("Congraduation !!!")
        
