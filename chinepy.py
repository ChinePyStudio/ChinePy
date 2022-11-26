'''

ChinePy版本：1.2.8
版权：飞皮哥（Feipi) & ChinePyStudio
是否有Bug：没用，并等待反馈中
开源网站：GitHub

本语言完全免费！

'''

#define
num_all = {}
print("本语言完全免费！")

#Compile area
class Compile():
    #变量定义
    def numer(self, name, value):
        num_all[name] = value
        print("成功")
        return 1
    #打印功能
    def print(self,things,numer = False):
        print(things)
        return True
    #讲指令（说指令）
    def talk(self,things,you,who = 'all'):
        print(you,'说',things,'给',who)
        return True
    #彩蛋
    def jntm(self):
        print('你干嘛')
        return True
    #退出功能
    def quite(self):
        quit()
    #报错功能
    def fail(self, case = '000x'):
        if case == '000x':
            print('没有发现错误')
            return False
        if case == '078x13':
            print('没有发现指定代码，或语法错误')
            return True
        if case == '889x032':
            print('程序错误，暂时无法运行')
            return True
        else:
            print('nothing to found')
            return True
    #错误检测（没用）
    def fail_q(self, num):
        if self.fail(num):
            return "有错误"
        else:
            return "没有错误"
    #反向解释（说）
    def ls(self,fal,thing,who1,who2):
        print(fal,"给", who1, "和", who2, "说：", thing)

#run
bin = Compile()
while True:
    try:
        commond = input()
        m = commond.split(' ')
        if m[0] == "变量":
            com = commond.split(' ')
            if com[1] == "整型":
                com[3] = int(com[3])
                bin.numer(com[2], com[3])
            elif com[1] == "浮点型":
                com[3] = float(com[3])
                bin.numer(com[2], com[3])
            elif com[1] == "表达型":
                com[3] = bool(com[3])
                bin.numer(com[2], com[3])
            else:
                bin.numer(com[2], com[3])
            continue
        if "打印" in commond:
            thing = commond.split(' ')
            if thing[1] == "变量":
                csa = thing[2]
                t2 = num_all[csa]
                bin.print(t2)
            else:
                bin.print(thing[1])
            continue
        if "说" in commond:
            meed = commond.split(' ')
            you = meed[0]
            thing = meed[2]
            who = meed[3]
            bin.talk(thing, you, who)
            continue
        if commond == '鸡你太美':
            bin.jntm()
            continue
        if commond == '退出':
            break
        if commond == '错误检测':
            fail_list = commond.split(' ')
            print(bin.fail_q(fail_list[1]))
        if "讲" in commond:
            ltalk = commond.split(" ")
            bin.ls(ltalk[0], ltalk[4], ltalk[2], ltalk[3])

        else:
            bin.fail('078x13')
    except: 
        bin.fail('078x13')
        break
