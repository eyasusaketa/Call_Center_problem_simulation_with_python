from random import randint
import time
import matplotlib.pyplot as plt
#import plotly.graph_objects as go
from prettytable import PrettyTable
data=[0]*5
frequency={0:0,1:0,2:0,4:0,3:0,5:0,6:0,7:0}


def interarrival():
    arra=0
    rand=randint(0,100)
    if(rand <=25):
        arra=1
    if(rand>25 and rand<=65):
        arra=2
    if(rand>65 and rand<=85):
        arra=3
    if(rand>85 and rand<=100):
        arra=4
    return arra



def ableservicetime():
    rand=randint(0,100)
    arra=0
    if(rand <=35):
        arra=1
    if(rand>35 and rand<=60):
        arra=2
    if(rand>60 and rand<=80):
        arra=3
    if(rand>80 and rand<=100):
        arra=4
    return arra    



def bakerservicetime():
    rand=randint(0,100)
    arra=0
    if(rand <=30):
        arra=1
    if(rand>30 and rand<=58):
        arra=2
    if(rand>58 and rand<=83):
        arra=3
    if(rand>83 and rand<=100):
        arra=4
    return arra    



def plotgraph(frequency,title):
    x_coordinate = [1, 2, 3, 4, 5,6,7]
    
    y_coordinate = [frequency[0], frequency[1],frequency[2],frequency[3], frequency[4],frequency[5],frequency[6]]
   
    tick_label = ['0', '1', '2', '3', '4','5','6']
   
    plt.bar(x_coordinate, y_coordinate, tick_label = tick_label,
	width = 0.8, color = ['red', 'green'])
    
    plt.xlabel('Upper limit of bin')
    
    plt.ylabel('Occurrence')
  
    plt.title(title)
  
    plt.show()    



def countfre(data):
    frequ=[0]*10
    for i in range(0,10):
        if i==data:
            frequ[i]=frequ[i]+1
        return frequ 


def run(Trial,numberofcaller,choosemethod):
    if choosemethod=="Random":
        for i in range(Trial):
            randomchoose(numberofcaller,i,Trial)
            
    if choosemethod=="Selectional":
        for i in range(Trial):
            callcenter(numberofcaller,i,Trial)
             
def randomchoose(numberofcaller1,round,trial):
    numberofcaller=numberofcaller1+1
    callnum=[0]*numberofcaller
    intrarrival=[0]*numberofcaller
    arrivaltime=[0]*numberofcaller
    ableavail=[0]*numberofcaller
    bakeravail=[0]*numberofcaller
    ableser=[0]*numberofcaller
    choosenserver=[0]*numberofcaller
    bakerser=[0]*numberofcaller
    delay=[0]*numberofcaller
        
    table=PrettyTable(['Caller Nr','Interarrival time','Arrival time','When Able Avail','When Baker Avail.','Server Choosen','Able service time','Baker Service','Caller delay'])
       
    for i in range(1,numberofcaller1+1):
        callnum[i]=i
        if(i==1):
            intrarrival[i]=0    
        if(i>1):
            intrarrival[i]=interarrival()
        arrivaltime[i]=arrivaltime[i-1]+intrarrival[i]
        ableavail[i]=ableavail[i-1]+ableser[i-1]
        bakeravail[i]=bakerser[i-1]+bakeravail[i-1]
        if arrivaltime[i]<=bakeravail[i] and arrivaltime[i]<=ableavail[i] and ableavail[i]==bakeravail[i]:
            choose=randint(1,2)
            if(1==choose):
                choosenserver[i]="able"
                ableser[i]=ableservicetime()
                ableavail[i]=max(arrivaltime[i-1],ableavail[i-1])+ableser[i-1]
            if 2==choose:
                bakerser[i]=bakerservicetime()
                bakeravail[i]=max(arrivaltime[i-1],bakeravail[i-1])+bakerser[i-1]
                choosenserver[i]="baker"
            
        if(arrivaltime[i]>=bakeravail[i]and arrivaltime[i]>=ableavail[i]):
            choose=randint(1,2)
            if(1==choose):
                choosenserver[i]="able"
                ableser[i]=ableservicetime()
                ableavail[i]=max(arrivaltime[i-1],ableavail[i-1])+ableser[i-1]
            if 2==choose:
                bakerser[i]=bakerservicetime()
                bakeravail[i]=max(arrivaltime[i-1],bakeravail[i-1])+bakerser[i-1]
                choosenserver[i]="baker"
            
        elif(arrivaltime[i]<bakeravail[i] and arrivaltime[i]>=ableavail[i]):
            choosenserver[i]="able"
            ableser[i]=ableservicetime()
            ableavail[i]=max(arrivaltime[i-1],ableavail[i-1])+ableser[i-1]
        elif(ableavail[i]>bakeravail[i]):
            bakerser[i]=bakerservicetime()
            bakeravail[i]=max(arrivaltime[i-1],bakeravail[i-1])+bakerser[i-1]
            choosenserver[i]="baker"
        elif(ableavail[i]<bakeravail[i]):
            choosenserver[i]="able"
            ableser[i]=ableservicetime()   
            ableavail[i]=max(arrivaltime[i-1],ableavail[i-1])+ableser[i-1] 
        if( ableavail[i] >arrivaltime[i] and arrivaltime[i]< bakeravail[i]):
            delay[i]=min(ableavail[i],bakeravail[i])-arrivaltime[i]
        if round==0:
            table.add_row([callnum[i],intrarrival[i],arrivaltime[i],ableavail[i],bakeravail[i],choosenserver[i],ableser[i],bakerser[i],delay[i]])
    if round==0:
        print(table)
    
    for item in delay:
        if item in frequency:
            frequency[item]+=1
        else:
            frequency[item]=1    

    if round==trial-1:
        plotgraph(frequency=frequency,title="For "+str(round+1)+" Simulation Trial")
