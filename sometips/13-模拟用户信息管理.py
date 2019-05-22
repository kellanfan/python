# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   13-模拟用户信息管理.py
@Time    :   2019/05/21 11:33:35
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib

import time
import sys
def print_menu():
    '''
    打印提示信息
    '''
    print("="*30)
    print("    用户信息管理系统V0.1")
    print("="*30)
    print("    1 添加用户信息")
    print("    2 修改用户信息")
    print("    3 查询用户信息")
    print("    4 删除用户信息")
    print("    5 显示用户信息")
    print("    6 退出系统")
    print("="*30)

print_menu()

user_info_list = []
while True:
    #获取用户的输入
    try:
        fun_num = int(input("请输入相关功能序号: "))
    except:
        print("请输入整数类型...")
        sys.exit(1)
    user_info = {}
    #根据用户输入执行相应的功能
    if fun_num == 1:
        print("可输入的信息有：")
        print("    1 用户名 2 性别 3 年龄 4 住址 5 QQ号 6 微信号 7 是否单身")
        user_info['name'] = input("请输入姓名： ")
        user_info['sex'] = input("请输入性别： ")
        user_info['age'] = input("请输入年龄： ")
        user_info['address'] = input("请输入地址： ")
        user_info['QQ'] = input("请输入QQ号： ")
        user_info['wechat'] = input("请输入微信号： ")
        user_info['single'] = input("是否单身？是：0 否：1   ")
        print(user_info)
        user_info_list.append(user_info)
    elif fun_num == 2:
#修改用户信息
        set_user = input("请输入要修改的用户名：")
        find_flag = 0
        for temp in user_info_list:
            if set_user == temp['name']:
                try:
                    info_num = int(input("请输入要修改的项目：1 性别 2 年龄 3 住址 4 QQ号 5 微信号 6 是否单身 ："))
                    info = input("请输入变更内容：")
                except:
                    print("没事干了么...")
                    sys.exit(2)
                if info_num == 1:
                    temp['sex'] = info
                elif info_num == 2:
                    temp['age'] = info
                elif info_num == 3:
                    temp['address'] = info
                elif info_num == 4:
                    temp['QQ'] = info
                elif info_num == 5:
                    temp['wechat'] = info
                elif info_num == 6:
                    temp['single'] = info
                else:
                    print("请输入正确信息...")
                print("用户名 \t性别 \t年龄 \t住址 \tQQ号 \t微信号 \t是否单身")
                print("%s\t%s\t%s\t%s\t%s\t%s\t%s" %(temp['name'],temp['sex'],
                                    temp['age'],temp['address'],temp['QQ'],
                                    temp['wechat'],temp['single']))
                find_flag = 1
                break
        if find_flag == 0:
            print("查无此人...")

    elif fun_num == 3:
        search = input("请输入要查询的用户名：")
        find_flag = 0
        for temp in user_info_list:
            if search == temp['name']:
                print("用户名 \t性别 \t年龄 \t住址 \tQQ号 \t微信号 \t是否单身")
                print("%s\t%s\t%s\t%s\t%s\t%s\t%s" %(temp['name'],temp['sex'],
                                    temp['age'],temp['address'],temp['QQ'],
                                    temp['wechat'],temp['single']))
                find_flag = 1
                break
        if find_flag == 0:
            print("查无此人...")
    elif fun_num == 4:
#删除账户信息
        del_user = input("请输入要删除的用户名：")
        find_flag = 0
        for temp in user_info_list:
            if del_user == temp['name']:
                print("正在删除用户名%s..." %del_user)
                user_info_list.remove(temp)
                time.sleep(1)
                find_flag = 1
                print("删除成功...")
                break
        if find_flag == 0:
            print("查无此人...")
        
    elif fun_num == 5:
        print("用户名 \t性别 \t年龄 \t住址 \tQQ号 \t微信号 \t是否单身")
        for infor in user_info_list:
            print("%s\t%s\t%s\t%s\t%s\t%s\t%s" %(infor['name'],infor['sex'],
                                    infor['age'],infor['address'],infor['QQ'],
                                    infor['wechat'],infor['single']))
    elif fun_num == 6:
        print("再见...")
        break
    else:
        print("请输入正确的序号...")
        continue
