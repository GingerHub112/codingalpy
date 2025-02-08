class Employee:
    def __init__(self):
        print("Object created!")
    def __del__(self):
        print("Object deleted!")

def create_and_delete():
    obj = Employee()
    del obj

create_and_delete()