# -*- coding: utf-8 -*-
# @Author: jmx
# @Date:   2018-12-21 09:15:03
# @Last Modified by:   jmx
# @Last Modified time: 2019-01-25 09:56:20
import os
import re
import time
import ctypes
import win32con
import win32api
import youtube_dl
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def log(workspace, str, isPrint=0):
    '''日志创建
    Arguments:
        str {str} -- 异常描述

    Keyword Arguments:
        isPrint {number} -- 是否打印异常 (default: {0})
    '''
    if os.path.exists(workspace+'\\错误日志') == False:
        os.mkdir(workspace+'\\错误日志')
    if os.path.exists(workspace+'\\错误日志/error.log') == False:
        open(workspace+'\\错误日志/error.log', 'w').close()
    f = open(workspace+'\\错误日志/error.log').read()
    creater_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    log = '%s %s : %s \n' % (f, creater_time, str)
    open(workspace+'\\错误日志/error.log', 'w').write(log)
    if isPrint == 1:
        tips(str)


def isDone(workspace, url, types='r'):
    '''判断是否存在，写入
    Arguments:
        url {str} -- url

    Keyword Arguments:
        types {str} -- 读/写 (default: {'r'})

    Returns:
        bool -- [description]
    '''
    if os.path.exists(workspace+'\\错误日志') == False:
        os.mkdir(workspace+'\\错误日志')
    if os.path.exists(workspace+'\\错误日志/total.download') == False:
        open(workspace+'\\错误日志/total.download', 'w').close()
        if types == 'r':
            return False
    else:
        f = open(workspace+'\\错误日志/total.download').read()
        if types == 'r':
            if url in f:
                return True
            else:
                return False
        else:
            creater_time = time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime())
            log = '%s %s : %s \n' % (f, creater_time, url)
            open(workspace+'\\错误日志/total.download', 'w').write(log)


def tips(str):
    '''提示
    Arguments:
        str {str} -- [description]
    '''
    print('*'.center(40+len(str), '*'))
    print(str.center(40, ' '))
    print('*'.center(40+len(str), '*'))


