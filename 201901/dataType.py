#data type
#integer real complex

#no limit for interger
#1267650600228229401496703205376
print(pow(2,100))
print(pow(2,100,1000))#376

#real has error
#False
print(0.1 + 0.2 == 0.3)

print(pow(1.01,365))
print(pow(0.99,365))
#37.7834343329
#0.0255179644523

#4.63
x=1.0
i=0
for i in range(0,365):
    if(i%7 in [6,0]):
        x*=0.99
    else:
        x*=1.01

print("{:.2f}".format(x))

def dayUp(df):
    dayUp=1.0
    for i in range(365):
        if(i%7 in [6,0]):
            dayUp*=0.99
        else:
            dayUp*=1+df
        return dayUp

dayf=0.01
while dayUp(dayf)<37.78:
    dayf+=0.001

print(dayf)