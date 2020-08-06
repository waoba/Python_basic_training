#import statistics
#list=[0,1,3,5,10,33,3,3,56,100]
#print(list)
#print(statistics.mean(list))
#print(statistics.median(list))
#print(statistics.mode(list))

#import cubed
#a=3.1000
#a=float(a)
#print(cubed.cubic(a))
#print(a*a*a)
#print(a*a)
#print(a)

#Test1
import os
import csv
#with open(os.path.join("C:/","Python","chap9.csv"),"r") as f:
#with open("C:/Python/chap9.csv","r",encoding="utf-8") as f:
#    print(os.path.join("C:/","Python","chap9.csv"))
#    print(f.read())

#TEst2
#comment=input("type a word: ")
#with open(os.path.join("C:/","Python","output","chap9_test.txt"),"w") as f:
#    for i in range(2):
#        f.write(comment)
#        f.write(",")

#Test3
list=[]
list.append(["ﾄｯﾌﾟｶﾞﾝ","リスキービジネス","マイノリティレポート"])
list.append(["タイタニック","レヴェナント","インセプション"])
list.append(["トレーニングデイ","マンオンファイヤ","フライト"])
#print(list)
with open("chap9.csv","w",encoding="utf_8_sig",newline="") as f:
    w=csv.writer(f,delimiter=",")
    for i in list:
        #print(i)
        w.writerow(i)

with open("chap9.csv","r",encoding="utf_8_sig") as f:
    r=csv.reader(f,delimiter=",")
    for row in r:
        print(row)
        print(",".join(row))
