# -*- coding: utf-8 -*-
# @Author: jmx
# @Date:   2019-01-08 17:45:36
# @Last Modified by:   jmx
# @Last Modified time: 2019-01-22 15:57:00
# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Jun 17 2015)
# http://www.wxformbuilder.org/
##
# PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
# Class MyFrame1
###########################################################################


class MyFrame1 (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(
            611, 448), style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVEBORDER))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(
            self, wx.ID_ANY, u"链接格式：一条一行", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer3.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.m_textCtrl1 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, 300), wx.HSCROLL | wx.TE_MULTILINE)
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
        self.m_statusBar1 = self.CreateStatusBar(2, wx.ST_SIZEGRIP, wx.ID_ANY)

        self.Centre(wx.BOTH)

        # Connect Events
        self.download.Bind(wx.EVT_BUTTON, self.download_even)
        self.look.Bind(wx.EVT_BUTTON, self.look_even)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def download_even(self, event):
        event.Skip()

    def look_even(self, event):
        event.Skip()
