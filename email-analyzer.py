file = open("mbox-short.txt")
di = dict()
cou = 0
largest_count = None
largest_email = None
for line in file:
    if line.startswith("From "):
        #spliting line to get emails only
        spl = line.split()
        emails = spl[1]
        #countng emails
        cou +=1
        #putting into dictionary
        di[emails] = di.get(emails,0)+1

for k,v in di.items():
    #print(k,":",v)
    #finding the email in highest count
    if largest_count is None or v > largest_count:
        largest_count = v
        largest_email = k

print("Total emails: ",cou)
print("Email with the highest count: ",largest_email,":",largest_count)