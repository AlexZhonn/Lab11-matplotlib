import matplotlib.pyplot as plt
import os
import math
def program():
    menu = ['1. Student grade' , '2. Assignment statistics','3. Assignment graph']
    for i in menu:        
        print(i)

    option = input('Enter your selection: ')

    if option == '1':
        name = input('What is the student\'s name: ')
        # check if the input students is in the students
        updated_name = name.split()
        with open('data/students.txt') as students_file:
            students_file_list = students_file.readlines()
            for i in range(len(students_file_list)):
                SPL = students_file_list[i].split()
                if updated_name[1] == SPL[1]:
                    if SPL[0][len(SPL[0])-len(updated_name[0]) : len(SPL[0])+1] == updated_name[0]:
                        ID = SPL[0][0:len(SPL[0])-len(updated_name[0])]
                    else:
                        print("Student not found")
                        return
                        
#find the assignment ID from the submission.txt                     
        AID = []
        students_weight = []
        for i in os.listdir('data/submissions'):    
            with open(f"data/submissions/{i}") as file:
                content = file.readline()
                if content.split()[0][:3] == ID:
                    AID.append(content.split()[0][4:9])
                    students_weight.append(content.split()[0][-2:])
        print(students_weight)
                    
# find the weight from assignments.txt
        points = []
        with open('data/assignments.txt') as afile:
            afile.list = afile.readlines()
            for i in range(len(afile.list)):
                for j in AID:
                    if afile.list[i].strip() == j:
                        points.append(afile.list[i+1].strip())
                    elif j[:-1] == afile.list[i]:
                        points.append(afile.list[i+1].strip())

        print(points)
#Calculate Student's grade by multiplying the weight and percentage
        total = 0
        total_points = [(float(point)) * (float(weight)/100) for point , weight in zip(points , students_weight)]
        print(total_points)
        for total_point in total_points:
            total += total_point
        print(total/1000)


    elif option == '2':
        ass_name = input("What is the assignment name: ")
        grade = []
        grade_total = 0
        Ass_ID = None
        with open('data/assignments.txt') as file:
            ass_list = file.readlines()
            for i in range(len(ass_list)):
                if ass_list[i].strip() == ass_name:
                    Ass_ID = ass_list[i+1].strip()
        if not Ass_ID:
            print("Assignment Not Found")
            return
        for i in os.listdir('data/submissions'):    
            with open(f"data/submissions/{i}") as sub_file:
                content = sub_file.readline()
                if content.split()[0][4:9] == Ass_ID:
                    grade.append(int(content.split()[0][-2:]))
                elif content.split()[0][4:8] == Ass_ID:
                    grade.append(int(content.split()[0][-2:]))
        print(grade)
        min_value= min(grade)
        max_value = max(grade)
        for i in grade:
            grade_total += i
        average = grade_total / len(grade)
        print(f'Min: {min_value}%')
        print(f'Avg: {math.floor(average)}%')
        print(f'Max: {max_value}%')
        return
    

    elif option == '3':
        ass_name = input("What is the assignment name: ")
        grade3 = [] 
        Ass_ID = None
        with open('data/assignments.txt') as file:
            ass_list = file.readlines()
            for i in range(len(ass_list)):
                if ass_list[i].strip() == ass_name:
                    Ass_ID = ass_list[i+1].strip()
        if not Ass_ID:
            print("Assignment not Found")
        for i in os.listdir('data/submissions'):    
            with open(f"data/submissions/{i}") as sub_file:
                content = sub_file.readline()
                if content.split()[0][4:9] == Ass_ID:
                    grade3.append(int(content.split()[0][-2:]))
                elif content.split()[0][4:8] == Ass_ID:
                    grade3.append(int(content.split()[0][-2:]))
        plt.hist(grade3,[0,25,50,75,100])
        plt.show()
if __name__ == "__main__":
    program()