import os
import random
import string
import subprocess
from captcha.image import ImageCaptcha

import logger as main_logger
import logging
logger = logging.getLogger('verifycode.creater')

CHARSET = string.digits+string.ascii_letters

def create_verifycode(source_str='1234', output_path='./files/test', fonts=None):
    '''
    根据字符串生成验证码
    source_str： 需要生成的字符串
    output_path： 验证码图片保存路径
    fonts： 字体格式
    '''
    output_file = os.path.join(output_path, source_str+'.png')
    fonts = fonts or get_fonts()
    image = ImageCaptcha(fonts=fonts)
    logger.debug(os.path.abspath(output_file)) ###
    image.write(source_str, output_file)
    

def get_fonts(fonts_path='/usr/share/fonts/'):
    '''
    获取指定目录下的字体文件列表
    fonts_path: 字体目录路径， 默认ubuntu系统字体
    '''
    fonts = []
    p = subprocess.Popen('find {} -name *.ttf | grep tlwg | grep .ttf'.format(fonts_path), shell=True, stdout=subprocess.PIPE)
    p.wait()
    result_lines = p.stdout.readlines()
    for line in result_lines:
        line = line.strip().decode()
        logger.debug(line) ###
        fonts.append(line)
    return fonts


def random_str(len=4, charSet=CHARSET):
    '''
    len: 生成字符串长度
    charSet: 字符集， 默认所有数字和字母
    '''
    out_str = ''
    for i in range(len):
        out_str += random.choice(charSet)
    #logger.debug(out_str) ###
    return out_str

def batch_create(num, output_path='./files/test', len=4, charSet=CHARSET, fonts=None):
    fonts = fonts or get_fonts()
    for i in range(num):
        code_str = random_str(len, charSet)
        create_verifycode(code_str, output_path, fonts)
    

if __name__ == '__main__':
    #get_fonts()
    #create_verifycode(random_str())
    #random_str()
    batch_create(10)