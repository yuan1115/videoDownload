# -*- coding: utf-8 -*-
# @Author: jmx
# @Date:   2019-01-08 17:45:36
# @Last Modified by:   jmx
# @Last Modified time: 2019-02-15 13:30:53
# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Jun 17 2015)
# http://www.wxformbuilder.org/
##
# PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import webbrowser
import wx.xrc
import wx.grid
import images
from os import system, getcwd, path, mkdir

###########################################################################
# Class MyFrame1
###########################################################################


class mainFrame (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"下载工具", pos=wx.DefaultPosition, size=wx.Size(
            858, 511), style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))
        self.SetIcon(images.AppIcon.GetIcon())

        mainbSizer = wx.BoxSizer(wx.HORIZONTAL)

        actionbSizer = wx.BoxSizer(wx.VERTICAL)

        name_radioBoxChoices = [u"按名称命名", u"按id命名", u"按链接命名", u"按名称+id命名"]
        self.name_radioBox = wx.RadioBox(
            self, wx.ID_ANY, u"输出文件名格式", wx.DefaultPosition, wx.DefaultSize, name_radioBoxChoices, 1, wx.RA_SPECIFY_ROWS)
        self.name_radioBox.SetSelection(3)
        actionbSizer.Add(self.name_radioBox, 0, wx.ALL | wx.EXPAND, 5)

        format_radioBoxChoices = [u"默认最佳", u"1080P", u"720", u"480", u"360"]
        self.format_radioBox = wx.RadioBox(
            self, wx.ID_ANY, u"视频分辨率", wx.DefaultPosition, wx.DefaultSize, format_radioBoxChoices, 1, wx.RA_SPECIFY_ROWS)
        self.format_radioBox.SetSelection(0)
        actionbSizer.Add(self.format_radioBox, 0, wx.ALL | wx.EXPAND, 5)

        m_radioBoxChoices = [u"是", u"否"]
        self.m_radioBox = wx.RadioBox(self, wx.ID_ANY, u"视频音频是否合成", wx.DefaultPosition,
                                      wx.DefaultSize, m_radioBoxChoices, 1, wx.RA_SPECIFY_ROWS)
        self.m_radioBox.SetSelection(0)
        actionbSizer.Add(self.m_radioBox, 0, wx.ALL | wx.EXPAND, 5)

        selebSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.seleTime_checkBox = wx.CheckBox(
            self, wx.ID_ANY, u"按上传时间筛选：", wx.DefaultPosition, wx.DefaultSize, 0)
        selebSizer.Add(self.seleTime_checkBox, 0, wx.ALL, 5)

        self.m_textCtrl4 = wx.TextCtrl(
            self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.Size(40, -1), wx.TE_CENTRE)
        selebSizer.Add(self.m_textCtrl4, 0, 0, 5)

        self.day_staticText = wx.StaticText(
            self, wx.ID_ANY, u"天", wx.DefaultPosition, wx.DefaultSize, 0)
        self.day_staticText.Wrap(-1)
        selebSizer.Add(self.day_staticText, 0, wx.ALL, 5)

        self.m_staticline3 = wx.StaticLine(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL | wx.LI_VERTICAL)
        selebSizer.Add(self.m_staticline3, 0, wx.EXPAND | wx.ALL, 5)

        # self.seleSize_checkBox = wx.CheckBox(
        #     self, wx.ID_ANY, u"按照文件大小筛选：", wx.DefaultPosition, wx.DefaultSize, 0)
        # selebSizer.Add(self.seleSize_checkBox, 0, wx.ALL, 5)

        # self.limitSize_textCtrl = wx.TextCtrl(
        #     self, wx.ID_ANY, u"100", wx.DefaultPosition, wx.Size(40, -1), wx.TE_CENTRE)
        # selebSizer.Add(self.limitSize_textCtrl, 0, 0, 5)

        # self.du_staticText = wx.StaticText(
        #     self, wx.ID_ANY, u"M", wx.DefaultPosition, wx.DefaultSize, 0)
        # self.du_staticText.Wrap(-1)
        # selebSizer.Add(self.du_staticText, 0, wx.ALL, 5)

        actionbSizer.Add(selebSizer, 0, wx.ALL | wx.EXPAND, 5)

        threadbSizer = wx.BoxSizer(wx.HORIZONTAL)

        # self.open_checkBox = wx.CheckBox(
        #     self, wx.ID_ANY, u"多进程下载", wx.DefaultPosition, wx.DefaultSize, 0)
        # threadbSizer.Add(self.open_checkBox, 0, wx.ALL, 5)

        # self.thread_staticText = wx.StaticText(
        #     self, wx.ID_ANY, u"进程数：", wx.DefaultPosition, wx.DefaultSize, 0)
        # self.thread_staticText.Wrap(-1)
        # threadbSizer.Add(self.thread_staticText, 0, wx.ALL, 5)

        # self.m_textCtrl41 = wx.TextCtrl(
        #     self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.Size(40, -1), wx.TE_CENTRE)
        # self.m_textCtrl41.SetMaxLength(2)
        # threadbSizer.Add(self.m_textCtrl41, 0, 0, 5)

        # self.du_staticText = wx.StaticText(
        #     self, wx.ID_ANY, u"个", wx.DefaultPosition, wx.DefaultSize, 0)
        # self.du_staticText.Wrap(-1)
        # threadbSizer.Add(self.du_staticText, 0, wx.ALL, 5)

        # self.m_staticText6 = wx.StaticText(
        #     self, wx.ID_ANY, u"（最多填16）", wx.DefaultPosition, wx.DefaultSize, 0)
        # self.m_staticText6.Wrap(-1)
        # threadbSizer.Add(self.m_staticText6, 0, wx.ALL, 5)

        actionbSizer.Add(threadbSizer, 0, wx.ALL | wx.EXPAND, 5)

        mainbSizer.Add(actionbSizer, 2, wx.ALL | wx.EXPAND, 5)

        self.m_staticline2 = wx.StaticLine(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL | wx.LI_VERTICAL)
        self.m_staticline2.SetForegroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        self.m_staticline2.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))

        mainbSizer.Add(self.m_staticline2, 0, wx.ALL | wx.EXPAND, 10)

        link_bSizer = wx.BoxSizer(wx.VERTICAL)

        linkbSizer = wx.BoxSizer(wx.VERTICAL)

        self.tips_staticText = wx.StaticText(
            self, wx.ID_ANY, u"链接格式：一条一行", wx.DefaultPosition, wx.DefaultSize, 0)
        self.tips_staticText.Wrap(-1)
        linkbSizer.Add(self.tips_staticText, 0, wx.ALL, 5)

        self.link_textCtrl = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, 350), style=wx.HSCROLL | wx.TE_MULTILINE)
        linkbSizer.Add(self.link_textCtrl, 0, wx.ALL | wx.EXPAND, 5)

        link_bSizer.Add(linkbSizer, 5, wx.EXPAND, 5)

        bntbSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.start_button = wx.Button(
            self, wx.ID_ANY, u"开始下载", wx.DefaultPosition, wx.Size(-1, -1), wx.BU_EXACTFIT)
        bntbSizer.Add(self.start_button, 0, wx.ALL, 5)

        self.stop_button = wx.Button(
            self, wx.ID_ANY, u"结束进程", wx.DefaultPosition, wx.Size(-1, -1), wx.BU_EXACTFIT)
        bntbSizer.Add(self.stop_button, 0, wx.ALL, 5)

        self.lookfile_button = wx.Button(
            self, wx.ID_ANY, u"下载目录", wx.DefaultPosition, wx.Size(-1, -1), wx.BU_EXACTFIT)
        bntbSizer.Add(self.lookfile_button, 0, wx.ALL, 5)

        self.lookplat_button = wx.Button(
            self, wx.ID_ANY, u"支持平台", wx.DefaultPosition, wx.Size(-1, -1), wx.BU_EXACTFIT)
        bntbSizer.Add(self.lookplat_button, 1, wx.ALL, 5)

        link_bSizer.Add(bntbSizer, 1, wx.ALL | wx.EXPAND, 5)

        mainbSizer.Add(link_bSizer, 2, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(mainbSizer)
        self.Layout()
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(4)
        self.statusbar.SetStatusWidths([-1, -4, -2, -2])
        self.statusbar.SetStatusText(u'欢迎使用', 0)
        self.statusbar.SetStatusText(
            u'项目地址：https://github.com/yuan1115/videoDownload', 1)
        self.statusbar.SetStatusText(u'总进度：0', 3)

        self.Centre(wx.BOTH)

        self.start_button.Bind(wx.EVT_BUTTON, self.download_even)
        self.stop_button.Bind(wx.EVT_BUTTON, self.endthr_even)
        self.lookfile_button.Bind(wx.EVT_BUTTON, self.lookfile_even)
        self.lookplat_button.Bind(wx.EVT_BUTTON, self.lookplat_even)

    def lookplat_even(self, event):
        event.Skip()
        link = linkType(None)
        link.Show()

    def lookfile_even(self, event):
        if path.exists(getcwd()+'\\下载目录') == False:
            mkdir(getcwd()+'\\下载目录')
        system('explorer '+getcwd()+'\\下载目录')

    def __del__(self):
        pass


class linkType (wx.Frame):
    supportLink = [
        {'name': '优酷', "url": 'www.youku.com/1'}
    ]

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title='支持列表', pos=wx.DefaultPosition, size=wx.Size(
            520, 300), style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.TAB_TRAVERSAL)
        self.SetIcon(images.AppIcon.GetIcon())

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER))

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_grid1 = wx.grid.Grid(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(500, 300), 0)
        rows = len(self.supportLink)
        # Grid
        self.m_grid1.CreateGrid(rows, 2)
        self.m_grid1.EnableEditing(False)
        self.m_grid1.EnableGridLines(True)
        self.m_grid1.EnableDragGridSize(False)
        self.m_grid1.SetMargins(0, 0)

        # Columns
        self.m_grid1.SetColSize(0, 80)
        self.m_grid1.SetColSize(1, 355)
        self.m_grid1.EnableDragColMove(False)
        self.m_grid1.EnableDragColSize(True)
        self.m_grid1.SetColLabelSize(30)
        self.m_grid1.SetColLabelValue(0, u"平台名")
        self.m_grid1.SetColLabelValue(1, u"链接格式")
        for i in range(rows):
            self.m_grid1.SetCellValue(i, 0, self.supportLink[i]['name'])
            self.m_grid1.SetCellValue(i, 1, self.supportLink[i]['url'])

        self.m_grid1.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid1.AutoSizeRows()
        self.m_grid1.EnableDragRowSize(False)
        self.m_grid1.SetRowLabelSize(40)
        self.m_grid1.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance
        self.m_grid1.SetLabelBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK))
        self.m_grid1.SetLabelTextColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        # Cell Defaults
        self.m_grid1.SetDefaultCellBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.m_grid1.SetDefaultCellTextColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTIONTEXT))
        self.m_grid1.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer4.Add(self.m_grid1, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.SetSizer(bSizer4)
        self.Layout()
        self.Centre(wx.BOTH)

        self.m_grid1.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.tourl)

    # Virtual event handlers, overide them in your derived class
    def tourl(self, event):
        event.Skip()
        row, col = event.GetRow(), event.GetCol()
        if col == 1:
            url = self.m_grid1.GetCellValue(row, col)
            webbrowser.open(url)

    def __del__(self):
        pass
