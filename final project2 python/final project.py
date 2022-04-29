import os
import datetime
import traceback
import matplotlib.pyplot as plt

class semester:
    def init(self, number_of_semester, courses):
        self.number_of_semester = number_of_semester
        self.courses = courses


def check_if_digit(student_id):  # this method to check if the id student is digit or not
    if student_id.isnumeric() == True:
        return True
    return False


def check_if_in_system(student_id):  # check if the file is already exist
    try:  # if file is in system
        file = open(student_id, 'r')
        file.close()
        print('The student id is already in the system!')
        return True
    except IOError:  # if the file is not in the system
        print('The student id is not in the system ...')
        return False


def sum(array=[]):  # function to make the sum of student markes
    Thesum = 0

    for i in array:
        Thesum = Thesum + int(i)

    return (Thesum)


# The first part : Add a new record file: here the program must ask to enter student ID. The
# program must raise an error if the ID is not unique.

def new_record():
    # we need to check if the student id is digit and exist in the system
    student_id = input("Could you please enter the student id: ")
    if check_if_digit(student_id) == False:  # check if the enterd file is only digits
        print("OPS!, student id must be only digit values.")
        return
    else:
        if check_if_in_system_part_2(student_id) == True:  # check if the file is in the system
            print("Try entering another number")
            return
        else:
            new_file = student_id + ".txt"  # add to the student id -> .txt
            new_file = open(new_file, "w")
            new_file.write("")
            new_file.close()
            print("The file has been added successfully")


# function to read the mean file (cources) and fill the data in array called cources
def read_cources(cources=[]):
    "This function will read the main cources"
    file = open('Courses.txt', "r")
    for line in file:
        line2 = line.strip('\n')
        cources.append(line2)  # filling the array
    file.close()


def if_semester_valid(student_id, tot):
    file = open(student_id, "r")
    line = " "
    while line:
        line = file.readline()  # readlines() is used to read all the lines and then return them as each line a string element in a list.
        lisp = line.split(';')  #

        if lisp[0].replace(" ", "") == tot:
            return False
    return True


def add_semester(student_id, semesteer):
    file = open(student_id, "a")  # open the file named n=by the student id
    file.write(semesteer + "\n")  # write
    file.close()
    return

def check_if_in_system_part_2(student_id):
    for c in os.listdir():
        if c.strip(".txt") == student_id:#remove .txt from the file name if it was =student id then its exist.
            return True
    return False

# function to fill the student file data in array called courcesss and takes the name of the student file with courcesss array
def read_std_file(student_id, courcesss=[]):
    "This function will read the student cources"
    f = open(student_id, 'r')
    for line in f:
        line2 = line.strip('\n')
        line3 = line2.replace(';', ",")

        firstWord = line.split("/")[1]  # take the number of semester after /
        if (firstWord[0] == "1" or firstWord[0] == "2" or firstWord[0] == "3"):
            firstWord2 = firstWord[3:]  # start taking data from first cource after ;
            line4 = firstWord2.strip('\n')  # to remove the end of lines
            line5 = line4.split(",")  # split according to ;
            for li in line5:
                courcesss.append(li)



# function to read the data of student's file and put them in 3 arrays according to semester
def read_student_file(stdudent_id, semester1=[], semester2=[], semester3=[], semester4=[]):
    "This function will read the file and fill the informations in an array"
    f = open(stdudent_id, "r")
    for line in f:
        line2 = line.strip('\n')
        line3 = line2.replace(';', ",")

        firstWord = line.split("/")[1]  # take the number of semester after /
        if firstWord[0] == "1":
            firstWord2 = firstWord[3:]  # start taking data from first cource after ;
            line4 = firstWord2.strip('\n')  # to remove the end of lines
            line5 = line4.split(",")  # split according to ;
            for li in line5:
                semester1.append(li)  # filling the first array --> first semester

        elif firstWord[0] == "2":
            firstWord2 = firstWord[3:]  # start taking data from first cource after ;
            line4 = firstWord2.strip('\n')  # to remove the end of lines
            line5 = line4.split(",")  # split according to ;
            for li in line5:
                semester2.append(li)  # filling the secound array --> secound semester

        elif firstWord[0] == "3":
            firstWord2 = firstWord[3:]  # start taking data from first cource after ;
            line4 = firstWord2.strip('\n')  # to remove the end of lines
            line5 = line4.split(",")  # split according to ;
            for li in line5:
                semester3.append(li)  # filling the third array --> summer semester

        else:
            firstWord2 = firstWord[3:]  # start taking data from first cource after ;
            line4 = firstWord2.strip('\n')  # to remove the end of lines
            line5 = line4.split(",")  # split according to ;
            for li in line5:
                semester4.append(li)  # filling the fourth array --> fourth semester


