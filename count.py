i='Hey guys whats up!041999'
count=0
count1=0
for x in range(0,len(i)):
 if(i[x].isalpha()):
     count=count+1
 elif(i[x].isdecimal()):
    count1=count1+1
print('Number of letters',count)
print('Number of number',count1)
