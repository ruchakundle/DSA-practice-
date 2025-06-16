#example 1
class cars:
    name="BMW"
    model=123
c=cars()
print(c.name,c.model)

#example 2
class employee:
    def enter(self):
        self.name= "Mahesh"
        self.prn=12345
        self.salary=100000
    def op(self):
        print("the name of the employee is:",self.name)
        
e=employee() 
e.enter()
e.op()

#exmaple of pet
class pet:
    def enter(self):
        self.name=input("enter pet name:")
        self.age=input("enter pet age:")
        self.species=input("enter pet species:")
        
    def display(self):
        print("name=",self.name)
        print("age=",self.age)
        print("species=",self.species)
        
p1=pet()
p1.enter()
p1.display()

#or

class pett:
    def enterr(self,namee,agee,speciess):
       self.namee=namee
       self.agee=agee
       self.speciess=speciess
       
    def displayy(self):
        print("name:",self.namee)
        print("age:",self.agee)
        print("species:",self.speciess)
        
p2=pett()
p2.enterr("moti","4","gavathi")
p2.displayy()
        
        