#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 28 Mar 2019 08:45:28 AM CST

# File Name: 15-使用pyPDF2模块打开PDF文件.py
# Description:

"""
import PyPDF2
mypdf = open('lipsum.pdf','rb') #要以二进制格式打开
pdf_doc = PyPDF2.PdfFileReader(mypdf)
print("一共%d页"%pdf_doc.numPages)
#获取指定页面内容并展示
first_page = pdf_doc.getPage(6)
print(first_page.extractText())

pdf_doc_writer = PyPDF2.PdfFileWriter()
pdf_doc_writer.addPage(first_page)
out_file = open('new.pdf', 'wb')
pdf_doc_writer.write(out_file)
