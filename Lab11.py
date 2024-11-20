import matplotlib.pyplot as plt
import os
import math
def program():
    menu = ['1. Student grade' , '2. Assignment statistics','3. Assignment graph']
    for i in menu:        
        print(i)

    option = input('Enter your selection: ')

    if option == '1':
        # check if the input students is in the students and store the ID.
        name = input('What is the student\'s name: ')
        
        updated_name = name.split()
        ID = None
        with open('data/students.txt') as students_file:
            students_file_list = students_file.readlines()
            for i in range(len(students_file_list)):
                SPL = students_file_list[i].split()
                if updated_name[1] == SPL[1]:
                    if SPL[0][3:] == updated_name[0]:
                        ID = SPL[0][:3]
        if not ID:
            print("Student not found")
            return
        
#find the assignment ID from the submission.txt and weight  
        AID_weight_dic = {}             
        AID = None
        students_weight = []
        for i in os.listdir('data/submissions'):    
            with open(f"data/submissions/{i}") as file:
                content = file.readline()
                if content.split()[0][:3] == ID:
                    AID = content.split()[0][4:9]
                    if AID[-1] == '|':
                        AID = AID[:-1]
                    students_weight = content.split()[0][-2:]
                    AID_weight_dic[AID] = int(students_weight)

# find the point from assignments.txt
        AID_points_dic = {}
        points = None
        with open('data/assignments.txt') as afile:
            afile_list = afile.readlines()
            for i in range(len(afile_list)):
                for j in AID_weight_dic.keys():
                    if afile_list[i].strip() == j:
                        points = afile_list[i+1].strip()
                        AID_points_dic[j] = int(points)
#Calculate Student's grade by multiplying the weight and percentage
        total = 0
        total_points = {key: AID_weight_dic[key] * AID_points_dic[key] for key in AID_weight_dic if key in AID_points_dic}
        total = sum(total_points.values())
        print(f'{round(total/1000)}%')


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
        plt.hist(grade3, bins = [0,25,50,75,100])
        plt.show()
if __name__ == "__main__":
    program()