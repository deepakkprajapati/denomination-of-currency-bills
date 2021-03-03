money=int(input('Enter the money value :'))
moneyValues=[2000,500,200,100,50,20,10,5,2,1]
moneylist=[]
print(f'Money value is {money}')

def cal(moneyValues,money):
    x=money//moneyValues
    y=money%moneyValues
    return x,y


for i in moneyValues:
    a,money=cal(i,money)
    moneylist.append(a)

for i in range(10):
    print(f' {moneyValues[i]} *  {moneylist[i]}')
