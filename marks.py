
f=open("marks.txt","w")
stu = 1
sub = 1
tot = 0
avg = 0
print("============================================")
no_of_stu = int(input("Enter the number of students : "))
no_of_sub = int(input("Enter the number of subjects : "))
print("============================================")

while (stu <= no_of_stu):
    index_no = int(input("Enter the student index no : "))
    dataindex = "index no : " + str(index_no)+ "\t"
    f.write(dataindex)
    while (sub <= no_of_sub):
        print("subject "+ str(sub) )
        x = input("Enter the subject "+ str(sub)+" mark : ")
        datamarks = "subject " + str(sub) + " marks : " + str(x) + "\t"
        f.write(datamarks)
        tot = tot + int(x)
        sub = sub + 1
    datatotal = " (Total = " + str(tot) + ")"
    f.write(datatotal)
    dataavg = " (Avarage = " + str(tot/no_of_sub) + ")"
    f.write(dataavg)
    f.write("\n")
    tot = 0
    sub = 1
    stu = stu + 1
    print("============================================")
f.close()
    
