#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 03 Aug 2017 07:44:05 PM CST

# File Name: login-test.py
# Description: 模拟使用MD5加密密码，用户登陆

"""

import hashlib
import json

def input_info():
    username = raw_input("please input your username: ")
    password = raw_input("please input your password: ")
    return username, password

def save_data(db):
    try:
        l = read_data()
        with open('db.json', 'w') as f:
            l.append(db)
            json.dump(l, f)
    except IOError:
        print "save data failed..."
    finally:
        f.close()

def read_data():
    try:
        with open('db.json', 'r') as f:
            content = json.load(f)
        f.close()
        return content
    except:
        content = []
        return content

def get_user_list():
    datalist = read_data()
    had_usernamelist = []
    for data in datalist:
        had_username = data.keys()
        had_usernamelist.append(had_username)
    return had_usernamelist


def register(username, password):
    print "Welcome to my system, please register~~~"
    check_password = raw_input("please input your password again to ensure it. Your password: ")
    while True:
        if password != check_password:
            print "password do not accordance, please input again!"
            check_password = raw_input("please input your password again to ensure it. Your password: ")
        else:
            break
    db = {}
    db[username] = calc_md5(username + password + 'kellan-salt')
    save_data(db)
    
def calc_md5(string):
    md5 = hashlib.md5()
    md5.update(string)
    return md5.hexdigest()

def login(username, password):
    print "welcome to my system! Please login..."
    had_username = get_user_list()
    data = read_data()
    users_dict = {}
    for users_dic in data:
        users_dict = dict(users_dict, **users_dic)
    userNameList = []
    for user in had_username:
        userNameList.append(user[0])
    if username in userNameList:
        md5_pass = calc_md5(username + password + 'kellan-salt')
        for i in range(5):
            if users_dict[username] == md5_pass:
                print "login successful! have fun!!!"
                break
            else:
                print "Password is ERROR!!! Please try again!"
                continue
    else:
        print "NOT has the user, please register!!!"


if __name__ == '__main__':
    choose = raw_input("Please choose login[0] or register[1]: ")
    if choose == 'login' or choose == '0':
        (username, password) = input_info()
        login(username, password)
    elif choose == 'register' or choose == '1':
        (username, password) = input_info()
        register(username, password)