# The second part :Add new semester with student course and grades: here the program must ask
# to enter the required information (student ID, year/semester, courses and
# grades). The system must raise an error if there is missing information or the
# information in wrong format.

def new_semester(courses=[]):
    student_id = input("Could you please enter the student id: ")
    if check_if_digit(student_id) == False:
        print("OPS!, student id must be only digit values.")
        return
    if check_if_in_system_part_2(student_id) == False:
        print("ERROR!, the id is not in the system, try entering another number")
        return

    student_id += ".txt"
    while True:
        try:
            time = input("Could you please enter the year you want?: \n"
                         "note you should know: please enter the year followed by '-' like:(2020-2021) :)")

            year = time.split('-')
            is_valid_date = True
            try:
                datetime.datetime(int(year[0]),1,1)
                datetime.datetime(int(year[1]),1,1)
            except ValueError:
                is_valid_date = False

            if is_valid_date:
                print("year is valid ..")
            else:
                print("year is not valid..")

            #here the semester number should be only 1 or 2 or 3
            semesteer =(input("Could you please enter the number of the semester: "))
            if semesteer == "1" or semesteer == "2" or semesteer == "3":
                print("the courses file consist the following:")
            else:
                print("ERROR!, semester should only be 1, 2 or 3.")

            semester = ""

            tot = time + "/" + semesteer#add the year entered by the user to the number of semester and between them '/'
            semester += "\n" + tot + " ;"#add to the semester the above method and add ';' to make it like the given project
            #semester=year+"/"+semesteer+";"
            if if_semester_valid(student_id, tot) == False:
                f = TypeError("OPS!, you entered a semester already exist. try sth new!")
                raise f
            read_cources(courses) #calling read_courses function to open the file and start compare if the course in or not
            print(courses)#print all courses inside the file
            while True:
                try:
                    cource = input("Could you please enter the course name or if you want to exit enter '0': ")
                    cource = cource.upper()
                    if cource == "0":
                        break #return to main menu
                    if (courses.count(cource) > 0) == False:#this method check if the course is exist in the courses file or not
                        cour = TypeError("the course you entered does not exist! try enter from above.")
                        raise cour
                    grade = input("Could you please enter the grade: ")
                    #here the program will check if the entered grade is digit, if not digit and was not between 0 and 100 then print the grade is not valid
                    if (check_if_digit(grade) == False) or (int(grade) < 0 or int(grade) > 100) == True:
                        cour = TypeError("ERROR!, sorry but the grade you entered is not valid")
                        raise cour
                    semester += " " + cource + " " + grade + ","#here add all the methods above together

                except Exception as cour:#Catch and print exception messages
                    print(cour)
            if semester == tot + " ;":#raise an error if the course was not added
                e = TypeError("please enter courses to add to the record")
                raise e
            semester = semester[:-1]
            add_semester(student_id, semester)#calling the function

            f1 = open(student_id, 'r')
            f2 = open('output1.txt', 'w')
            for eachline in f1:
                if (not eachline.isspace()):
                    f2.write(eachline)
            f1.close()
            f2.close()

            os.remove(student_id)
            f3 = open(student_id, 'w')
            f4 = open('output1.txt', 'r')
            for linee in f4:
                f3.write(linee)

            f3.close()
            f4.close()

            os.remove('output1.txt')
            print("The data added to file successfully")
            break #return to main menu
        except Exception as e:#Catch and print exception messages
            print(e)
            continue

# The third part : Update: here the system must ask for student ID and the name of the course to
# be change and the new grade.

