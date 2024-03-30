class My_class:
        person_count = 0
        def __init__(self, name:str, age:int) -> None:
                self.name = name
                self.age = age
                My_class.person_count += 1
                
        def display(self) -> None:
                print(self.name)
                print(self.age)
                print(My_class.person_count)


person1 = My_class("Stefan", 34)
person1.display()



        



