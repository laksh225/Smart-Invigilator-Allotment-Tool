class Faculty:
    def __init__(self, name, flag, designation, experience, availability):
        self.name = name
        self.flag = flag
        self.designation = designation
        self.experience = experience
        self.availability = availability

    def __repr__(self):
        return f'{self.name} - {self.designation} - {self.flag}'

    def inc_flag(self):
        self.flag += 1

    def dec_flag(self):
        self.flag -= 1

def inc_flag(fac):
    fac.flag+=1

def dec_flag(fac):
    fac.flag-=1

if __name__=='__main__':
    Person1 = Faculty(1, "Fac1", 0, "Professor")
    print(Person1)
