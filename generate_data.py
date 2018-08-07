'''
生成训练数据
'''
import os
import string

#所有数字和大小写字母
CHARSET = string.digits + string.ascii_letters
CHARDICT = {}
for index, char in enumerate(CHARSET):
    CHARDICT[char] = index

import logger as main_logger
import logging
logger = logging.getLevelName('verifycode.parsecode')

def gen_files(source_path='./files/test', extend=''):
    '''
    生成器，获取指定目录下的指定文件
    source_path： 读取目录
    extend： 指定后缀的文件
    return： name 文件名， file 文件绝对路径
    '''
    result = os.walk(source_path)
    path, dirs, files = next(result)
    path = os.path.abspath(path)
    for file in files:
        name, ext = os.path.splitext(file)
        if not extend or ext == extend:
            file_path = os.path.join(path, file)
            yield name, file_path

def quantize_str(code, charDict=CHARDICT):
    '''
    把字符串数值化
    code: 要转换的字符串
    charDict: 字符映射表
    eg， 当 charDict = [0, 1, ..., 9]：
        quantize_str('123', charDict) = [
                        [0, 1, 0, 0, 0， 0， 0， 0， 0， 0]，
                        [0, 0, 1, 0, 0， 0， 0， 0， 0， 0]，
                        [0, 0, 0, 1, 0， 0， 0， 0， 0， 0]，
                    ]
    '''
    char_len = len(charDict.keys())
    result = []
    for char in code:
        char_list = [0]*char_len
        index = charDict[char]
        char_list[index] = 1
        result.append(result)
    return result

