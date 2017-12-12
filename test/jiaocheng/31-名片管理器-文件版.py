#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 06 Dec 2017 11:33:07 AM CST

# File Name: 31-名片管理器-文件版.py
# Description:

"""
import sys
#全局变量，存储信息
card_info = []

def print_menu():
    '''打印提示信息'''
    print "="*30
    print "    名片管理系统V0.1"
    print "="*30
    print "    1 添加信息"
    print "    2 修改信息"
    print "    3 查询信息"
    print "    4 删除信息"
    print "    5 显示信息"
    print "    6 保存信息"
    print "    7 退出系统"
    print "="*30

def add_info():
    new_info = {}
    print "请输入相关信息："
    new_info['name'] = raw_input("1.姓名：")
    new_info['company'] = raw_input("2.公司：")
    new_info['address'] = raw_input("3.地址：")
    new_info['phone'] = raw_input("4.电话：")
    
    global  card_info
    card_info.append(new_info)

def exit_system():
    print "再见！"
    sys.exit(0)

def save_info():
    try:
        f = open("back.data",'w')
        f.write(str(card_info))
        f.close()
        print "保存成功！"
    except:
        print "保存失败！"

def sort_info(card_info):
    print "姓名\t公司\t地址\t电话"
    for info in card_info:
        print "%s\t%s\t%s\t%s" %(info['name'],info['company'],info['address'],info['phone'])

def open_read():
    try:
        f = open("back.data")
        return eval(f.read())
        f.close()
    except:
        print "打开读取失败！"

def show_info():
    try:
        global  card_info
        sort_info(open_read())
    except:
        print "显示失败！"

def del_info():
    try:
        global  card_info
        card_info = open_read()
        del_name = raw_input("您要删除的名字：")
        sign = False
        for info in card_info:
            if info['name'] == del_name:
                card_info.remove(info)
                print "删除%s成功，请重新保存数据"%del_name
                sign = True
        if sign == False:
            print "没有%s的信息"%del_name
    except:
        print "删除失败！"

def search_info():
    try:
        global  card_info
        card_info = open_read()
        search_info = raw_input("您要查找的名字：")
        print "姓名\t公司\t地址\t电话"
        for info in card_info:
            if info['name'] == search_info:
                print "%s\t%s\t%s\t%s" %(info['name'],info['company'],info['address'],info['phone'])
    except:
        print "查询失败！"
                

def main():
    print_menu()
    while True:
        num = int(input("请输入操作序号："))
        if num == 1:
            add_info()
        if num == 2:
            pass
        if num == 3:
            search_info()
        if num == 4:
            del_info()
        if num == 5:
            show_info()
        if num == 6:
            save_info()
        if num == 7:
            exit_system()

if __name__ == '__main__':
    main()
