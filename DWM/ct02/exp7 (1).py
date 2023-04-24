def update(temp):
	dist_mat=[]
	for x in range(temp):
		dist_mat.append([])
		for y in range(temp):
			dist_mat[x].append(0)		
	return dist_mat

d=['a','b','c','d','e']
a=[1.0,2.0,3.0,4.0,5.0]
print("*****initial cluster*****")
print(d)
print(a)

for i in range(4):
	print('****after %d iteration****' %(i+1))

	dist_m=update(len(a))
	min_dist=99

	for i in range(len(a)):
		for j in range(len(a)):
			dist=abs(a[i]-a[j])
			dist_m[i][j]=dist
			if(i != j):
				if(dist<min_dist):	
					min_dist=dist
					i_min=i
					j_min=j

	cl1=a[i_min]
	cl2=a[j_min]
	v=(a[i_min]+a[j_min])/2
	a.remove(cl1)	
	a.remove(cl2)
	a.append(v)
	print(a)

	v=(d[i_min]+d[j_min])
	cl1=d[i_min]
	cl2=d[j_min]
	d.remove(cl1)
	d.remove(cl2)
	d.append(v)
	print(d)
