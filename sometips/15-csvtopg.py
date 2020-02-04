# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   15-csvtopg.py
@Time    :   2020/02/04 10:29:27
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   csv文件数据写到postgresql的通用脚本
'''

# here put the import lib
import os
import psycopg2
import pandas as pd

def create_table(filename,headers,header_types):
    sql = 'CREATE TABLE IF NOT EXISTS table_{}('.format(filename)
    columns_list = []
    for header in headers:
        if header_types[header] == 'int':
            part = header + ' INT'
        elif header_types[header] == 'float':
            part = header + ' FLOAT'
        elif header_types[header] == 'datetime64':
            part = header + ' DATE'
        else:
            part = header + ' VARCHAR(300)'
        columns_list.append(part)
    columns = ','.join(columns_list)
    sql = sql + columns + ')'
    return sql

def create_insert_sql(filename, column_head):
    s_str = ','.join(['%s'] * len(column_head))
    sql = 'INSERT INTO table_{}({}) VALUES ({})'.format(filename, ','.join(column_head), s_str)
    return sql

def get_file_data(file):
    try:
        if file.endswith('.csv'):
            data = pd.read_csv(file,encoding='gbk')
        elif file.endswith('.xls') or file.endswith('.xlsx'):
            data = pd.read_excel(file)
        else:
            data = None
    except Exception as e:
        print('Read data from file [{0}] failed: [{1}]'.format(file, e))
        data = None
    return data
    
def main():
    # connect to pg
    try:
        pg_conn = psycopg2.connect(database='csv',user='spiderman',password='Sun55kong',host='192.168.1.2')
        cursor = pg_conn.cursor()
        print('Connect to postgresql successfully')
    except Exception as e:
        print('Connetc to postgresql failed：{}'.format(e)) 
    # traverse folder
    for file in os.listdir(os.getcwd()):
        data = get_file_data(file)
        if data is not None:
            # define filename and header
            filename = file.split('.')[0]
            column_head = data.columns.tolist()
            # get create table sql
            create_table_sql = create_table(filename, column_head, data.dtypes)
            # create table
            try:
                cursor.execute(create_table_sql)
                pg_conn.commit()
                print('Create table [table_{}] successfully'.format(filename))
            except Exception as e:
                print('Create table [table_{0}] failed: [{1}]'.format(filename, e))
            # get insert data sql
            insert_sql = create_insert_sql(filename, column_head)
            # insert data
            try:
                cursor.executemany(insert_sql, data.values.tolist())
                pg_conn.commit()
                print('Insert data successfully.')  
            except Exception as e:
                print('Insert data failed: [{}]'.format(e))
    
    cursor.close()
    pg_conn.close()

if __name__ == "__main__":
    main()