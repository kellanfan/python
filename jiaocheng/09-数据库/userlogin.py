#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Fri 29 Jun 2018 10:56:30 AM CST

# File Name: userlogin.py
# Description:

"""

import sys
import hashlib
sys.path.append('/root/python/spider/misc')
import mysql_connect
import redishelper

def hash_pass(passwd):
    hash = hashlib.sha1()
    hash.update(passwd.encode('utf-8'))
    return hash.hexdigest()

def register():
    name = input("请输入用户名: ")
    passwd = input("请输入密码: ")
    passwd1 = input("请重新输入密码: ")
    if passwd == passwd1:
        pass1 = hash_pass(passwd)
        m = mysql_connect.MysqlConnect('/root/python/spider/misc/mysql_data.yaml')
        sql = "insert into user (name,password) value ('%s', '%s')"%(name, pass1)
        m.change_data('test',sql)
        print("注册完成")
    else:
        print("密码不一致")

def login():
    name = input("请输入用户名: ")
    passwd = input("请输入密码: ")
    pass1 = hash_pass(passwd)

    r = redishelper.RedisHelper()
    m = mysql_connect.MysqlConnect('/root/python/spider/misc/mysql_data.yaml')
    if r.get(name) == None:
        sql = "select password from user where name = '%s'" %(name)
        if len(m.select_data('test',sql)) == 0:
            print("无此用户，请注册")
        else:
            pass2 = m.select_data('test',sql)[0]
            if pass2[0] == pass1:
                print("成功")
                r.set(name,pass2[0])
            else:
                print("密码错误")
    else:
        if r.get(name).decode('utf-8') == pass1:
            print("成功")
        else:
            print("密码错误")
    

def main():
    flag = input("请选择的操作:0<注册>,1<登陆>")
    try:
        flag = int(flag)
    except:
        print("请输入正确序号")
        sys.exit(-1)
        
    if int(flag) in [0,1]:
        if flag == 0:
            register()
        elif flag == 1:
            login()
    else:
        print("请输入正确序号")

if __name__ == '__main__':
    main()