def update():
    student_id = input("Could you please enter the student id: ")
    student_id += ".txt"  # connected the student id with .txt --> to make student id as a file name
    student = []
    student2 = []
    if check_if_in_system(student_id) == True:  # to check if the file is in system
        print("The file is exist ...")
        cource = input("Please inter the course you want to change its mark: ")
        cource = cource.upper()
        f = open(student_id, 'r')
        fout = open('output.txt', 'w')
        stringchange = ""
        for line in f:
            line2 = line.strip('\n')
            line3 = line2.replace(';', ",")
            firstWord = line.split("/")[1]  # take the number of semester after /

            if (firstWord[0] == "1" or firstWord[0] == "2" or firstWord[0] == "3"):
                firstWord2 = firstWord[3:]  # start taking data from first cource after ;
                line4 = firstWord2.strip('\n')  # to remove the end of lines
                line5 = line4.split(",")  # split according to ;
                n = 0;
                for li in line5:
                    cor =  li.split(" ")[1] # take the first part of each element after ,
                    if cor == cource:  # if the first part is equal to the cource that user needs then
                      n = 1;
                      new_mark = input("please enter the new mark: ")
                      old_mark = li.split(" ")[2]
                      change = li.replace(old_mark, new_mark)
                      stringchange = change
                      fout.write(line.replace(li, stringchange))

                if (n == 0) is True:
                  fout.write(line)

                else:
                    n = 0;
                    continue;

        f.close()
        fout.close()

        os.remove(student_id)
        f11 = open(student_id, 'w')
        f22 = open('output.txt', 'r')
        for linee in f22:
            f11.write(linee)

        f11.close()
        f22.close()

        os.remove('output.txt')
        print("update successfully")


    else:
        print("The file dose not exist !!!")



# The fourth part : Student statistics: first the program must ask for student ID. The program will
# print information such as number of taken hours, remaining courses (you need
# to create a list/file that contains all ENCS and ENEE courses for computer

def studentStatistics(cources=[]):
    student_id = input("Could you please enter the student id: ")
    student_id += ".txt"
    student = []

    if check_if_in_system(student_id) == True:  # check if the student id is in the system
        print("Student statistics :")
        read_std_file(student_id, student)  # reading informations
        stdcou = []
        num1 = 0;
        for eachcource in cources:
            stdcou.append(eachcource)
            for element in student:
                    elm = element.split(" ")[1]  # take the course without the mark
                    if eachcource == elm:
                        num1 += 3  # each course = 3 hours
                        stdcou.pop()  # to remove the course from the stdout array

        print(" * The number of taken hours : ", num1)  # the first part of part 4

        print(" * The remaining courses : ", stdcou)  # the second part of part 4

        print(" * Average per semester :")  # the third part of part 4

        semester1 = []  # array of first semester cources
        semester2 = []  # array of second semester cources
        semester3 = []  # array of summer semester cources

        read_student_file(student_id, semester1, semester2, semester3)  # send the arrays and student id to the function

        allmarkes = []  # array connected all arrays togethor
        markes1 = []  # array of first semester cources markes
        markes2 = []  # array of secound semester cources markes
        markes3 = []  # array of summer semester cources markes

        # variables to calculate the average
        avg1 = 0
        avg2 = 0
        avg3 = 0

        # filling the arrays with semester markes
        for mark in semester1:
            mark2 = mark.split(" ")[2]  # to get the part of each cource
            markes1.append(mark2)  # filling the array
            allmarkes.append(mark2)  # filling the all array

        if (len(markes1) > 0) is True:

          sum1 = sum(markes1)  # send the array to the sum function
          avg1 = sum1 / len(markes1)  # calculate avg
          print("  -The average of the first semester : ", avg1)  # print the avg of the first semester

        for mark in semester2:
            mark2 = mark.split(" ")[2]  # to get the part of each cource
            markes2.append(mark2)  # filling the array
            allmarkes.append(mark2)  # filling the all array

        if (len(markes2) > 0) is True:
          sum2 = sum(markes2)  # send the array to the sum function
          avg2 = sum2 / len(markes2)  # calculate avg
          print("  -The average of the second semester : ", avg2)  # print the avg of the second semester

        for mark in semester3:
            mark2 = mark.split(" ")[2]  # to get the part of each cource
            markes3.append(mark2)  # filling the array
            allmarkes.append(mark2)  # filling the all array

        if (len(markes3) > 0) is True:
          sum3 = sum(markes3)  # send the array to the sum function
          avg3 = sum3 / len(markes3)  # calculate avg
          print("  -The average of the summer semester : ", avg3)  # print the avg of the summer semester

        allsum = sum(allmarkes)  # send the array to the sum function
        allavg = allsum / len(allmarkes)  # calculate avg
        print(" * Overall average : ", allavg)  # print the avg of all semesters
        print("")

