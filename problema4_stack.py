# Problema 4 – Stivă (20p)

class Stiva:
    def __init__(self):
        self.items=[]
    def push(self,elemente):
        self.items.append(elemente)
        return self
    def pop(self):
        return self.items.pop
    def peek(self):
        return self.items[-1]
    def __repr__(self):
        return str(self.items)

#Exemplu:
items=Stiva()
items.push(5)
items.push(7)
items.push(9)
print("pop:",items.pop())
print("peek:",items.peek())
print("Stiva finala:",items)
#output: Stiva finala: [5, 7, 9]
