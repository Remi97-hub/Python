class Multfunc():
    def SubfeildsinAI():
        print("Sub-Feilds in AI are:")
        subfeilds=('Machine Learning','Neural Network','vision','Robotics','Speech Processing','Natural Language Processing')
        for list in subfeilds:
            print(list)
    
    def oddeven():
        num=int(input("Enter a number:"))
        if(num%2==1):
            print(num,"is odd")
        else:
            print(num,"is even")
   
    def MarriageEligiblity():
        gender=input("Enter yor gender")
        age=int(input("Enter your Age"))
        if(gender=="male" and age>20):
            print("Eligible")
            message="Eligible"
        elif(gender=="female" and age>18):
            print("Eligible")
            message="Eligible"
        else:
            print("Not Eligible")
            message="Not Eligible"
            return message
   
    def percentage():
        s1=int(input("Subject1:"))
        s2=int(input("Subject2:"))
        s3=int(input("Subject3:"))
        s4=int(input("Subject4:"))
        s5=int(input("Subject5:"))
        total=s1+s2+s3+s4+s5
        percent=total/5
        print("Total:",total)
        print("Percentage:",percent)
    
    def trianglearea():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        areaformula=(height*breadth)/2
        print("Area Formula:(Height*Breadth)/2")
        return areaformula
   
    def triangleperimeter():
        h1=int(input("Height1:"))
        h2=int(input("Height2:"))
        breadth=int(input("Breadth:"))
        perimeterformula=h1+h2+breadth
        print("Perimeter Formula: Height1+Height2+Breadth")
        return perimeterformula
            