# The fifth part : Global statistics: here the program must print information regarding all student
# such as overall students average, average hours per semester, plot the
# distribution of their grades (histogram).

def globalStatistics(cources=[]):

    fout = open('allFiles.txt', 'w') # file containing  all students file
    files = []
    list = os.listdir("C:\\Users\\hp pro\\Desktop\\project") # find all files in the folder
    for file in list:
        if file.endswith(".txt"): # if file end with .txt
          file2 = file.strip(".txt")
          if check_if_digit(file2) == True:
             files.append(file)
             f = open(file, 'r')
             for line in f:
                 fout.write(line)
                 fout.write("\n")
    fout.close()

    fin = open('allFiles.txt', 'r')
    fout2 = open('files.txt', 'w')
    for line in fin:
        if (not line.isspace()):
            fout2.write(line)

    fin.close()
    fout2.close()

    students_id = "files.txt"
    student =[]
    if check_if_in_system(students_id) == True:  # check if the student id is in the system
        print("Global statistics :")
        read_std_file(students_id, student)  # reading informations
        num1 = 0;
        for eachcource in cources:
            for element in student:
                    elm = element.split(" ")[1]  # take the course without the mark
                    if eachcource == elm:
                        num1 += 3  # each course = 3 hours

        print(" * The number of taken hours : ", num1)  # the first part of part 4

        print(" * Average per semester :")  # the third part of part 4

        semester1 = []  # array of first semester cources
        semester2 = []  # array of second semester cources
        semester3 = []  # array of summer semester cources

        read_student_file(students_id, semester1, semester2, semester3)  # send the arrays and student id to the function

        allmarkes = []  # array connected all arrays togethor
        markes1 = []  # array of first semester cources markes
        markes2 = []  # array of secound semester cources markes
        markes3 = []  # array of summer semester cources markes

        # variables to calculate the average
        avg1 = 0
        avg2 = 0
        avg3 = 0

        # filling the arrays with semester markes
        for mark in semester1:
            mark2 = mark.split(" ")[2]  # to get the part of each cource
            markes1.append(mark2)  # filling the array
            allmarkes.append(mark2)  # filling the all array

        if (len(markes1) > 0) is True:

          sum1 = sum(markes1)  # send the array to the sum function
          avg1 = sum1 / len(markes1)  # calculate avg
          print("  -The average of the first semester for all students : ", avg1)  # print the avg of the first semester

        for mark in semester2:
            mark2 = mark.split(" ")[2]  # to get the part of each cource
            markes2.append(mark2)  # filling the array
            allmarkes.append(mark2)  # filling the all array

        if (len(markes2) > 0) is True:
          sum2 = sum(markes2)  # send the array to the sum function
          avg2 = sum2 / len(markes2)  # calculate avg
          print("  -The average of the second semester for all students: ", avg2)  # print the avg of the second semester

        for mark in semester3:
            mark2 = mark.split(" ")[2]  # to get the part of each cource
            markes3.append(mark2)  # filling the array
            allmarkes.append(mark2)  # filling the all array

        if (len(markes3) > 0) is True:
          sum3 = sum(markes3)  # send the array to the sum function
          avg3 = sum3 / len(markes3)  # calculate avg
          print("  -The average of the summer semester for all students : ", avg3)  # print the avg of the summer semester

        allsum = sum(allmarkes)  # send the array to the sum function
        allavg = allsum / len(allmarkes)  # calculate avg
        print(" * Overall average for all semesters : ", allavg)  # print the avg of all semesters
        print("")
        plt.hist(allavg)
        plt.hist(avg1)
        plt.hist(avg2)
        plt.hist(avg3)
        plt.title('plot for the distribution of student grades\n'
                  'blue:allavg, orange:semester1, green:semester2 and red:semester3')
        plt.show()
