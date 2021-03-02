"""
13. Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο ένα αρχείο ASCII κειμένου,
το χωρίζει σε λέξεις και εμφανίζει τα ζευγάρια λέξεων όπου το συνολικό τους μήκος
χαρακτήρων είναι ακριβώς 20. Κάθε ζευγάρι φεύγει από το σύνολο και το
πρόγραμμα τελειώνει όταν εξαντληθούν τα ζευγάρια.
"""
import os.path
import string
import random
def cl(l):
    fl=1
    while fl:
        fl=0
        if  len(l) > 0 :
            if (l[0] not in string.ascii_letters and l[0] not in string.digits) :
                l=l[1:]
                fl=1
        if  len(l)>0:        
            if (l[-1] not in string.ascii_letters and l[-1] not in string.digits) :
                p=len(l)
                l= l[0:p-1]
                fl=1
    return l
a="two_cities.txt"
if not os.path.isfile(a):
    print("Δε βρέθηκε το αρχείο")
else:
    W=[]
    S=[]
    for i in range(20):
        W.append([])
    file1=open(a,"r",encoding='utf-8')
    flag=1
    while flag:
        r=file1.readline()
        if r=="":
          flag=0
        else:
            d=r.split()
            for j in d:
                if len(j)<20:
                    j = cl(j)
                    if len(j) > 0:    
                        W[len(j)].append(j)
    file1.close()
    for i in range(len(W)):
        random.shuffle(W[i])
        S.append(len(W[i]))
    for h in range(1,11):
        while len(W[h])>0 and len(W[20-h])>0 and len(W[10])>1:
            if h!=10:
                print( W[h][0] ," - ", W[20-h][0]," - ",h,20-h )
                W[h].pop(0)
                W[20-h].pop(0)
            elif h == 10 and len(W[h]) > 1:
                print( W[h][0] ," - ", W[h][1]," - ",h,20-h )
                W[h].pop(0)
                W[h].pop(0)
        print()
    print( '       Αρχικές  --  Τελικές' )
    print( '       λέξεις   --   λέξεις' )
    print( '------------------------------' )
    for k in range(len(W)):
        print( "{:0>2}".format( k )," - ", "{:>7,}".format( S[k] ), ' -- ', "{:>7,}".format( len(W[k]) ) )
            
