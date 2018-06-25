import re

print('请输入密码： ', end="")
password = input()
if len(password) < 8:
    print('长度不够8位')
    exit(1)
regrx = re.compile(r'[A-Z]')
mo = regrx.search(password)
if mo:
    regrx = re.compile(r'[a-z]')
    mo = regrx.search(password)
    if mo:
        regrx = re.compile(r'\d+')
        mo = regrx.search(password)
        if mo:
            print('设置成功')
        else:
            print('没有数字')
    else:
        print('没有小写字母')
else:
    print("没有大写字母")