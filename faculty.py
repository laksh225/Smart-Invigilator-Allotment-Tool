class Faculty:
    def __init__(self, index, name, flag, designation):
        self.name = name
        self.index = index
        self.flag = flag
        self.designation = designation
    def __str__(self):
        return f'{self.name} - {self.designation}'
       
if __name__=='__main__':
    Person1 = Faculty(1, "Fac1", 0, "Professor")
    print(Person1)