"""
    作者：zqc
    功能：判断密码强度
    版本：v3.0
    日期：2019/07/24
    3.0新增功能: 保存密码及强度到文件中.
"""

def check_number_exist(password_str):
    """
        判断字符中是否包含数字
    """
    has_number = False

    for c in password_str:
        if c.isnumeric():
            has_number = True
            break

    return has_number

def check_letter_exist(password_str):
    """
        判断字符中是否包含字母
    """
    has_letter = False

    for c in password_str:
        if c.isalpha():
            has_letter = True
            break
    return has_letter


def main():
    """
        主函数
    """
    ##设定潮湿登录此时
    try_times = 5

    while try_times >= 0:

        #前台输入的密码
        password = input("请输入密码:")

        #配置密码级别
        strength_level = 0

        #规则1：密码长度大于8

        if len(password) >= 8:
            strength_level += 1
        else:
            print('密码长度要求至少8位!')

        #规则2:包含数字
        if check_number_exist(password):
            strength_level += 1
        else:
            print('密码要求包含数字！')

        #规则3:包含字母
        if check_letter_exist(password):
            strength_level += 1
        else:
            print('密码要求包含字母！')


        f = open('password.txt', 'a')
        f.write('密码:{},强度:{}\n'.format(password,strength_level))
        f.close()

        #结果，判断密码强度是否合适。
        if strength_level == 3:
            print('恭喜!,密码强度合格！')
            break
        else:
            print('抱歉，密码强度不合格！')
            try_times -= 1

        print("<----------------------->")



    if try_times <= 0:
        print("尝试次数过多,密码设置失败!!!!")

if __name__ == "__main__":
    main()