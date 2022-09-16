line=input('please input the number of line:')
line=int(line)  # 输入行数
number=2*line-1 # 数据总数
data=[0]*(number)   # 数据初值
j=line-1    # 选取中间的值
data[j]=1
printline=1 # 初值
while printline<=line:
    i=0
    while i<=number-1:
        if data[i]==1:
            print('*',end="")
        if data[i]==0:
            print(' ',end="")
        i=i+1
    # print(data)    # 检验数据
    print() # 输出当前行的*号
    printline=printline+1
    if printline>line:
        break   # 判断是否结束，防止数据溢出
    i=j-printline+1
    while i<=(j-1+printline):
        data[i]=data[i]+(-1)**(data[i])
        i=i+1   # 下一行数据变换处理




