class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house 
    
    @property
    def houses(self):
        return self._house
    
    @houses.setter
    def house(self, house):
        if house not in ["Gryffindor", "HuffLepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("INvalid house in Hogwarts")

def main():

    student = get_student()

    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")

    student = Student(name, house) # Construtor de usando uma classe de modelo.

    return student    

if __name__ == "__main__":
    main()