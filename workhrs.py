book = open('workhrs.txt')
data = book.readline()
data = book.readline()
while(data):
    data_list = data.split("\t\t")
    print(data_list)
    data = book.readline()
