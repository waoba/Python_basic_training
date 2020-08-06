list=["Walking dead","Antlage","the sopranos","Vampire diaries"]
for drama in list:
    i=list.index(drama)
    print(i,drama)
#for i in range(25,51):
#    print(i)
#list=["7","77","777","7777"]
#while True:
#    ipt=input("type q to quit or type a number: ")
#    ipt=str(ipt)
#    if ipt=="q":
#        print("quit the sequence")
#        break
#    elif ipt in list:
#        print("Correct!")
#        continue
#    else:
#        print("Incorrect!")
#        continue
list1=[8,19,148,4]
list2=[9,1,33,83]
mult=[]
for num1 in list1:
    for num2 in list2:
        mult.append(num1*num2)

print(mult)