# The sixth part : Searching: here the system must retrieve the ID of the students that satisfy the
# given criteria. Here you can search for the following: based on average, taken
# hours.

def searching():
    seet = set()
    while True:
        fout = open('allFiles.txt', 'w')  # file containing  all students file
        files = []
        num2 = 0;
        list = os.listdir("C:\\Users\\hp pro\\Desktop\\project")  # find all files in the folder
        for file in list:
            if file.endswith(".txt"):  # if file end with .txt
                file2 = file.strip(".txt")
                if check_if_digit(file2) == True:
                    files.append(file)
                    num2+=1

        fout.close()

        option = input("Could you please enter what you want to search?\n"
                       "1) Average\n"
                       "2) Taken hours\n"
                       "3) Return to menu\n")
        if option == "1":
            averag = input("Could you please enter the average you want me to search? :)\t")
            if averag.isnumeric() == False:
                print("ERROR!, the average should be only digit values :(, try again :)")
                break#or continue
            #the user should chose with what to compare the grade
            check = input("Hello again!,chose from below what to compare : \n"
                      "1) grater than\n"
                      "2) less than\n"
                      "3) equal\n")
            if (check == "1" or check == "2" or check == "3") == False:
                print("AN ERROR OCCURRED, could you please chose again (valid options!)\n")
                break #return to main menu

            elif check == "1":
                for eachFile in files:
                    semester1 = []  # array of first semester cources
                    semester2 = []  # array of second semester cources
                    semester3 = []  # array of summer semester cources

                    read_student_file(eachFile, semester1, semester2,
                                      semester3)  # send the arrays and student id to the function

                    allmarkes = []  # array connected all arrays togethor
                    markes1 = []  # array of first semester cources markes
                    markes2 = []  # array of secound semester cources markes
                    markes3 = []  # array of summer semester cources markes

                    # variables to calculate the average
                    avg1 = 0
                    avg2 = 0
                    avg3 = 0

                    # filling the arrays with semester markes
                    for mark in semester1:
                        mark2 = mark.split(" ")[2]  # to get the part of each cource
                        markes1.append(mark2)  # filling the array
                        allmarkes.append(mark2)  # filling the all array

                    if (len(markes1) > 0) is True:
                        sum1 = sum(markes1)  # send the array to the sum function
                        avg1 = sum1 / len(markes1)  # calculate avg
                        if (float(avg1) > float(averag)) is True:
                            File = eachFile.strip(".txt")
                            print("This student with this number ", File," got an average higher than the required average in the first semester")

                    for mark in semester2:
                        mark2 = mark.split(" ")[2]  # to get the part of each cource
                        markes2.append(mark2)  # filling the array
                        allmarkes.append(mark2)  # filling the all array

                    if (len(markes2) > 0) is True:
                        sum2 = sum(markes2)  # send the array to the sum function
                        avg2 = sum2 / len(markes2)  # calculate avg
                        if (float(avg2) > float(averag)) is True:
                            File = eachFile.strip(".txt")
                            print("This student with this number ", File," got an average higher than the required average in the second semester")

                    for mark in semester3:
                        mark2 = mark.split(" ")[2]  # to get the part of each cource
                        markes3.append(mark2)  # filling the array
                        allmarkes.append(mark2)  # filling the all array

                    if (len(markes3) > 0) is True:
                        sum3 = sum(markes3)  # send the array to the sum function
                        avg3 = sum3 / len(markes3)  # calculate avg
                        if (float(avg3) > float(averag)) is True:
                            File = eachFile.strip(".txt")
                            print("This student with this number ", File," got an average higher than the required average in the summer semester")

            elif check == "2":
                for eachFile in files:
                    semester1 = []  # array of first semester cources
                    semester2 = []  # array of second semester cources
                    semester3 = []  # array of summer semester cources

                    read_student_file(eachFile, semester1, semester2,
                                      semester3)  # send the arrays and student id to the function

                    allmarkes = []  # array connected all arrays togethor
                    markes1 = []  # array of first semester cources markes
                    markes2 = []  # array of secound semester cources markes
                    markes3 = []  # array of summer semester cources markes

                    # variables to calculate the average
                    avg1 = 0
                    avg2 = 0
                    avg3 = 0

                    # filling the arrays with semester markes
                    for mark in semester1:
                        mark2 = mark.split(" ")[2]  # to get the part of each cource
                        markes1.append(mark2)  # filling the array
                        allmarkes.append(mark2)  # filling the all array

                    if (len(markes1) > 0) is True:
                        sum1 = sum(markes1)  # send the array to the sum function
                        avg1 = sum1 / len(markes1)  # calculate avg
                        if (float(avg1) < float(averag)) is True:
                            File = eachFile.strip(".txt")
                            print("This student with this number ", File," got an average less than the required average in the first semester")

                    for mark in semester2:
                        mark2 = mark.split(" ")[2]  # to get the part of each cource
                        markes2.append(mark2)  # filling the array
                        allmarkes.append(mark2)  # filling the all array

                    if (len(markes2) > 0) is True:
                        sum2 = sum(markes2)  # send the array to the sum function
                        avg2 = sum2 / len(markes2)  # calculate avg
                        if (float(avg2) < float(averag)) is True:
                            File = eachFile.strip(".txt")
                            print("This student with this number ", File," got an average less than the required average in the second semester")

                    for mark in semester3:
                        mark2 = mark.split(" ")[2]  # to get the part of each cource
                        markes3.append(mark2)  # filling the array
                        allmarkes.append(mark2)  # filling the all array

                    if (len(markes3) > 0) is True:
                        sum3 = sum(markes3)  # send the array to the sum function
                        avg3 = sum3 / len(markes3)  # calculate avg
                        if (float(avg3) < float(averag)) is True:
                            File = eachFile.strip(".txt")
                            print("This student with this number ", File," got an average less than the required average in the summer semester")

            elif check == "3":
                for eachFile in files:
                    semester1 = []  # array of first semester cources
                    semester2 = []  # array of second semester cources
                    semester3 = []  # array of summer semester cources

                    read_student_file(eachFile, semester1, semester2,
                                      semester3)  # send the arrays and student id to the function

                    allmarkes = []  # array connected all arrays togethor
                    markes1 = []  # array of first semester cources markes
                    markes2 = []  # array of secound semester cources markes
                    markes3 = []  # array of summer semester cources markes

                    # variables to calculate the average
                    avg1 = 0
                    avg2 = 0
                    avg3 = 0

                    # filling the arrays with semester markes
                    for mark in semester1:
                        mark2 = mark.split(" ")[2]  # to get the part of each cource
                        markes1.append(mark2)  # filling the array
                        allmarkes.append(mark2)  # filling the all array

                    if (len(markes1) > 0) is True:
                        sum1 = sum(markes1)  # send the array to the sum function
                        avg1 = sum1 / len(markes1)  # calculate avg
                        if (float(avg1) == float(averag)) is True:
                            File = eachFile.strip(".txt")
                            print("This student with this number ", File, " got an average equal the required average in the first semester")

                    for mark in semester2:
                        mark2 = mark.split(" ")[2]  # to get the part of each cource
                        markes2.append(mark2)  # filling the array
                        allmarkes.append(mark2)  # filling the all array

                    if (len(markes2) > 0) is True:
                        sum2 = sum(markes2)  # send the array to the sum function
                        avg2 = sum2 / len(markes2)  # calculate avg
                        if (float(avg2) == float(averag)) is True:
                            File = eachFile.strip(".txt")
                            print("This student with this number ", File," got an average equal the required average in the second semester")

                    for mark in semester3:
                        mark2 = mark.split(" ")[2]  # to get the part of each cource
                        markes3.append(mark2)  # filling the array
                        allmarkes.append(mark2)  # filling the all array

                    if (len(markes3) > 0) is True:
                        sum3 = sum(markes3)  # send the array to the sum function
                        avg3 = sum3 / len(markes3)  # calculate avg
                        if (float(avg3) == float(averag)) is True:
                            File = eachFile.strip(".txt")
                            print("This student with this number ", File, " got an average equal the required average in the summer semester")

            continue

        elif option == "2":
            takenHoures = input("Could you please enter the hours you want me to search? :)\t")
            if takenHoures.isnumeric() == False:
                print("ERROR!, the taken houres should be only digit values :(, try again :)")
                break  # or continue
            # the user should chose with what to compare the grade
            check = input("Hello again!,chose from below what to compare : \n"
                          "1) grater than\n"
                          "2) less than\n"
                          "3) equal\n")
            if (check == "1" or check == "2" or check == "3") == False:
                print("AN ERROR OCCURRED, could you please chose again (valid options!)\n")
                break  # return to main menu

            elif check == "1":
                for eachfile in files:
                    student = []
                    read_std_file(eachfile, student)  # reading informations
                    num1 = 0;
                    for eachcource in cources:
                        for element in student:
                            elm = element.split(" ")[1]  # take the course without the mark
                            if eachcource == elm:
                                num1 += 3  # each course = 3 hours

                    if (int(num1) > int(takenHoures)) is True:
                        print("1")
                        file2 = eachfile.strip(".txt")
                        print("This student with this number ", file2,
                              " got an houres grater than the required hour average")

            elif check == "2":
                for eachfile in files:
                    student = []
                    read_std_file(eachfile, student)  # reading informations
                    num1 = 0;
                    for eachcource in cources:
                        for element in student:
                            elm = element.split(" ")[1]  # take the course without the mark
                            if eachcource == elm:
                                num1 += 3  # each course = 3 hours

                    if (int(num1) < int(takenHoures)) is True:
                        file2 = eachfile.strip(".txt")
                        print("This student with this number ", file2,
                              " got an houres less than the required hour average ")

            elif check == "3":
                for eachfile in files:
                    student = []
                    read_std_file(eachfile, student)  # reading informations
                    num1 = 0;
                    for eachcource in cources:
                        for element in student:
                            elm = element.split(" ")[1]  # take the course without the mark
                            if eachcource == elm:
                                num1 += 3  # each course = 3 hours
                    if (int(num1) == int(takenHoures)) is True:
                        print("3")
                        file2 = eachfile.strip(".txt")
                        print("This student with this number ", file2,
                              " got an houres equal the required hour average ")

            continue

        elif option == "3":
            break
