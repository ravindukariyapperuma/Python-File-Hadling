book = open('workshrs.txt')
data = book.readline()
data = book.readline()
while(data):
    data_list = data.split("\t\t")
