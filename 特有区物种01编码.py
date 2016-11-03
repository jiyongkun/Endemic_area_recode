# -*- coding: cp936 -*-
import csv

#�Զ���һ������������Idת���ɵ���ĸ����λ����Id�ĺ���, ��A02
def id_trans(id_num, rows_num):#rows_numΪ���򷽸���
    num = id_num%rows_num + 1
    character = chr(id_num/rows_num + 65)
    if num < 10:
        num_char = '0' + str(num)
    else:
        num_char = str(num)
    return character + num_char 

#�Զ���һ�����������������б�ת����01���еĺ���#
#0�������� 1������    
def recode(species,species_list):#speciesΪĳ�����������������б�;species_listΪ���������б�
    #��ʼ��һ��ȫ��0���ַ����б�#
    code_num = [] 
    for i in species_list:
        code_num.append('0')
    #���б��к��е����ֱ�Ϊ1#
    for i in species:
        code_num[species_list.index(i)] = '1'
    return code_num #����һ��01���е��б�
    
    
print '������Ҫת����csv�ļ�����'
file_in_csv = csv.reader(open(raw_input(),'rb')) #�Զ�����ģʽ��
file_out = open('output.csv','wb') #�Զ�����ģʽд��
file_in = []
#����һ�����������ļ����ݵĶ�ά�б�#
for row in file_in_csv:
    file_in.append(row)
    
print '��������򷽸�����'
rows_num = int(raw_input())

print '����������...'

#��ȡ�����������ֵ��б�#
species_list = [] #�����б�
for one_line in file_in[1:]:#�ӵڶ��п�ʼ��ȡ
    species_name = one_line[1].strip()
    if species_name not in species_list and species_name != '':
        species_list.append(species_name)
csv_out = csv.writer(file_out)
csv_out.writerow(['species'] + species_list)
#print species_list

#����ÿ����������������ֵ�#        
box_species = {} #ÿ����������������б��ֵ䣬{box_id: [����1,����2,...],...} 
for one_line in file_in[1:]:
    species_name = one_line[1].strip()
    if one_line[2] != '' and species_name != '':
        box_id = id_trans(int(one_line[2].strip()), rows_num) #����ĸ����λ���ֵķ���id
        box_species.setdefault(box_id,[]).append(species_name)

#�ֵ����#
for box_id in box_species:
    box_seq = recode(box_species[box_id],species_list)
    file_out.write(box_id + ',' + ','.join(box_seq) + '\n')    
    
file_out.close()
print '������ϣ�ת������ļ��ѱ�����output.csv\n��ĸ�������ᣬ���ִ������\nA01�������½ǵ�һ������\n�밴�س����˳�'
raw_input()


