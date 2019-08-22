
f=open("marks.txt","w")
stu = 0
sub = 1
tot = 0
print("After enter all students marks then enter index no 0 for finish program")
no_of_sub = int(input("Enter the number of subjects : "))
print("===================================")
index_no = int(input("Enter the student index no : "))
while (index_no != 0):
    dataindex = "index no : " + str(index_no)
    f.write(dataindex)
    while (sub <= no_of_sub):
        print("subject "+ str(sub) )
        x = input("Enter the subject "+ str(sub)+" mark : ")
        datamarks = ", "+str(x)
        f.write(datamarks)
        tot = tot + int(x)
        sub = sub + 1
    f.write("\n")
    sub = 1
    stu = stu + 1
    print("===================================")
    index_no = int(input("Enter the student index no : "))
f.close()
    
