def f(x):
    return int(x)*3
ipt=input("input x value here")
result=f(ipt)
print(result)
ipt=input("write any sentence as you like")
result_l=len(ipt)
print(result_l)

def eo(x):
    if x%2==0:
        print("you entered even")
    elif x%2==1:
        print("you entered odd")
    else:
        print("you should etner integer")

ipt=input("judge even or odd, enter any number. ")
ipt=float(ipt)
result=eo(ipt)
print(result)
