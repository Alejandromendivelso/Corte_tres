class GfG: 
    def __init__(self): 
        self.MAX =100
        self.arr = [0] * self.MAX
        self.no = 0
  
    def breakLine(self): 
        print("\n---------------------------------------") 
  
    def reinalugar(self, k, i):  
        for j in range(1, k): 
            if (self.arr[j] == i or 
               (abs(self.arr[j] - i) == abs(j - k))
               ): 
                return False
        return True
  
    def display(self, n): 
        self.breakLine() 
        self.no += 1
        print("Solucion No.", self.no, end = " ") 
        self.breakLine() 
  
        for i in range(1, n + 1): 
            for j in range(1, n + 1): 
                if self.arr[i] != j: 
                    print("\t0", end = " ") 
                else: 
                    print("\tR", end = " ") 
            print() 
  
    def nQueens(self, k, n):  
        for i in range(1, n + 1): 
            if self.reinalugar(k, i): 
                self.arr[k] = i 
                if k == n: 
                    self.display(n) 
                else: 
                    self.nQueens(k + 1, n) 
  
if __name__ == '__main__': 
    print("PROBLEMA N-REINAS CON BACKTRAkING")
    n = int(input("Introduzca numero de reinas: "))
    obj = GfG() 
    obj.nQueens(1, n) 
  
