import os
import time
import keyboard

class maze:
    def __init__(self) -> None:
        self.maze = [
                    ["X", "X", "X", "X", "X", "X", "X"],
                    ["X", " ", "X", " ", "X", " ", " "],
                    ["X", " ", " ", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", " ", " ", "X"],
                    ["X", " ", "X", "X", "X", " ", "X"],
                    ]
        self.ply = pos(5, 1)
        self.end = pos(1, 6)
        self.maze[self.ply.y][self.ply.x] = "P"
        self.maze[self.end.y][self.end.x] = "E"
    
    def isInBound(self, y, x):
        if y>=0 and x>=0 and y<len(self.maze) and x<len(self.maze[0]):
            return True
        else:
            return False
    
    def print(self): #เคลียร์หน้าจอหลังแล้วปลิ้นเขาวงกต
        os.system("cls")
        print("\n\n\n")
        for row in self.maze:
            for col in row:
                print(col," ", end="")
            print("")
        print("\n\n\n")
    
    def printEND(self): #เคลียร์หน้าจอหลังแลเวปลิ้นCongraturation
        os.system("cls")
        print("\n\n\n")
        print(">>>>> Congraturation!!! <<<<<")
        print("\n\n\n")
        keyboard.wait("")

    #def move_up(self):
        next_move = pos(self.ply.y-1, self.ply.x)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True
    
    #def move_down(self):
        next_move = pos(self.ply.y+1, self.ply.x)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    #def move_left(self):
        next_move = pos(self.ply.y, self.ply.x-1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    #def move_right(self):
        next_move = pos(self.ply.y, self.ply.x+1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def moveEND(self, y, x):
        if self.maze[y][x] == "E":
            self.printEND()
            return False
        self.maze[self.ply.y][self.ply.x] = " "  # ลบตำแหน่งเดิม
        self.maze[y][x] = "P"  # วางตำแหน่งใหม่
        self.ply = pos(y, x)
        self.print()
        return True
    
    def solve_maze(self):
        stack = [(self.ply.y, self.ply.x)]  # เริ่มต้นที่ P
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # บน, ล่าง, ซ้าย, ขวา

        while stack:
            y, x = stack.pop()  # หยิบตำแหน่งสุดท้ายออกมา (DFS)
            if (y, x) in visited:
                continue
            visited.add((y, x))
            
            if not self.moveEND(y, x):  # ถ้าเจอ E ให้หยุด
                break

            # เพิ่มตำแหน่งที่สามารถเดินได้ลงใน Stack
            for dy, dx in directions:
                next_y, next_x = y + dy, x + dx
                if (next_y, next_x) not in visited and self.isInBound(next_y, next_x) and self.maze[next_y][next_x] in [" ", "E"]:
                    stack.append((next_y, next_x))
                time.sleep(0.25)
class pos:
    def __init__(self) -> None:
        self.y = None
        self.x = None
    
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

if __name__ == '__main__':

    m = maze()
    m.print()
    m.solve_maze()
    
