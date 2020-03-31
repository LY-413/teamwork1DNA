# 姓名：高艺特、胡流云、张志杰、刘光波、顾鹏程
# Python程序设计
# Teamwork1: DNA分析

#这个程序读取DNA测序器的输出并计算统计数据，比如GC的含量。
#从如下命令行运行：python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# sys模块支持读取文件、命令行参数等。
import sys


###########################################################################
### 将核苷酸读入一个名为seq的变量中
###

# 需要指定文件名
if len(sys.argv) < 2:
    print( "运行此程序时，必须提供一个文件名作为参数。")
    sys.exit(2)
# 在命令行上指定的文件名，作为字符串。
filename = sys.argv[1]
# 可以从中读取数据的文件对象。
inputfile = open(filename)

# 输入文件中迄今为止已读取的所有核苷酸。
seq = ""
# 当前行号（=到目前为止读取的行数）。
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # 如果我们在2，6，10行
    if linenum % 4 == 2:
        # 从行尾删除换行符
        line = line.rstrip()
        seq = seq + line


###########################################################################
### 计算统计
###

# 迄今为止发现的总核苷酸。
total_count = 0
# G和C核苷酸的数量。
gc_count = 0
#A和T核苷酸的数量。
at_count = 0
#A,T,C,G的数量分别是。
AN = 0
TN = 0
CN = 0
GN = 0

# 对于字符串中的每个碱基（bp），
for bp in seq:
    # 增加我们看到的碱基总数
    total_count = total_count + 1

    # 接下来，如果bp是G或C，
    if bp == 'C' or bp == 'G':
        # 增加bp的计数
        gc_count = gc_count + 1
    #接下来，如果bp是A或T，
    if bp == 'A' or bp == 'T':
        at_count = at_count + 1
    #分别计数A,T,C,G:
    if bp=='A' :
        AN = AN + 1
    if bp == 'T':
        TN = TN + 1
    if bp == 'C':
        CN = CN + 1
    if bp == 'G':
        GN = GN + 1


# 用GC碱基总计数gc_count 除以总计数sum count
gc_content = float(gc_count) / (AN+TN+GN+CN)
at_content = float(at_count)/(AN+TN+GN+CN)

#用气相色谱含量进行微生物分类
if gc_content > 0.6:
    kind = "气相色谱含量高（high）"
elif gc_content <= 0.6 and gc_content >=0.4 :
    kind ="中等GC含量（medium）"
else:
    kind ="气相色谱含量低（low）"

# 打印答案
print ('GC-content:', gc_content)
print('AT-content:',at_content)
print('G count:',GN)
print('C count:',CN)
print('A count:',AN)
print('T count:',TN)
print('Sum count:',AN+TN+GN+CN)
print('Total count:',total_count)
print('seq length:',len(seq))
print('AT/CG Ratio:',(AN+TN)/(CN+GN))
print('GC Classification:',kind)