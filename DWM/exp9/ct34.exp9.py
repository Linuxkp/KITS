file1=open("text1.txt","r+")
file2=open("text2.txt","r+")
file3=open("text3.txt","r+")

count1=count2=count3=0
stopwords=['is','are','a','the','but','if','then','and']
adict={}
for line in file1:
    myline=line.strip('\n').strip('\r').split(' ')
    for word in myline:
        if(word in stopwords):
            continue
        if word in adict:
            adict[word]+=1
        else:
             adict[word]=1

for key in adict:
    print(key,adict[key])
adict={}
for line in file2:
     myline=line.strip('\n').strip('\r').split(' ')
     for word in myline:
         if(word in stopwords):
             continue
         if word in adict:
            adict[word]+=1
         else:
             adict[word]=1

for key in adict:
    print(key,adict[key])
adict={}

for line in file3:
    myline=line.strip('\n').strip('\r').split(' ')
    for word in myline:
        if(word in stopwords):
            continue
        if word in adict:
            adict[word]+=1
        else:
             adict[word]=1

for key in adict:
    print(key,adict[key])
adict={}


