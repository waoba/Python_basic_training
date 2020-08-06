coil=80
count=0
wallet=1000
count=input('How many coils do you want?')
price=coil*int(count)
wallet-=price
if wallet<0:
    print('you do not have enough to buy them')
else:
    print('you buy '+count+' coils with '+str(price)+' and remain '+str(wallet)+' in your wallet')