def callcenter(numberofcaller1,round,trial):
    numberofcaller=numberofcaller1+1
    callnum=[0]*numberofcaller
    intrarrival=[0]*numberofcaller
    arrivaltime=[0]*numberofcaller
    ableavail=[0]*numberofcaller
    bakeravail=[0]*numberofcaller
    ableser=[0]*numberofcaller
    choosenserver=[0]*numberofcaller
    bakerser=[0]*numberofcaller
    delay=[0]*numberofcaller
        
    table=PrettyTable(['Caller Nr','Interarrival time','Arrival time','When Able Avail','When Baker Avail.','Server Choosen','Able service time','Baker Service','Caller delay'])
       
    for i in range(1,numberofcaller1+1):
        callnum[i]=i
        if(i==1):
            intrarrival[i]=0    
        if(i>1):
            intrarrival[i]=interarrival()
        arrivaltime[i]=arrivaltime[i-1]+intrarrival[i]
        ableavail[i]=ableavail[i-1]+ableser[i-1]
        bakeravail[i]=bakerser[i-1]+bakeravail[i-1]
        if arrivaltime[i]<=bakeravail[i] and arrivaltime[i]<=ableavail[i] and ableavail[i]==bakeravail[i]:
            choosenserver[i]="baker"
            bakerser[i]=bakerservicetime()
            bakeravail[i]=max(arrivaltime[i-1],bakeravail[i-1])+bakerser[i-1]
            
           
        if(arrivaltime[i]>=bakeravail[i]):
            choosenserver[i]="baker"
            bakerser[i]=bakerservicetime()
            bakeravail[i]=max(arrivaltime[i-1],bakeravail[i-1])+bakerser[i-1]
        elif(arrivaltime[i]<bakeravail[i] and arrivaltime[i]>=ableavail[i]):
            choosenserver[i]="able"
            ableser[i]=ableservicetime()
            ableavail[i]=max(arrivaltime[i-1],ableavail[i-1])+ableser[i-1]
        elif(ableavail[i]>bakeravail[i]):
            bakerser[i]=bakerservicetime()
            bakeravail[i]=max(arrivaltime[i-1],bakeravail[i-1])+bakerser[i-1]
            choosenserver[i]="baker"
        elif(ableavail[i]<bakeravail[i]):
            choosenserver[i]="able"
            ableser[i]=ableservicetime()   
            ableavail[i]=max(arrivaltime[i-1],ableavail[i-1])+ableser[i-1] 
        if( ableavail[i] >arrivaltime[i] and arrivaltime[i]< bakeravail[i]):
            delay[i]=min(ableavail[i],bakeravail[i])-arrivaltime[i]
        if round==0:
            table.add_row([callnum[i],intrarrival[i],arrivaltime[i],ableavail[i],bakeravail[i],choosenserver[i],ableser[i],bakerser[i],delay[i]])
    if round==0:
        print(table)
    
    for item in delay:
        if item in frequency:
            frequency[item]+=1
        else:
            frequency[item]=1    

    if round==trial-1:
        plotgraph(frequency=frequency,title="For "+str(round+1)+" Simulation Trial")
    

caller=input("Enter number of Callers")
trial=input("Enter number of Simulation Trial")
print("Enter Method of Choose")
print("1: Baker gets call if both are idle")
print("2:Call is assigned randomly to Able and baker")
chooseinput=input()
if chooseinput=='1':
    run(Trial=int(trial),numberofcaller=int(caller),choosemethod="Selectional")
elif chooseinput=='2':
    run(Trial=int(trial),numberofcaller=int(caller),choosemethod="Random")    
else:
    print("Wrong input Please try again")