class email():
    """docstring for ClassName"""
    __mail_host = ""  # 设置服务器
    __mail_user = ""  # 用户名
    __mail_pass = ""  # 口令
    __sender = ''

    def __init__(self):
        # 添加是否邮件提醒
        emailConfFile = self.__workspace+'\\错误日志\\email.conf'
        if os.path.exists(emailConfFile) == False:
            o = ['1.是', '2.否']
            try:
                a = int(
                    input('是否启用邮件提醒(默认：1)：\n{}\n'.format('\n'.join(o))))
            except ValueError:
                a = 1
            if a not in [1, 2]:
                a = 1
            tips('选择是否邮件提醒：%s' % a)
            if a == 1:
                if os.path.exists(self.__workspace+'\\错误日志') == False:
                    os.makedirs(self.__workspace+'\\错误日志')
                open(emailConfFile, 'w').write('1')
                win32api.SetFileAttributes(
                    emailConfFile, win32con.FILE_ATTRIBUTE_HIDDEN)

    def sendEmail(self, receivers, content):
        '''邮件发送

        异常处理邮件，下载完成邮件

        Arguments:
            receivers {list} -- [description]
            content {str} -- [内容]
        '''
        # isopen = open(self.__workspace+'\\错误日志\\email.conf')
        # if isopen != '1':
        #     return False
        # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        message = MIMEText(content, 'plain', 'utf-8')
        message['From'] = Header("管理员", 'utf-8')
        message['To'] = Header("软件使用者", 'utf-8')
        subject = '视频下载异常通知'
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.__mail_host, 25)
            smtpObj.login(self.__mail_user, self.__mail_pass)
            smtpObj.sendmail(self.__sender, receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")


class videoDownload(email):
    '''docstring for videoDownload

    [description]

    Variables:
        __workspace {str} -- [工作区]
        __proxyUrl {list} -- 需要代理的平台
    '''
    __workspace = os.getcwd()
    __proxyUrl = ['youtube.com']
    downloadType = 0
    downType = ['1.you-get', '2.youtube-dl']
    OutFormatNum = 0  # 选择的
    formatType = ['1.按照标题', '2.按照id', '3.按照url', '4.标题加id']
    OutFormat = '%(title)s.%(ext)s'
    # 支持的url格式
    __youtubeDlSUp = [
        'https://www.laola1.tv/en-int/video/stimmen-sv-kapfenberg-sturm-graz-len',
        'https://v.youku.com/v_show/id_XMzc5MzgzMzk2OA==.html'
        'https://www.bilibili.com/video/av38753351/',
        'https://www.youtube.com/watch?v=XyAFYKYD2OI',
        'https://www.youtube.com/watch?v=9cPGugdipoU&list=PLhItSD5qK6iEbWmK4n5ty2-ZEZgPkms-r'
    ]

    def __init__(self):
        if os.path.exists(self.__workspace+'\\下载目录') == False:
            os.mkdir(self.__workspace+'\\下载目录')
        if os.path.exists(self.__workspace+'\\错误日志') == False:
            os.mkdir(self.__workspace+'\\错误日志')
        if os.path.exists('异常链接.txt') == False:
            open('异常链接.txt', 'w').close()
        if os.path.exists('视频链接.txt') == False:
            open('视频链接.txt', 'w').close()
        while os.path.exists(self.__workspace+'\\错误日志\\usr.txt') == False:
            name = input('请输入你的姓名\n')
            self.downloadType = self.chooseType(self.downType)
            self.OutFormatNum, self.__OutFormat = self.chooseOutFormat(
                self.formatType)
            if name.strip() != '':
                conf = name+'\n'+str(self.downloadType)+'\n'+self.OutFormat
                open(self.__workspace+'\\错误日志\\usr.txt', 'w').write(conf)
                win32api.SetFileAttributes(
                    self.__workspace+'\\错误日志\\usr.txt', win32con.FILE_ATTRIBUTE_HIDDEN)
        else:
            conf = open(self.__workspace+'\\错误日志\\usr.txt').readlines()
            self.name = conf[0].replace('\n', '')
            self.downloadType = conf[1].replace('\n', '')
            self.__OutFormat = conf[2].replace('\n', '')

    def chooseType(self, downType):
        '''选择下载方式
        1.you-get(还没写)
        2.youtube-dl

        Arguments:
            downType {list} -- 可选的下载方式

        Returns:
            [type] -- [description]
        '''
        try:
            downloadType = int(
                input('选择下载方式(默认:youtubl-dl,目前只有youtube-dl)：\n{}\n'.format('\n'.join(downType))))
            if downloadType not in [1, 2]:
                downloadType = 2
            if downloadType == 1:
                downloadType = 2
                tips('you-get下载方式即将上线')
        except ValueError:
            downloadType = 2
        tips('下载方式选择的是：%s' % downloadType)
        return downloadType

    def chooseOutFormat(self, formatType):
        '''选择输出文件的格式

        [description]

        Arguments:
            formatType {list} -- [description]

        Returns:
            [type] -- [description]
        '''
        try:
            OutFormatNum = int(
                input('选择输出文件的格式(默认：标题)：\n{}\n'.format('\n'.join(formatType))))
            if OutFormatNum not in [1, 2, 3, 4]:
                OutFormatNum = 1
        except ValueError:
            OutFormatNum = 1
        tips('输出文件的格式选择的是：%s' % OutFormatNum)
        if OutFormatNum == 1:
            OutFormat = '%(title)s.%(ext)s'
        if OutFormatNum == 2:
            OutFormat = '%(id)s.%(ext)s'
        if OutFormatNum == 3:
            OutFormat = '%(url)s.%(ext)s'
        if OutFormatNum == 4:
            OutFormat = '%(title)s-%(id)s.%(ext)s'
        return OutFormatNum, OutFormat

    def downVideo(self, url, isProxy=0, times=1):
        if self.downloadType == '1':
            pass
        else:
            self.youtubeDl(url, isProxy, times)

    def youtubeDl(self, url, isProxy, times):
        # 定义某些下载参数
        ydl_opts = {
            # outtmpl 格式化下载后的文件名，避免默认文件名太长无法保存
            'outtmpl': self.__OutFormat,
            'format': 'best'
        }

        for i in self.__proxyUrl:
            if i in url:
                isProxy = 1
                break

        if isProxy == 1:
            ydl_opts['proxy'] = 'http://127.0.0.1:1080'

        try:
            info = youtube_dl.YoutubeDL(ydl_opts).extract_info(
                url, download=False)
        except youtube_dl.utils.DownloadError as e:
            error = str(e)
            if '10061' in error:
                e = ctypes.windll.user32.MessageBoxA(
                    0, '请打开梯子再继续'.encode('gbk'), '脚本异常'.encode('gbk'), 0)
                if e == 1:
                    pass
                exit()
            if times > 2:
                # 如需启用邮件提醒功能先配置email类里面的参数
                # self.sendEmail(['接收邮箱'],
                #                '{}获取{}链接的视频出错，错误信息：{}，跳过该视频！'.format(self.name, url, error))
                log(self.__workspace, self.__workspace,
                    '获取{}链接的视频出错，错误信息：{}，跳过该视频！'.format(url, error), 1)
                f = open('异常链接.txt').read()
                if url in f:
                    pass
                else:
                    open('异常链接.txt', 'w').write(f+url+'\n')
                return False
            else:
                times += 1
                self.youtubeDl(url, isProxy, times)
                return False

        playlist = 0
        if '_type' in info:
            if info['_type'] == 'playlist':
                playlist = 1

        # 判断youtube是否列表
        if playlist == 1:
            if os.path.exists('下载目录\\'+info['id']) == False:
                os.mkdir('下载目录\\'+info['id'])
            os.chdir(self.__workspace+'\\下载目录\\'+info['id'])
            for v in info['entries']:
                # 自动选择选择格式
                # for i in v['formats']:
                #     filename = filename.replace('%(ext)s', v['ext'])
                #
                filePath = '下载目录\\'+info['id']+'\\'
                self.youtubeDlOne(filePath, v, ydl_opts, isProxy, times)
        else:
            filePath = '下载目录\\'
            os.chdir(self.__workspace+'\\下载目录')
            self.youtubeDlOne(filePath, info, ydl_opts, isProxy, times)
        os.chdir(self.__workspace)

    def youtubeDlOne(self, filePath, info, ydl_opts, isProxy, times):
        url = info['webpage_url']
        filename = self.__OutFormat.replace('%(title)s', info['title']).replace(
            '%(id)s', info['id']).replace('%(url)s', info['webpage_url']).replace('%(ext)s', info['ext'])
        fileName = re.sub(r'[\/:*?"<>|]', "_", filename)
        filePath = filePath+fileName
        isdownload = isDone(self.__workspace, url)
        if isdownload == True:
            log(self.__workspace, url+'已下载', 1)
            return False
        tips('开始下载%s' % url)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([url])
            except youtube_dl.utils.DownloadError as e:
                if times > 2:
                    # self.sendEmail([''], '{}下载视频{}时出错，错误信息：{}，跳过该视频！'.format(
                    #     self.name, url, str(e)))
                    log(self.__workspace,
                        '下载视频{}时出错，错误信息：{}，跳过该视频！'.format(url, str(e)), 1)
                    f = open('异常链接.txt').read()
                    if url in f:
                        pass
                    else:
                        open('异常链接.txt', 'w').write(url)
                else:
                    times += 1
                    self.youtubeDlOne(filePath, fileName, url,
                                      ydl_opts, isProxy, times)
                    return False
        if os.path.exists(filePath):
            isDone(self.__workspace, url, 'w')
        return True

    def __del__(self):
        pass


if __name__ == "__main__":
    download = videoDownload()
    urllist = open('视频链接.txt').readlines()
    i = 0
    while len(urllist):
        try:
            download.downVideo(urllist[i].replace('\n', ''))
        except IndexError:
            e = ctypes.windll.user32.MessageBoxA(
                0, '下载完成'.encode('gbk'), '下载进度'.encode('gbk'), 0)
            open('视频链接.txt', 'w').write('')
            exit()
        try:
            urllist.remove(i)
        except ValueError:
            pass
        i += 1
    else:
        e = ctypes.windll.user32.MessageBoxA(
            0, '请将视频链接复制到“视频链接.txt”中，一条一行'.encode('gbk'), '提示'.encode('gbk'), 0)
        exit()
