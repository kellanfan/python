#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

db = MySQLdb.connect("100.128.1.254","fankai","Zhu88jie","test")
cursor = db.cursor()
def selectsql(select_sql):
  try:
    cursor.execute(select_sql)
    results = cursor.fetchall()
    for row in results:
      cust_id = row[0]
      cust_name = row[1]
      cust_address = row[2]
      cust_city = row[3]
      cust_state = row[4]
      cust_zip = row[5]
      cust_country = row[6]
      cust_contact = row[7]
      cust_email = row[8]
      print("cust_id=%s, cust_name=%s, cust_address=%s, cust_city=%s, cust_state=%s, cust_zip=%s, cust_country=%s, cust_contact=%s, cust_email=%s" % \
      (cust_id, cust_name, cust_address, cust_city, cust_state, cust_zip, cust_country, cust_contact, cust_email))
  except:
    print("Error: unable to fecth data")

def updatesql(update_sql):
  try:
    cursor.execute(update_sql)
    db.commit()
    print("Update sql Succeed!!!")
  except:
    db.rollback()
    print("Update sql Failed!!!")

def insertsql(insert_sql):
  try:
    cursor.execute(insert_sql)
    db.commit()
    print("Insert sql Succeed!!!")
  except:
    db.rollback()
    print("Insert sql Failed!!!")

def selectonesql(selectone_sql):
  try:
    cursor.execute(selectone_sql)
    data = cursor.fetchone()
    print("%s" % data)
  except:
    print("Error: unable to fecth data")
def showcolumns(showcolumns_sql):
  try:
    cursor.execute(showcolumns_sql)
    data = cursor.fetchone()
    print("columns=%s" % data)
  except:
    print("Error: unable to fecth data")
     
selectone_sql = "SELECT VERSION()"
select_sql = "SELECT * FROM customers"
update_sql = "update customers set cust_zip = '55555' where cust_id = 10001"
sql = "select count(*) from information_schema.columns where table_schema='test' and table_name='orderitems'"
showcolumns(sql)
db.close()
