#!/usr/bin/env python
# coding:utf-8
# Examples for file operations

urls = [
    'www.baidu.com',
    'www.sina.com.cn',
    'www.163.com',
    'www.google.com',
    'www.nxmup.com',
]

with open('test_file.txt', 'w', encoding='utf-8') as f:
    for url in urls:
        f.writelines(url + '\n')

with open('test_file.txt', 'r') as f:
    for line in f.readlines():
        print('previous line: ', line.encode('utf-8'))
        line = line.strip('\n')
        print('remove \\n line: ', line.encode('utf-8'))
        print()
