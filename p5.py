n=int(input("Enter The no of elements in list: "))
wgt=[0]*n

for i in range(n):
    wgt[i]=int(input("enter weights: "))

VeryLight=[]
NormalLoad=[]
Overload=[]
HeavyLoad=[]
InvalidEntries=[]

for w in wgt:
    if(w < 0):
        InvalidEntries+=[w]
    elif(w<=5):
       VeryLight+=[w]
    elif(w<=25):
        NormalLoad+=[w]
    elif(w<=60):
       HeavyLoad+=[w]
    else:
        Overload+=[w]

Name=input("enter the name ")
r=0
for i in Name :
    r+=1
    
PLI=r%3
AffectedCount=0

if(PLI==0):
    print("Rule A")
    for j in Overload:
        AffectedCount+=1
        InvalidEntries+=[j]
    Overload=[]
    
    
elif(PLI==1):
    print("Rule B")
    for j in VeryLight:
        AffectedCount+=1
    VeryLight=[]

else:
    print("Rule C")
    for j in VeryLight:
        AffectedCount+=1
    
    for j in OverLoad:
        AffectedCount+=1

    VeryLight=[]
    OverLoad=[]
    InvalidEntries=[]
    
    
    

ValidCount=len(VeryLight)+len(NormalLoad)+len(Overload)+len(HeavyLoad)



print("Len of Name: ",r)
print("PLI Value: ",PLI)



print("Very Light: ",VeryLight)
print("Normal Load: ",NormalLoad)
print("Heavy Load: ",HeavyLoad)
print("Overload: ",Overload)
print("Invalid Entries: ",InvalidEntries)
print("Total Valid Weights: ",ValidCount)
print("Total Affected Weights: ",AffectedCount)