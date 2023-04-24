import math
def dec(a,b,c,d,m,n):
    file_object=open('data.txt','r+')
    f=file_object.readlines()
    count_1_y=0
    count_1_n=0
    count_2_y=0
    count_2_n=0
    county=0
    countn=0
    count_1=0
    count_2=0

    for x in range(10):
        splits=f[x].strip('\n').split('\t')
        if splits[m]==a and splits[n]==c:
            count_1_y=count_1_y+1
        if splits[m]==a and splits[n]==d:
            count_1_n=count_1_n+1
        if splits[m]==b and splits[n]==c:
            count_2_y=count_2_y+1
        if splits[m]==b and splits[n]==d:
            count_2_y=count_2_y+1
        if splits[n]==c:
            county=county+1
        if splits[n]==d:
            countn=countn+1
        if splits[m]==a:
            count_1=count_1+1
        if splits[m]==b:
            count_2=count_2+1

    e=-(float(county)/10*math.log(float(county)/10,2))-(float(countn)/10*math.log(float(countn)/10,2))
    ec1=float(count_1)/10*(-float(count_1_y)/count_1*math.log(float(count_1_y)/count_1,2)-float(count_1_n)/count_1*math.log(float(count_1_n)/count_1,2))
    ec2=float(count_2)/10*(-float(count_2_y)/count_2*math.log(float(count_2_y)/count_2,2)-float(count_2_n)/count_2*math.log(float(count_2_n)/count_2,2))

    ec=ec1+ec2
    gain=e-ec
    return gain
    file_object.close()


gain1=dec('20', '43', 'y','n', 0, 3)
gain2=dec('76', '66', 'y', 'n', 1,3)
gain3=dec('50', '40', 'y', 'n', 2,3)

print("gain1 ", gain1)
print("gain2 ", gain2)
print("gain3 ", gain3)

