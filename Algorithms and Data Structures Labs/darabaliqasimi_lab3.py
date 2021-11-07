import argparse
class genericUniversity:
    def __init__(self, studentType, ID, firstName, lastName, email):
        self.studentType = studentType
        self.ID = ID
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        
    def get_studentType(self):
        return self.studentType
    def get_ID(self):
        return self.ID
    def get_firstName(self):
        return self.firstName
    def get_lastName(self):
        return self.lastName
    def get_email(self):
        return self.email

    def set_studentType(self, studentType):
        self.studentType = studentType
        return self.studentType
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

class Undergraduate(genericUniversity):
    def __init__(self, studentType, ID, firstName, lastName, email, dormRoom):
        super().__init__(studentType, ID, firstName, lastName, email)
        self.dormRoom = dormRoom
    def get_dormRoom(self, dormRoom):
        return self.dormRoom
    def set_dormRoom(self, dormRoom):
        self.dormRoom = dormRoom
        return self.dormRoom
    def __repr__(self):
        return "{0},{1},{2},{3},{4},{5}".format(self.studentType, self.ID, self.firstName, self.lastName, self.email, self.dormRoom, sep=(","))
        
class Graduate(genericUniversity):
    def __init__(self, studentType, ID, firstName, lastName, email, office):
        super().__init__(studentType, ID, firstName, lastName, email)
        self.office = office
    def get_office(self):
        return self.office
    def set_office(self, office):
        self.office = office
        return self.office
    def __repr__(self):
        return "{0},{1},{2},{3},{4},{5}".format(self.studentType, self.ID, self.firstName, self.lastName, self.email, self.office, sep=(","))
        
class Courses:
    def __init__(self, department, number, enrolledIDList):
        self.department = department
        self.number = number
        self.enrolledIDList = enrolledIDList
    def get_department(self, department):
        return self.department
    def get_number(self, number):
        return self.number
    def get_enrolledIDList(self, enrolledIDList):
        return self.enrolledIDList
    def set_department(self, department):
        self.department = department
        return self.department
    def set_number(self, number):
        self.number = number
        return self.number
    def set_enrolledIDList(self, enrolledIDList):
        self.enrolledIDList = enrolledIDList
        return self.enrolledIDList
    def enrollStudent(self, ID):
        self.enrolledIDList.append(ID)
    def countStudents(self):
        length = len(self.enrolledIDList) -1
        return length

def loadStudents(inputFileName):
    students_array = []
    read_file = open(inputFileName, 'r')
    for obJects in read_file.readlines():
        objects = obJects.split(",")
        studentType = objects[0]
        ID = objects[1]
        firstName = objects[2]
        lastName = objects[3]
        email = objects[4]
        room = objects[5]
        if studentType == "under":
            student = Undergraduate(studentType, ID, firstName, lastName, email, room)
            students_array.append(student)
        elif studentType == "grad":
            student = Graduate(studentType, ID, firstName, lastName, email, room)
            students_array.append(student)
    return students_array
   
def enrolling(inputFileName2, students_array):
    all_students_id = []
    students_list = []
    open_file = open(inputFileName2, "r")
    for all_students in students_array:
        get_id = int(all_students.get_ID())
        all_students_id.append(get_id)
    for ids in open_file:
        convert_int = int(ids)
        if convert_int in all_students_id:
            enrolled_students = convert_int
            students_list.append(enrolled_students)
    cs256Enrollments = Courses("CS", 256, students_list)
    cs256Enrollments.enrollStudent(students_list)
    return cs256Enrollments

if __name__=="__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-s", "--inputFileName")
	parser.add_argument("-e", "--inputFileName2")
	args = parser.parse_args()
             
students_array = loadStudents(args.inputFileName)
cs256Enrollments = enrolling(args.inputFileName2, students_array)
print(cs256Enrollments.countStudents())
