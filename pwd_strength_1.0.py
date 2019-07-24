"""
    作者：zqc
    功能：判断密码强度
    版本：v1.0
    日期：2019/05/17
"""

def check_number_exist(password_str):
    """
        判断字符中是否包含数字
    """
    for c in password_str:
        pwd_strength_1
        .0.py        if c.isnumeric():
            return True
    return False

def check_letter_exist(password_str):
    """
        判断字符中是否包含字母
    """
    for c in password_str:
        if c.isalpha():
            return True
    return False


def main():
    """
        主函数
    """
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


    #结果，判断密码强度是否合适。
    if strength_level == 3:
        print('恭喜!,密码强度合格！')
    else:
        print('抱歉，密码强度不合格！')


if __name__ == "__main__":
    main()