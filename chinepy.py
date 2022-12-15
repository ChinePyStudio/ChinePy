"""

ChinePy版本：1.2.8
版权：飞皮哥（Feipi) & ChinePyStudio
是否有Bug：没用，并等待反馈中
开源网站：GitHub

本语言完全免费！

"""

# define
import number

num_all = {}
print("本语言完全免费！")
VERSION = "1.3.1 - DEFAULT"

# Compile area
class Compile():
    def __init__(self, mode = 0):
        if mode == 0:
            self.log("加载完成，版本" + VERSION)
    def log(self,things, mode = 0):
        if mode == 0:
            print("[ChinePy控制台 - 日志反馈]" + things)
        if mode == 1:
            print("[ChinePy控制台 - 警告]" + things + "| 操作失误会导致问题 请留意警告信息")
        if mode == 2:
            print("[ChinePy控制台 - Error] 报错反馈：" + things)
    # 变量定义
    def numer(self, name, value):
        num_all[name] = value
        print("成功")
        return 1

    # 打印功能
    def print(self, things, numer=False):
        print(things)
        return True

    # 讲指令（说指令）
    def talk(self, things, you, who='all'):
        print(you, '说', things, '给', who)
        return True

    # 彩蛋
    def jntm(self):
        print('你干嘛')
        return True

    # 反向解释（说）
    def ls(self, fal, thing, who1, who2):
        print(fal, "给", who1, "和", who2, "说：", thing)


# API接口 - PeopleNumber
'''
关于这个API接口，许多人认为不可以诞生在ChinePy内，但此接口象征这ChinePy支持综合模块汉化API支持。对以后的模块汉化打好了基础
安全风险：无
版权：有
是否付费：无需
'''


# 定义类
# 初始化 - 参数NUM为身份证号
class NumberAPI:
    # init 初始化接口
    def __init__(self, num):
        self.num = num
        self.father = Compile(mode = 1)
        self.log("身份证API加载完成")
    # 日志输出器
    def log(self,things,mode = 0):
        if mode == 0:
            print("[API接口反馈]" + things)
        if mode == 1:
            print("[API接口警告]" + things + "| 操作失误会导致问题 请留意警告信息")

    def creatAPI(self):
        self.api = number.NumBerUse(self.num, True)
    def creatPackage(self):
        self.pkg = number.Jicheng
    def sex(self):
        num_sex = self.api.sex()
        self.log("对方性别为" + num_sex)
    def age(self):
        num_age = self.api.showage()
        self.log("对方年龄为" + str(num_age))
    def loc(self):
        loc = self.api.city_load()
        self.log("对方所属地区" + loc)


'''
运行部分
负责调用命令
同时可以在其他的对ChinePyAPI接口的程序进行调用（后期推出ChinePyAPI版本开源）
'''
# run
bin = Compile()
while True:
    try:
        commond = input("[Command Input System]>>>")
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

        if "创建接口" in commond:
            cmd = commond.split(" ")
            if cmd[1] == "PeopleNumber":
                pnAPI = NumberAPI(input("请输入身份证号："))
                pnAPI.creatAPI()
        if "PeopleNumber" in commond:
            cmd = commond.split(" ")
            if cmd[1] == "查看地区":
                pnAPI.loc()
            if cmd[1] == "查看年龄":
                pnAPI.age()
            if cmd[1] == "查看性别":
                pnAPI.sex()

        else:
            bin.log("未知命令", 2)
    except BaseException as e:
        bin.log("语法错误:"+str(e), 2)
