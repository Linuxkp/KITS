def freq_two(count,a,b):
	counta=0
	if count>=3:
		for i in itemset:
			if a in i and b in i:
				counta=counta+1
	if counta >= 3:
		return([a,b],counta)
	else:	
		pass
	
def freq_three(a,b,c):
	count = 0
	for i in itemset:
		if a in i and b in i and c in i:
			count = count+1
	if count >= 3:	
		return ([a,b,c],count)
	else:
		print("Count of(2,3,4) is less than 3: count=",count)
		pass

itemset=[[1,2,3,4],[1,2,4],[1,2],[2,3,4],[2,3],[3,4],[2,4]]
print("This is our given Itemset:\n",itemset)
print("Minimum Support is: 3\n")
count1=count2=count3=count4=0
for i in itemset:
	if 1 in i:
		count1=count1+1
	if 2 in i:		
		count2=count2+1
	if 3 in i:
		count3=count3+1 
	if 4 in i:
		count4=count4+1
print("Frequent itemset of size 1 are:\n (Since all are above minimum support)\n")
print("1: ",count1,"\n")
print("2: ",count2,"\n")
print("3: ",count3,"\n")
print("4: ",count4,"\n")

freq_list=[]
freq_list.append(freq_two(count1,1,2))
freq_list.append(freq_two(count1,1,3))
freq_list.append(freq_two(count1,1,4))
freq_list.append(freq_two(count2,2,3))
freq_list.append(freq_two(count2,2,4))
freq_list.append(freq_two(count3,3,4))

print("Frequent itemset of size 2 are :\n")
print(freq_list)

print("Pairs(1,3) and (1,4) are not frequent\n")
print("Hence larger set must not include (1,3) and (1,4)\n")
print("By considering above condition, we have (2,3,4) as triple\n")
freq3=freq_three(2,3,4)
print("Frequent itemset of size 3 are :\n",freq3)
