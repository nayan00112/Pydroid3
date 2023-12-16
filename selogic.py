pra=input("enter pragraph: ")

p=['.',',', '"', "'", "_","-", '*', '^','&','#',':',";",')', ']',">","<",'(','[', "?", "!","=","+","×","÷",'/','~','%','}','{','$','|','`','¡', "'"]
cw=['is','are','am','we', 'you', "he",'she', 'it','were','was', 'has', 'have', 'do', 'did', 'dose', 'not', "doesn't", "don't", "of", "for", "when", "where", "whose", "who", "what", "whome", "be", "being", "can", "could", "will", "would", "must", 'much', 'many', "too" ,"how" ,"in", 'out', 'on', 'top', 'and','this', 'that','those','these', '  ', ' i ']
pra=pra.replace(" I ", " ")
for i in range(10):
    pra=pra.replace(str(i),"")
   
for i in p:
    pra=pra.replace(i,"").lower()



npra=pra.split(' ')

#for i in npra:
#    for j in cw:
#        if j==i:
#            npra.remove(j);
t1=0
t2=0            
while (t1<len(npra)):
    while (t2<len(npra)):
        if (npra[t1]==npra[t2]) and (t1!=t2):
            npra.remove(npra[t1])
        t1+=1
        t2+=1

fnpra=[]
for i in npra:
    if i!="":    
        fnpra.append(i.replace('\n',""))
    
print()
voc=[]
for i in npra:
    if i!="":
        voc.append(i)
   
for i in voc:
    print(i)          