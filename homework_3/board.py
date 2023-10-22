import random
# Класс, в котором вся логика игры
class Board:
    n = 3
    array = [''] * n * n

    def __init__(self, n = 3): # Конструктор инициализирует поле для игры размером n на n
        self.n = n
        self.array = [''] * n * n
        self.lines = []
        for i in range(0, self.n*self.n, self.n):
            line = []
            for j in range(i, i + self.n):
                line.append(j)
            self.lines.append(tuple(line))
        for i in range(self.n):
            line = []
            for j in range(i, self.n*self.n, self.n):
                line.append(j)
            self.lines.append(tuple(line))
        line = []
        for i in range(0, self.n*self.n, self.n+1):
            line.append(i)
        self.lines.append(tuple(line))
        line = []
        for i in range(self.n-1, self.n*self.n-1, self.n-1):
            line.append(i)
        self.lines.append(tuple(line))
        
    def print(self):
        for i in range(0, self.n*self.n, self.n):
            for j in range(i, i + self.n):
                if self.array[j] == '':
                    print(j, end='\t')
                else:
                    print(self.array[j], end='\t')
            print()

    def checkWin(self):
        for line in self.lines:
            result = self.array[line[self.n-1]] != ''
            for i in line[:self.n-1]:
                result &= self.array[i] == self.array[line[self.n-1]]
            if result:
                return self.array[line[self.n-1]]
        return False
    
    def checkDeadlock(self):
        return len(self.getEmptyIndexes()) == 0
    
    def setO(self, index):
        self.array[index] = '◯'

    def setX(self, index):
        self.array[index] = '✖'

    def getEmptyIndexes(self):
        result = []
        for i in range(self.n*self.n):
            if self.array[i] == '':
                result.append(i)
        return result
    
    def run(self): # метод, который запускает процесс игры
        while(self.checkWin() == False):
            self.print()
            print('Выберите позицию крестика:')
            n = int(input())
            print()
            self.setX(n)
            if self.checkDeadlock():
                self.print()
                print("Ничья!")
                return
            self.print()
            print('Выберите позицию нолика:')
            n = int(input())
            print()
            self.setO(n)
            #self.setO(random.choice(self.getEmptyIndexes()))
        self.print()
        print("Победил", self.checkWin())