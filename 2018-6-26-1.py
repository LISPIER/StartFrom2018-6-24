#给出一个文件，每行十个个位数，统计任何一个数在一行中的某个位置出现了多少次

filename="a.txt"

file=open(filename,"r",-1,"utf-8")

lineList=[]

#对counterList进行初始化，counterList[i][j]表示第i位上，数字j出现过多少次
counterList=[]
i=0
j=0
while(i<10):
    counterList.append([])
    while(j<10):
        counterList[i].append(0)
        j+=1
    j=0
    i+=1

line_index=0

number_index=0

for line in file:
    line=line.replace("\n","")
    lineList.append(line)

while(line_index<len(lineList)):
    line=lineList[line_index]
    while(number_index<10):
        number=line[number_index]
        counterList[number_index][int(number)]+=1
        number_index+=1
    number_index=0
    line_index+=1

def count(placeNumber,number):
    return counterList[placeNumber-1][number]

i=0
j=0

while(i<len(counterList)):
    print("在第"+str(i+1)+"位中:")
    while(j<10):
        #print(str(j)+"出现了"+str(count(i+1,j))+"次")
        print(str(j)+"出现的概率是"+str(count(i+1,j))+"/"+str(len(lineList)))
        j+=1
    print("\n")
    j=0
    i+=1