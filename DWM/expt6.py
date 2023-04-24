itemset=[[1,2,3,4],[1,2,4],[1,2],[2,3,4],[2,3],[3,4],[2,4]]
min_sup=3
count1=count2=count3=count4=0
freq1=[]
freq2=[]
freq3=[]
count=0

def func1(a):
         count=0
         for i in itemset:
             count=count+1
         if count>=min_sup:
             freq1.append(a)

def func2(a,b):
         count=0
         for i in itemset:
             if a in i and b in i:
                 count+=1
         if count>=min_sup:
             if a in freq1 and b in freq1:
                 freq2.append([a,b])
                
def func3(a,b,c):
         count=0
         for i in itemset:
             if a in i and b in i and c in i:
                 count= count+1
         if count>=min_sup:
             if a in freq1 and b in freq1 and c in freq1:
                 if [a,b] in freq2 and [a,c] in freq2:
                     freq3.append([a,b,c])
func1(1)
func1(2)
func1(3)
func1(4)
print(freq1)
func2(1,2)
func2(1,3)
func2(1,4)
func2(2,3)
func2(2,4)
func2(3,4)
print(freq2)
func3(1,2,3)
func3(1,2,4)
func3(1,3,4)
func3(2,3,4)
print(freq3)
