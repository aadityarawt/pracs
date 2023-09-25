class operation:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        c=self.a+self.b
        return c
    
    def sub(self):
        d=self.a+self.b
        return d

x=float(input("Enter the first number: "))
y=float(input("Enter the second number: "))
c=operation(x,y)

a=c.add()
s=c.add()

print("The Addition is:",a)
print("The Subtraction is:",s)

