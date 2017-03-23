import re

# 读取文件
def read_file(x):

    f = open("dda.log","r")
    i = 1
    d = {}
    l = []
    n = {}
    for line in f:
        read_line(line,d,l)
        # if i > 100:
        #     break
        # i = i + 1



    # filter_access_num(d,x,n,l)

    print(len(l))
    pass

# 读取行
def read_line(line,d,l):

    # match = re.findall("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", line)
    match = re.findall('\s{1}[0-9]{1,9}\s{1}\"{1}', line)
    # print(match)
    # d.setdefault(match[0],0)
    # d[match[0]] = d[match[0]] + 1
    sizeMatch = re.findall('[0-9]{1,9}',match[0])
    a = int(sizeMatch[0])

    if a > 300*1024:
        l.append(a)
        # print(a)

#过滤访问数
def filter_access_num(d,x,n,l):
    # for key in d:
    #     if d[key] > x:
    #         n[key] = d[key]


    pass

read_file(500)