class Robot:
    def __init__(self, width: int, height: int):
        self.pos = []
        self.dir = []
        self.idx = 0
        self.moved = False
        self.toDir = {0: "East", 1: "North", 2: "West", 3: "South"}
        
        # Pre-calculate boundary
        for i in range(width):
            self.pos.append([i, 0])
            self.dir.append(0)
        for i in range(1, height):
            self.pos.append([width - 1, i])
            self.dir.append(1)
        for i in range(width - 2, -1, -1):
            self.pos.append([i, height - 1])
            self.dir.append(2)
        for i in range(height - 2, 0, -1):
            self.pos.append([0, i])
            self.dir.append(3)
        
        self.dir[0] = 3

    def step(self, num: int) -> None:
        self.moved = True
        self.idx = (self.idx + num) % len(self.pos)

    def getPos(self) -> List[int]:
        return self.pos[self.idx]

    def getDir(self) -> str:
        if not self.moved: return "East"
        return self.toDir[self.dir[self.idx]]