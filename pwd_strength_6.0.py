"""
    作者：zqc
    功能：判断密码强度
    版本：v4.0
    日期：2019/08/05
    3.0新增功能: 保存密码及强度到文件中.
    4.0新增功能: 读取文件.
    5.0新增功能：定义一个password工具类
    6.0新增功能：定义一个文件工具类
"""


##类的定义
class PasswordTool:
    """
        密码工具类
    """

    # 初始化方法
    def __init__(self, password):  # 初始化
        # 类属性
        self.password = password
        self.strength_level = 0

    def process_password(self):
        # 规则1：密码长度大于8

        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('密码长度要求至少8位!')

        # 规则2:包含数字
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print('密码要求包含数字！')

        # 规则3:包含字母
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print('密码要求包含字母！')

    # 类方法
    def check_number_exist(self):
        """
            判断字符中是否包含数字
        """
        has_number = False

        for c in self.password:
            if c.isnumeric():
                has_number = True
                break

        return has_number

    def check_letter_exist(self):
        """
            判断字符中是否包含字母
        """
        has_letter = False

        for c in self.password:
            if c.isalpha():
                has_letter = True
                break
        return has_letter


class FileTool:
    """
        文件工具类
    """

    def __init__(self,filepath):
        self.filepath = filepath

    def writ_to_file(self, line):
        f = open(self.filepath, 'a')
        f.write(line)
        f.close()

    def read_from_file(self):
        f = open(self.filepath, 'r')
        lines = f.readlines()
        f.close()
        return lines

def main():
    """
        主函数
    """
    ##设定潮湿登录此时
    try_times = 5

    filepath = 'password_6.0.txt'
    ##实例化文件工具对象
    file_tool = FileTool(filepath)

    while try_times >= 0:

        # 前台输入的密码
        password = input("请输入密码:")

        ##类的调用
        ##实例化调用密码工具
        password_tool = PasswordTool(password)
        password_tool.process_password()


        line = '密码:{},强度:{}\n'.format(password, password_tool.strength_level)

        #写操作
        file_tool.writ_to_file(line)

        # 结果，判断密码强度是否合适。
        if password_tool.strength_level == 3:
            print('恭喜!,密码强度合格！')
            break
        else:
            print('抱歉，密码强度不合格！')
            try_times -= 1

        print("<----------------------->")

    if try_times <= 0:
        print("尝试次数过多,密码设置失败!!!!")

    #读操作
    lines = file_tool.read_from_file()
    print(lines)


    # 读取文件
    # f = open('password.txt','r')

    # 1.read()
    # context = f.read()
    # print(context)

    # 2.readline()
    # line = f.readline()
    # print(line)
    # line = f.readline()
    # print(line)
    # for line in f:
    #     print(line)

    # 3.readlines
    # lines =  f.readlines() #列表
    # print(lines)

    # for line in f.readlines():
    #     print('read:{}'.format(line))
    #
    # f.close()

if __name__ == "__main__":
    main()
