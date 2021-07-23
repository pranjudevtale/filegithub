pranju=open("question4","r")
for i in (pranju):
    if "delhi" in i:
        pranju=open("delhi#","a")
        print(i)
    elif "shimla" in i:
        pranju=open("shimla#","a")
        print(i)
    else: 
        pranju=open("other#","a")
        print(i)
pranju.closed

