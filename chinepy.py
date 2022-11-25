#define
num_all = {}

#Compile area
class Compile():
    def numer(self,name, value):
        num_all[name] = value
        return 1
    def print(self,things):
        print(things)
        return True
    def talk(self,things,you,who = 'all'):
        print(you,'说',things,'给',who)
        return True
    def jntm(self):
        print('你干嘛')
        return True
    def quit(self,pack=None):
        return 'quit'
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
    def fail_q(self, num):
        if self.fail(num):
            return "有错误"
        else:
            return "没有错误"
    def ls(self,fal,thing,who1,who2):
        print(fal,"给", who1, "和", who2, "说：", thing)

#run
bin = Compile()
while True:
    try:
        commond = input()
        if "变量" in commond:
            com = commond.split(' ')
            if com[0] == "整型":
                com[0] = int(com[0])
            elif com[0] == "浮点型":
                com[0] = float(com[0])
            elif com[0] == "表达型":
                com[0] = bool(com[0])
            bin.numer(com[0])
        if "打印" in commond:
            thing = commond.split(' ')
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
            if bin.quit() == 'quit':
                break
        if commond == '错误检测':
            fail_list = commond.split(' ')
            print(bin.fail_q(fail_list[1]))
        if "讲" in commond:
            ltalk = commond.split(" ")
            bin.ls(ltalk[0], ltalk[4], ltalk[2], ltalk[3])

        else:
            bin.fail('078x13')
    except: bin.fail('078x13')