while True:

    cources = []
    read_cources(cources)

    login = input("Hello, welcome to Amany & Hadeel student recording system\n------------------------------------\n"
                  "please chose one from below:\n"
                  "\t\t\t\t1-I'm an admin"
                  "\n\t\t\t\t2-I'm a user"
                  "\n\t\t\t\t3-End the program\n------------------------------------\n")
    if login == "1":
        while True:
            print("\t\tWelcome to the admin page\n--------------------------\n"
                  "\t\t\t\tMenu\n"
                  "\t\t1-Add a new record file to the system\n"
                  "\t\t2-Add a new semester to the student record\n"
                  "\t\t3-update the student record\n"
                  "\t\t4-Student statistics\n"
                  "\t\t5-Global statistics\n"
                  "\t\t6-Searching\n"
                  "\t\t7-return to login\n--------------------------\n")
            option = input()
            if option == "1":
                new_record()
            elif option == "2":
                new_semester(cources)
            elif option == "3":
                update()
            elif option == "4":
                studentStatistics(cources)
            elif option == "5":
                globalStatistics(cources)
            elif option == "6":
                searching()
            elif option == "7":
                break
            else:
                print("AN ERROR OCCURRED, could you please chose again (valid options!)\n")
    elif login == "2":
        while True:
            print("\t\tWelcome to the student page\n--------------------------\n"
                  "\t\t\t\tMenu\n"
                  "\t\t1-Student statistics\n"
                  "\t\t2-Global statistics\n"
                  "\t\t3-return to login\n--------------------------\n")
            option = input()
            if option == "1":
                studentStatistics(cources)
            elif option == "2":
                globalStatistics(cources)
            elif option == "3":
                break
            else:
                print("AN ERROR OCCURRED, could you please chose again (valid options!)\n")
    else:
        exit()