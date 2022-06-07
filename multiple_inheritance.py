#multiple inheritance demonstrate
class ClassA:
    def classFun(self):
        print("In ClassA")

class ClassB(ClassA):
    def classFun(self):
        print("In ClassB")

class ClassC(ClassA):
    def classFun(self):
        print("In ClassC")

class ClassD(ClassB, ClassC):
    def classFun(self):
        print("In ClassD")
        ClassB.classFun(self)
        ClassC.classFun(self)

obj = ClassD()
obj.classFun()