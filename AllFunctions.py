class AllFunctions():
    def Subfields():
        print("Sub-fields in AI are:")
        list=["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        for temp in list:
            print(temp)

    def oddeven():
        num=int(input("Enter the number"))
        if((num%2)==0):
            print(num,"is an Even number")
        else:
            print(num, "a odd number")

    def eligible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(gender=='Male'):
            if(age>=21):
                print('ELIGIBLE')
            else:
                print('NOT ELIGIBLE')
        if(gender=='Female'):
            if(age>=18):
                print('ELIGIBLE')
            else:
                print('NOT ELIGIBLE')

    def percentage():
        mark1=int(input("Subject1= "))
        mark2=int(input("Subject2= "))
        mark3=int(input("Subject3= "))
        mark4=int(input("Subject4= "))
        mark5=int(input("Subject5= "))
        Total = mark1+mark2+mark3+mark4+mark5
        print("Total : ",mark1+mark2+mark3+mark4+mark5)
        Percent = (Total / 500) * 100
        print("Percentage : ",Percent)

    def triangle():
        H=int(input("Height:"))
        B=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle: ",(H*B)/2)
        H1=int(input("Height1:"))
        H2=int(input("Height2:"))
        B=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ",H1+H2+B)