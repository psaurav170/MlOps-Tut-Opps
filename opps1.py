# initaiate a class
class employee:
    # special method/dunder method - constructor
    def __init__(self):
        print("Started executing attributes/data")
        self.id = 123
        self.salary = '130000'
        self.designation = 'MLOps Engineer'
        print("attributes/data has been initiated")

    def travel(self, destination):
        print("This travelled method was called mannually")
        print(f'employee is traveling to {destination}')

#create an obj/instance of the class
sam = employee()

# Printing a attribute
#print(sam.id, sam.designation, sam.salary)

#calling a method
#sam.travel('Pune')
print(type(sam))