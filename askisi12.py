"""
12. Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο
ένα αρχείο ASCII κειμένου και μετατρέπει τον κάθε χαρακτήρα του
στον “κατοπτρικό” του χαρακτήρα ASCII. Κατοπτρικοί χαρακτήρες
είναι αυτοί των οποίων το άθροισμα είναι 128.
Εμφανίστε το κατοπτρικό κείμενο στο χρήστη με ανάποδη σειρά χαρακτήρων.
"""
fle="two_cities.txt"
L=""
f1=open(fle,"r",encoding='utf-8')
fl=1
while fl:
    a=f1.readline()
    if a=="":
        fl=0
    else:
        for x in a:
            oc=ord(x)
            oca=128-ord(x)
            if oca>=0 and oca<=128:
                nch=chr(oca)
                L=nch+L
f1.close()
print('len L:',len(L))
print(L)
