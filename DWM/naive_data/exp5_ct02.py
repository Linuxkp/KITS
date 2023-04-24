def Naive_classify():
    file_object=open('Naive_data1.txt','r+')
    data=file_object.readlines()
    cnt_red_y=0
    cnt_dom_y=0
    cnt_suv_y=0
    cnt_red_n=0
    cnt_dom_n=0
    cnt_suv_n=0
    total_y=0
    total_n=0
    for x in range(10):
        splist=data[x].split('\t')
        if splist[0]=='red' and splist[3]=='yes\n':
            cnt_red_y=cnt_red_y+1
        if splist[2]=='domastic' and splist[3]=='yes\n':
            cnt_dom_y=cnt_dom_y+1
        if splist[1]=='suv' and splist[3]=='yes\n':
            cnt_suv_y=cnt_suv_y+1
        if splist[0]=='red' and splist[3]=='no\n':
            cnt_red_n=cnt_red_n+1
        if splist[2]=='domastic' and splist[3]=='no\n':
            cnt_dom_n=cnt_dom_n+1
        if splist[1]=='suv' and splist[3]=='no\n':
            cnt_suv_n=cnt_suv_n+1
        if splist[3]=='yes\n':
            total_y=total_y+1
        if splist[3]=='no\n' :
            total_n=total_n+1

    pr_red_y = cnt_red_y/total_y
    pr_red_n = cnt_red_n/total_n

    pr_dom_y = cnt_dom_y/total_y
    pr_dom_n = cnt_dom_n/total_n

    pr_suv_y = cnt_suv_y/total_y
    pr_suv_n = cnt_suv_n/total_n

    pr_yes = total_y/10
    pr_no = total_n/10

    result_y = pr_yes * pr_red_y * pr_suv_y * pr_dom_y
    result_n = pr_no * pr_red_n * pr_suv_n * pr_dom_n

    print("probability for yes is ", result_y)
    print("probability for no is ", result_n)

    if result_y > result_n:
        print("Classified as yes\n")
    elif result_y < result_n:
        print("Classified as no\n")
    else:
        print("Can't Classify\n")

    file_object.close()
Naive_classify()
input("Press Enter to exit")
