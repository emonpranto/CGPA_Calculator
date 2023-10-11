def cgpacal():
    gpamark=0
    subjectno=int(input("Enter how many subject you want to calculate : "))
    sub =[]
    mark =[]
    for i in range (1 ,subjectno+1):
        if i>0:
            subname=input(f"Enter subject name {i}: ")
            sub.append(subname)
            submark=int(input(f"Enter subject mark {i} : "))
            mark.append(submark)

        if submark>=80:
            gpa=5
        elif submark>=70 and submark<80:
            gpa=4
        elif submark>=60 and submark<70:
            gpa=3
        elif submark>=50 and submark<60:
            gpa=2
        elif submark>=44 and submark<50:
            gpa=1
         
        
        else: 
            gpa=0
        
        gpamark += gpa
        
        cgpa= float(gpamark/subjectno)
        
        if cgpa==5:
            grade="A+"
            print("Congratulation, You have passed in exam")
        elif cgpa<5 and cgpa>=4:
            grade="A"
            print("Congratulation, You have passed in exam")
        elif cgpa<4 and cgpa>=3.5:
            grade="A"
            print("Congratulation, You have passed in exam")
        elif cgpa<3.5 and cgpa>=3:
            grade="B"
            print("Congratulation, You have passed in exam")
        elif cgpa<3 and cgpa>=2:
            grade="C"
            print("Congratulation, You have passed in exam")
        elif cgpa<2 and cgpa>=1:
            grade="D"
            print("Congratulation, You have passed in exam")
            
        else :
            grade="F"
            print("You Failed in Exam")
        

        
    print("Your CGPA is :" + str(cgpa))
    print("Your grade is :" , grade)

    print("Your Marksheet:")

    for i in range (subjectno):
        print(sub[i] ,mark[i])



cgpacal()

    






    
