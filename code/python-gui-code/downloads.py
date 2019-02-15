# -*- coding: utf-8 -*-
# @Author: jmx
# @Date:   2019-01-08 17:46:10
# @Last Modified by:   jmx
# @Last Modified time: 2019-02-15 14:40:27
from gui import mainFrame
import wx
import youtube_dl
import os
import func
from datetime import datetime, date, timedelta
import threading
import time


class downloads(mainFrame):
    """docstring for downloads"""
    __nameType = [
        '%(title)s.%(ext)s',
        '%(id)s.%(ext)s',
        '%(url)s.%(ext)s',
        '%(title)s_%(id)s.%(ext)s'
    ]
    __format = [
        'bestvideo',
        '[height=1080]',
        '[height=720]',
        '[height=480]',
        '[height=360]'
    ]
    __proxyUrl = ['youtube.com']
    __error_log_Path = 'log'
    __workspace = os.getcwd()
    __outputPath = __workspace+'\\下载目录\\'

    def statusbarinfo(self, pos, strs):
        self.statusbar.SetStatusText(
            u'%s' % strs, pos)

    def download_even(self, event):
        '''点击下载事件

        [description]

        Arguments:
                event {[type]} -- [description]
        '''
        if os.path.exists(self.__outputPath) == False:
            os.mkdir(self.__outputPath)
        if os.path.exists(self.__error_log_Path) == False:
            os.mkdir(self.__error_log_Path)
        event.Skip()
        self.outtmpl = self.__nameType[self.name_radioBox.GetSelection()]
        formats = self.__format[self.format_radioBox.GetSelection()]
        if self.m_radioBox.GetSelection() == True:
            formats += '+bestaudio/best'
        else:
            formats += ',bestaudio/best'
        # if self.seleSize_checkBox.GetValue() == True:
        #     self.limitSize = self.limitSize_textCtrl.GetValue()
        # else:
        #     self.limitSize = 0

        if self.seleTime_checkBox.GetValue() == True:
            self.startTime = datetime.strptime(str(date.today(
            )), '%Y-%m-%d') + timedelta(days=-int(self.seleTime_checkBox.GetValue()))
            self.endTime = date.today()
        else:
            self.startTime = 0
            self.endTime = 0
        urllist = self.link_textCtrl.GetValue().split("\n")
        for i in urllist:
            if i == '':
                urllist.remove(i)
        if len(urllist) == 0:
            wx.MessageBox(u"请将链接复制到右侧框内", "Message",
                          wx.OK | wx.ICON_INFORMATION)
            return False
        self.statusbarinfo(3, '总进度：0/%s' % (str(len(urllist))))
        ydl_opts = {
            'outtmpl': self.outtmpl,
            'format': formats,
        }
        num = 0
        for i in urllist:
            isProxy = 0
            for j in self.__proxyUrl:
                if j in i:
                    isProxy = 1
                    break
            if isProxy == 1:
                ydl_opts['proxy'] = 'http://127.0.0.1:1080'
            self.youtubeDl(ydl_opts, i, num, len(urllist))
            num += 1

    def endthr_even(self, event):
        # filesize
        # timestamp
        # formats
        pass

    def youtubeDl(self, ydl_opts, url, num, count):
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                info = ydl.extract_info(url, download=False)
            except youtube_dl.utils.DownloadError as e:
                self.youtubeDl(ydl_opts, url, num, count)
                return False
            playlist = 0
            try:
                if '_type' in info:
                    if info['_type'] == 'playlist':
                        playlist = 1
            except TypeError:
                pass
            self.statusbarinfo(3, '总进度：%s/%s ，当前正在下载第%s个' %
                               (str(num), str(count), str(num+1)))
            # 判断是否列表
            if playlist == 1:
                if os.path.exists(self.__outputPath+info['playlist_title']) == False:
                    os.mkdir(self.__outputPath+info['playlist_title'])
                for v in info['entries']:
                    self.statusbarinfo(1, '开始下载列表%s->%s' %
                                       (info['playlist_title'], info['title']))
                    filePath = self.__outputPath+info['playlist_title']+'\\'
                    ydl_opts['outtmpl'] = filePath+ydl_opts['outtmpl']
                    self.youtubeDlOne(filePath, v, ydl_opts)
            else:
                self.statusbarinfo(1, '开始下载%s' % info['title'])
                filePath = self.__outputPath
                ydl_opts['outtmpl'] = filePath+ydl_opts['outtmpl']
                self.youtubeDlOne(filePath, info, ydl_opts)
            self.statusbarinfo(3, '总进度：%s/%s ，当前正在下载第%s个' %
                               (str(num+1), str(count), str(num+1)))

    def speed(self, filesize, filepath):
        downloadsize = 0
        fsize = 0
        sp = 'kb/s'
        realsize = round(filesize/(1024*1024), 2)
        [dirPath, filename] = os.path.split(filepath)

        while os.path.exists(filepath) == False:
            filelist = os.listdir(dirPath)
            for i in filelist:
                if filename in i:
                    downloadsize = os.path.getsize(dirPath+'\\'+i)
                    # speed = round(
                    #     (newdownloadsize-downloadsize)/(1024*1024), 2)
                    # sp = 'M/s'
                    # if speed < 1:
                    #     speed *= 1024
                    #     sp = 'kb/s'
                    fsize = round(downloadsize/(1024*1024), 2)
                    break
            self.statusbarinfo(2, str(fsize)+'/' +
                               str(realsize)+'M')
            time.sleep(1)
        else:
            self.statusbarinfo(2, str(realsize)+'/' +
                               str(realsize)+'M')
            self.statusbarinfo(1, '%s下载完成' % filename)

    def youtubeDlOne(self, filePath, info, ydl_opts, times=1):
        filelist = os.listdir(filePath)
        for i in filelist:
            if '.part' in i:
                os.remove(filePath+i)
        url = info['webpage_url']
        isdownload = func.isDone(self.__workspace+'\\log\\log.txt', url)
        if isdownload == True:
            func.log(self.__workspace, url+'已下载', 1)
            return False
        if self.startTime != 0:
            if info['upload_date'] <= str(self.startTime) or info['upload_date'] >= str(self.endTime):
                return False
        filepath = filePath+self.outtmpl.replace('%(title)s', info['title']).replace(
            '%(id)s', info['id']).replace('%(url)s', info['url']).replace('%(ext)s', info['ext'])
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                func.tips('正在下载%s' % url)
                self.statusbarinfo(1, '正在下载%s' % info['title'])
                self.t1 = threading.Thread(
                    target=ydl.download, args=([url],))
                self.t1.start()
                self.t2 = threading.Thread(
                    target=self.speed, args=(info['filesize'], filepath))
                self.t2.start()
            except youtube_dl.utils.DownloadError as e:
                if times > 2:
                    func.log(self.__workspace,
                             '下载视频{}时出错，错误信息：{}，跳过该视频！'.format(url, str(e)), 1)
                    f = open('异常链接.txt').read()
                    if url in f:
                        pass
                    else:
                        open('异常链接.txt', 'w').write(url)
                else:
                    times += 1
                    self.youtubeDlOne(filePath, info,
                                      ydl_opts, times)
                    return False
        return True


if __name__ == "__main__":
    app = wx.App()
    main_loop = downloads(None)
    main_loop.Show()
    app.MainLoop()
