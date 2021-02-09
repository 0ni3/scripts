# coding=utf-8
class Person:

    def __init__(self, name, surname, age, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address

    def personal_file(self):
        file = f"""
        Name : {self.name}
        Surname : {self.surname}
        Age : {self.age}
        Address : {self.address}\n"""
        return file

    def change_file(self):
        print("""Modifica scheda:
        1 - Name
        2 - Surname
        3 - Age
        4 - Address""")
        choise = input("Cosa vuoi modificare?")
        if choise == "1":
            self.nome = input("Nuovo nome -->")
        if choise == "2":
            self.surname = input("Nuovo cognome -->")
        if choise == "3":
            self.age = input("Nuova età -->")
        if choise == "4":
            self.address = input("Nuovo indirizzo -->")


class Student(Person):
    profile = "Studente"

    def __init__(self, name, surname, age, address, studies):
        super().__init__(name, surname, age, address) # gestisce l'init principale della classe genitore Persona
        self.studies = studies

    def personal_file(self):
        file = f"""
        Profilo:{Student.profile}
        Corsi di Studi:{self.studies}
        ***"""
        return super().personal_file() + file


class Teacher(Person):
    profile = "Insegnante"

    def __init__(self, name, surname, age, address, subjects=None):
        super().__init__(name,surname,age,address)
        if subjects is None:
            self.subjects = []
        else:
            self.subjects = subjects

    def personal_file(self):
        file = f"""
        Profilo:{Teacher.profile}
        Materie insegnate:{self.subjects}
        ***"""
        return super().personal_file() + file


student_one = Student("Mike","Doe","22","via bo","informatica")
teacher_one = Teacher("Mario","Rossi","33","viale roma 32",["Python", "Security", "C"])
print(student_one.personal_file())
print(teacher_one.personal_file())

#print(help(Student))
