"""
Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο ένα αρχείο ASCII κειμένου
και να το κόβει σε συνεχόμενες τριάδες λέξεων (όλες τις δυνατές).
Στην συνέχεια, διαλέγει τυχαία μια τριάδα και προσπαθεί να συντάξει
ένα τυχαίο κείμενο από αυτό, χρησιμοποιώντας τις δυο τελευταίες λέξεις
και επιλέγοντας μια τριάδα που να ξεκινάει από αυτές τις δυο. Το πρόγραμμα
ολοκληρώνεται, όταν γράψει 200 λέξεις ή δεν μπορεί να επιλεγχεί άλλη τριάδα λέξεων.
"""


import random
import string

#**************************
def clear_word(word):
    """
    καθαρίζει το 1ο ή το τελευταίο γράμμα κάθε λέξης
    αν δεν είναι γράμμα ή αριθμός
    """

    flag=1
    while flag:

        flag=0
        if  len(word) > 0 :
            if (word[0] not in string.ascii_letters and word[0] not in string.digits) :
                word = word[1:]
                flag=1
            
        if  len(word) > 0 :        
            if (word[-1] not in string.ascii_letters and word[-1] not in string.digits) :
                ln = len(word)
                word = word[0:ln-1]
                flag=1

    return word
#**************************

#******************************
def make_triades(lista):

    for i in range(0,len(lista)-2):
        m=[]
        for j in range(i,i+3):
            m.append(lista[j])
        words3.append(m)

    return
#*******************************

#*******************************
def find_compatible_triades(triada):
    tmp=[]
    for item in words3:
        if item[0] == triada[1] and item[1] == triada[2]:
            tmp.append(words3.index(item))

    if len(tmp) > 0 :
        y = random.choice(tmp)
        word = words3[y]
    else:
        word = -1

    return word
    
#*******************************

M=[] # ολες οι λέξεις
words3=[] # ολες οι τριαδες λέξεων

var_file="two_cities.txt"

f1=open(var_file,"r",encoding='utf-8')



flag=1
while flag:
    x=f1.readline()

    if x=="":
        flag=0
    else:
        y=x.split()
        for item in y:
            item = clear_word(item)
            if len(item) > 0:
                M.append(item)
            
f1.close()

make_triades(M)

##print( 'len words3 :', len(words3) )
random_triada = random.choice(words3)
i=3
txt=random_triada[0] + " " + random_triada[1] + " " + random_triada[2]

flag=1
while flag:
    new_triada = find_compatible_triades(random_triada)

    if new_triada != -1 and i <= 200:
        txt += " " + new_triada[2]
        i+=1
        random_triada = new_triada
        
    elif new_triada == -1 or i > 200:
        print(txt)
        flag=0

    
    

