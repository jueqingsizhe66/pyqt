#!/usr/bin/env python
#_*_coding=utf-8 _*_
"File: emaildisplay -- "
"display email on the web page or on cmd line"
"""
Python：一个类，读取邮件文件，然后返回其指定的部分，例如Subject, Date, Body, attachementsname or attachement．
工作需要，写了一个类，读取email文件，然后分析其时间，主题，文件内容，和附件文件名称以及提取附件。这个类可以用于命令行，也可以用于网页。写下来，和大家一同学习，记得以前学习过一个提取附件并保存为文件的脚本，结果，附件名前的空格被自动取消掉了，这个类也可以提取附件，并保存文件，如果从邮件的结构中文件名是怎样的，保存的文件名就是怎样的。
类的名称叫EMAIL：
1. getDate() 返回邮件的时间戳。
2. getSubject()  返回邮件的主题
3 . getBody()  返回邮件的内容
4. getAttachNames()  返回附件民（以元祖的形式
5. getAttachLoc(fname)  输入附件名称（从方法4中获得），一次提取一个附件，并保存在/tmp下，返回文件的地址。
"""
import sys
import os
import email


class EMAIL(object):
    """input email file, and output relative parts of it. such as header, body, attachment..."""
    def __init__(self, emailpath):
        try:
            self.emailPath=emailpath
            self.msg=email.message_from_file(open(emailpath))
            self.body=""
            self.filenames=[]
            for i in self.msg.walk():
                if i.get_content_type() == 'text/html': # !
                    self.body=i
                if i.get_filename() is not None:
                    self.filenames.append(i.get_filename())
        except IOError:
            sys.exit()
    def getDate(self):
        return self.msg.get('Date')

    def getSubject(self):
        return self.msg.get('Subject')

    def getBody(self):
        return self.body

    def getAttachNames(self):
        """return a tuple of attachName"""
        return tuple(self.filenames)

    def getAttachLoc(self, fname=None):
        """work like `ripmime -i`, attachment location is in /tmp/mid
           if attchments are multi, return a tuple of locations
        """
        for i in self.msg.walk():
            if i.get_filename() is not None and i.get_filename == fname:
                fpath=os.path.join("/tmp", i.get_filename())
                try:
                    f=open(fpath, "wb")
                    f.write(base64.b64decode(i.get_payload()))
                    f.close()
                except IOError:
                    return False
        return fpath
