# -*- coding: cp936 -*-
import csv

#自定义一个将方格数字Id转换成单字母加两位数字Id的函数, 如A02
def id_trans(id_num, rows_num):#rows_num为横向方格数
    num = id_num%rows_num + 1
    character = chr(id_num/rows_num + 65)
    if num < 10:
        num_char = '0' + str(num)
    else:
        num_char = str(num)
    return character + num_char 

#自定义一个将方格所含物种列表转换成01序列的函数#
#0：不存在 1：存在    
def recode(species,species_list):#species为某个方格所含的物种列表;species_list为所有物种列表
    #初始化一个全是0的字符串列表#
    code_num = [] 
    for i in species_list:
        code_num.append('0')
    #将列表中含有的物种标为1#
    for i in species:
        code_num[species_list.index(i)] = '1'
    return code_num #返回一个01序列的列表
    
    
print '请输入要转换的csv文件名：'
file_in_csv = csv.reader(open(raw_input(),'rb')) #以二进制模式打开
file_out = open('output.csv','wb') #以二进制模式写入
file_in = []
#构造一个包含输入文件数据的二维列表#
for row in file_in_csv:
    file_in.append(row)
    
print '请输入横向方格数：'
rows_num = int(raw_input())

print '正在运行中...'

#获取包含所有物种的列表#
species_list = [] #物种列表
for one_line in file_in[1:]:#从第二行开始读取
    species_name = one_line[1].strip()
    if species_name not in species_list and species_name != '':
        species_list.append(species_name)
csv_out = csv.writer(file_out)
csv_out.writerow(['species'] + species_list)
#print species_list

#生成每个方格包含的物种字典#        
box_species = {} #每个方格包含的物种列表字典，{box_id: [物种1,物种2,...],...} 
for one_line in file_in[1:]:
    species_name = one_line[1].strip()
    if one_line[2] != '' and species_name != '':
        box_id = id_trans(int(one_line[2].strip()), rows_num) #单字母加两位数字的方格id
        box_species.setdefault(box_id,[]).append(species_name)

#字典遍历#
for box_id in box_species:
    box_seq = recode(box_species[box_id],species_list)
    file_out.write(box_id + ',' + ','.join(box_seq) + '\n')    
    
file_out.close()
print '运行完毕，转换结果文件已保存至output.csv\n字母代表纵轴，数字代表横轴\nA01代表左下角第一个方格\n请按回车键退出'
raw_input()


