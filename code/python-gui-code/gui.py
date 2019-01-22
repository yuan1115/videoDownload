# -*- coding: utf-8 -*-
# @Author: jmx
# @Date:   2019-01-08 17:45:36
# @Last Modified by:   jmx
# @Last Modified time: 2019-01-22 17:47:52
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

###########################################################################
# Class MyFrame1
###########################################################################


class MyFrame1 (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title='视频下载', pos=wx.DefaultPosition, size=wx.Size(
            611, 448), style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER))
        self.SetIcon(images.AppIcon.GetIcon())
        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(
            self, wx.ID_ANY, u"链接格式：一条一行", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer3.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.m_textCtrl1 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, 280), wx.HSCROLL | wx.TE_MULTILINE)
        bSizer3.Add(self.m_textCtrl1, 0, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(bSizer3, 2, wx.ALL | wx.EXPAND, 5)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.download = wx.Button(
            self, wx.ID_ANY, u"点击下载", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.download, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.look = wx.Button(self, wx.ID_ANY, u"查看支持链接",
                              wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.look, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        bSizer1.Add(bSizer2, 1, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1, -3, -1])
        self.statusbar.SetStatusText(u'欢迎使用', 0)
        self.statusbar.SetStatusText(
            u'项目地址：https://github.com/yuan1115/videoDownload', 1)
        self.statusbar.SetStatusText(u'总进度：0%', 2)

        self.Centre(wx.BOTH)

        # Connect Events
        self.download.Bind(wx.EVT_BUTTON, self.download_even)
        self.look.Bind(wx.EVT_BUTTON, self.look_even)

    def look_even(self, event):
        event.Skip()
        link = linkType(None)
        link.Show()

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
