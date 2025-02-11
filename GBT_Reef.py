import os
import time

class maze:
    def __init__(self) -> None:
        self.maze = [
                    ["X", "X", "X", "X", "X", "X", "X"],
                    ["X", " ", " ", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", "E"],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", " ", " ", "X"],
                    ["X", "P", "X", "X", "X", "X", "X"],
                    ]
        self.ply = pos(5, 1)  # จุดเริ่มต้น P
        self.end = pos(2, 6)  # จุดสิ้นสุด E
    
    def isInBound(self, y, x):
        return 0 <= y < len(self.maze) and 0 <= x < len(self.maze[0])
    
    def print(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("\n\n\n")
        for row in self.maze:
            print(" ".join(row))
        print("\n\n\n")
        time.sleep(0.25)
    
    def printEND(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("\n\n\n")
        print(">>>>> Congraturation!!! <<<<<")
        print("\n\n\n")
    
    def move(self, y, x):
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
            
            if not self.move(y, x):  # ถ้าเจอ E ให้หยุด
                break

            # เพิ่มตำแหน่งที่สามารถเดินได้ลงใน Stack
            for dy, dx in directions:
                next_y, next_x = y + dy, x + dx
                if (next_y, next_x) not in visited and self.isInBound(next_y, next_x) and self.maze[next_y][next_x] in [" ", "E"]:
                    stack.append((next_y, next_x))

class pos:
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

if __name__ == '__main__':
    m = maze()
    m.print()
    m.solve_maze()
