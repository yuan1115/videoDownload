# -*- coding: utf-8 -*-
# @Author: jmx
# @Date:   2019-01-22 18:18:40
# @Last Modified by:   jmx
# @Last Modified time: 2019-01-23 17:05:54
import os
import time


def log(logfile, str, isPrint=0):
    '''日志创建
    Arguments:
        str {str} -- 异常描述

    Keyword Arguments:
        isPrint {number} -- 是否打印异常 (default: {0})
    '''
    [path, file] = os.path.split(logfile)
    if os.path.exists(path) == False:
        os.mkdir(path)
    if os.path.exists(logfile) == False:
        open(logfile, 'w').close()
    f = open(logfile).read()
    creater_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    log = '%s %s : %s \n' % (f, creater_time, str)
    open(logfile, 'w').write(log)
    if isPrint == 1:
        tips(str)


def tips(str):
    '''提示
    Arguments:
        str {str} -- [description]
    '''
    print('*'.center(40+len(str), '*'))
    print(str.center(40, ' '))
    print('*'.center(40+len(str), '*'))


def isDone(downFile, url, types='r'):
    '''判断是否存在，写入
    Arguments:
        url {str} -- url

    Keyword Arguments:
        types {str} -- 读/写 (default: {'r'})

    Returns:
        bool -- [description]
    '''
    [path, file] = os.path.split(downFile)
    if os.path.exists(path) == False:
        os.mkdir(path)
    if os.path.exists(downFile) == False:
        open(downFile, 'w').close()
        if types == 'r':
            return False
    else:
        f = open(downFile).read()
        if types == 'r':
            if url in f:
                return True
            else:
                return False
        else:
            creater_time = time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime())
            log = '%s %s : %s \n' % (f, creater_time, url)
            open(downFile, 'w').write(log)
