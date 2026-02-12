#personilisation option B
n=int(input("no of inputs :"))
name=input("enter the name :")
data=[]
for i in range(n):
    a=input("enter data :")
    data.append(a)
no_list=[]
sr_list=[]
for i in data:
    if i.isdigit():
        no_list.append(i)
    else :
        sr_list.append(i)
        
#personilisation option B    
x=len(no_list)
y=len(sr_list)
x-=1
y-=1
if(len(name)%2==0):
    no_list.remove(no_list[0])
    sr_list.remove(sr_list[0])
else:
    no_list.remove(no_list[x])
    sr_list.remove(sr_list[y])
print("numbers list",no_list)

print("string list",sr_list)
print("Total Numbers",len(no_list))
print("Total strings",len(sr_list))
