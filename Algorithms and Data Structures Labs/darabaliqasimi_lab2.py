import argparse
class Student:
    def __init__(self, ID, firstName, lastName, email, year, gpa):
        self.ID = ID
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        if year == "FR" or year == "SO" or year == "JR" or year == "SR":
            self.year = year
        else:
            raise ValueError('The year does not exist or is not in correct format')
        if gpa <= 4.0 or gpa >= 0.0:
            self.gpa = gpa
        else:
            raise ValueError("Invalid gpa")
    def get_ID(self):
        return self.ID
    def get_firstName(self):
        return self.firstName
    def get_lastName(self):
        return self.lastName
    def get_email(self):
        return self.email
    def get_year(self):
        return self.year
    def get_gpa(self):
        return self.gpa
    
    def set_ID(self, ID):
        self.ID = ID
        return self.ID
    def set_firstName(self, firstName):
        self.firstName = firstName
        return self.firstName
    def set_lastName(self, lastName):
        self.lastName = lastName
        return self.lastName
    def set_email(self, email):
        self.email = email
        return self.email
    def set_year(self, year):
        self.year = year
        return self.year
    def set_gpa(self, gpa):
        self.gpa = gpa
        return self.gpa
    
def loadStudents(InputFileName):
    student_array = []
    InputFile = open(InputFileName, 'r')
    for objects in InputFile.readlines():
        student_info = objects.split(',')
        ID = student_info[0]
        firstName = student_info[1]
        lastName = student_info[2]
        email = student_info[3]
        year = student_info[4]
        gpa = float(student_info[5])
        student_object = Student(ID, firstName, lastName, email, year, gpa)
        student_array.append(student_object)
    return student_array

def displayStudents(student_array):
    for student in student_array:
        print(student.get_ID(), student.get_firstName(), student.get_lastName(), student.get_email(), student.get_year(), student.get_gpa(), sep=(','))
        
def averageGPA(student_array):
    gpa_list = []
    for student in student_array:
        gpa = float(student.get_gpa())
        gpa_list.append(gpa)
    sum_gpa = 0.0
    for student_gpa in gpa_list:
        sum_gpa += student_gpa
        average_gpa = sum_gpa/len(gpa_list)
        round_average_gpa = round(average_gpa, 2)
    print(round_average_gpa)

def improveGPA(student_array, percentimprovement = 1.0):
    for gpa in student_array:
        gpas = float(gpa.get_gpa())
        process_improvement = gpas * percentimprovement/100
        improve = gpas + process_improvement
        if improve > 4.0:
            improve = 4.0
        gpa.set_gpa(improve)

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--InputFileName")
    parser.add_argument("-p", "--percentimprovement")
    args = parser.parse_args()

student_array = loadStudents(args.InputFileName)

displayStudents(student_array)
averageGPA(student_array)
improveGPA(student_array)
averageGPA(student_array)
