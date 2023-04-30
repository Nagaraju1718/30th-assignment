str=input()
list1=[]
for i in range(len(str)):
    char =str[i].lower()
    if char not in list1:
        list1.append(char)
for i in list1:
    print(i,end=',')
        
