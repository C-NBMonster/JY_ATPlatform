#coding:utf-8
import os,re
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
def del_files(path,filename):
        for root,dirs,files in os.walk(path):#（使用 os.walk ,这个方法返回的是一个三元tupple(dirpath(string), dirnames(list), filenames(list)), 其中第一个为起始路径， 第二个为起始路径下的文件夹, 第三个是起始路径下的文件.）
                for name in files:
                    if filename in name:#判断某一字符串是否具有某一字串，可以使用in语句
                        os.remove(os.path.join(root,name))##os.move语句为删除文件语句
# pdf_list = os.listdir("../ccc2")
# ww=[]
# for temp in pdf_list:
#     print(re.sub("\D", "", temp))
#     ww.append(re.sub("\D", "",temp))
# print(ww)
# for t in os.listdir("../ccc2/"+temp):
#     print(t)
#     if re.findall('证据7',t):
#         os.rename("../ccc/"+temp+"/"+t,"../ccc/"+temp+"/"+'证据7：挖财到达飞放款回单'+'.pdf')
#     if re.findall('证据8',t):
#         os.rename("../ccc/"+temp+"/"+t,"../ccc/"+temp+"/"+'证据8：达飞到挖财代偿回单'+'.pdf')
#     if re.findall('证据10',t):
#         os.rename("../ccc/"+temp+"/"+t,"../ccc/"+temp+"/"+'证据10：达飞VS挖财网合作协议'+'.pdf')
#     print(t)
#
# for t in os.listdir("../ccc2/"+temp):
#     print(t)
#     if re.findall('证据7',t):
#         os.rename("../ccc/"+temp+"/"+t,"../ccc/"+temp+"/"+'证据7：挖财到达飞放款回单'+'.pdf')
#     if re.findall('证据8',t):
#         os.rename("../ccc/"+temp+"/"+t,"../ccc/"+temp+"/"+'证据8：达飞到挖财代偿回单'+'.pdf')
#     if re.findall('证据10',t):
#         os.rename("../ccc/"+temp+"/"+t,"../ccc/"+temp+"/"+'证据10：达飞VS挖财网合作协议'+'.pdf')
#     print(t)
path=PATH("..\ccc4")
pdf_list = os.listdir("../ccc4")
for temp in pdf_list:
    for t in os.listdir("../ccc4/"+temp):
        print(t)
        if re.findall('证据1：',t) or re.findall('证据2：',t) or re.findall('证据3：',t) or re.findall('证据4：',t) or re.findall('证据12：',t) or re.findall('身份证',t):
            del_files(path,t)
        #     os.rename("../ccc2/"+temp+"/"+t,"../ccc2/"+temp+"/"+'证据7：挖财到达飞放款回单'+'.pdf')
        # if re.findall('证据8',t):
        #     os.rename("../ccc2/"+temp+"/"+t,"../ccc2/"+temp+"/"+'证据8：达飞到挖财代偿回单'+'.pdf')
        # if re.findall('证据10',t):
        #     os.rename("../ccc2/"+temp+"/"+t,"../ccc2/"+temp+"/"+'证据10：达飞VS挖财网合作协议'+'.pdf')
        # print(t)