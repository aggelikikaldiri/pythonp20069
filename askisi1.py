"""
1.Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει την διάσταση
ενός τετραγώνου και θα φτιάχνει μέσα από λίστες τον αντίστοιχο πίνακα.
Στην συνέχεια θα βρίσκει το πλήθος των θέσεων και θα γεμίζει
στην τύχη τις μισές με μονάδες (στρογγυλοποίηση προς τα πάνω).
Σκοπός είναι να μετρήσετε πόσες τετράδες από μονάδες υπάρχουν
οριζόντια, κάθετα, και διαγώνια. Το πρόγραμμα επαναλαμβάνεται
100 φορές (για την ίδια διάσταση) και επιστρέφει τον μέσο όρο των τετράδων.
"""
import random
def tetrades():
    h=0
    for i in range(len(T)):
        e=sum(T[i])
        if e==4:
           h+=1
    return h
def listoffour(l):
    for i in range(0,len(l)-3):
        x=[]
        for j in range(i,i+4):
            x.append(l[j])
        T.append(x)
syn_tetr=0 
sti=int(input("δώσε διάσταση τετραγώνου (>=4) : "))
gram = sti
for o in range(100):
    T=[]
    L=[]
    for i in range(gram):
        L1=[]
        for j in range(sti):
            L1.append(0)
        L.append(L1)
    th = (gram*sti)
    if th%2==0:
        half_th=th//2
    else:
        half_th=(th//2)+1
    i=0
    while i<half_th:
        x=random.randint(0,th-1)
        r=x//sti
        c=x%sti
        if L[r][c]== 0:
            L[r][c]= 1
            i+=1      
      #ΟΡΙΖΟΝΤΙΑ
    for r in range(0,gram):
        L1 = []
        for c in range(0,sti):
            L1.append( L[r][c] )
        if len(L1) > 4:
            listoffour(L1)
        else:
            T.append( L1 )
    #ΚΑΘΕΤΑ
    for col in range(0,sti):
        L1 = []
        for r in range(0,gram):
            L1.append(L[r][c])
        if len(L1) > 4:
            listoffour(L1)
        else:
            T.append( L1 )
    #1η
    r_v=0
    c_v=0
    fl=0
    r=r_v
    for i in range(0,sti):  
        L1  = []
        fl  = 0
        c= c_v
        while fl==0:
            L1.append(L[r][c])
            r+=1
            c-=1
            if r>= gram or c<0:
                fl=1
        if len(L1) > 4:
            listoffour(L1)
        elif len(L1) == 4:
            T.append( L1 )
        
        r=0
        c_v+=1
    r_v=1
    c_v=sti-1
    fl=0
    for i in range(r_v,gram):
        L1 = []
        fl = 0
        r=r_v
        c=c_v
        while fl==0:
            L1.append(L[r][c])
            r+=1
            c-=1
            if r>=gram or c<0:
                fl=1
        if len(L1) > 4:
            listoffour(L1)
        elif len(L1) == 4:
            T.append( L1 )
        r_v+=1
        c_v=sti-1    
    #2η
    r_v=gram-1
    c_v=0
    f =0
    for i in range(0,gram):
        L1=[]
        fl=0
        r= r_v
        c=c_v
        while fl==0:
            L1.append(L[r][c])  
            r+=1
            c+=1
            if r>= gram or c>= sti :
                fl=1
        if len(L1) > 4:
            listoffour(L1)
        elif len(L1) == 4:
            T.append( L1 )
        r_v-=1
        c_v=0
    r_v=0
    c_v=1
    fl=0
    for i in range(1,sti):
        L1 = []
        fl = 0
        r= r_v
        c=c_v
        while fl == 0:
            L1.append(L[r][c])
            r+=1
            c+=1
            if r>= gram or c>= sti :
                fl=1
        if len(L1) > 4:
            listoffour(L1)
        elif len(L1) == 4:
            T.append( L1 )
        
        r_v=0
        c_v+=1    
    syn_tetr+=tetrades()
print('σύνολο τετράδων : ', syn_tetr)
print(' M.O.  τετράδων : ', round(syn_tetr/100,2))
