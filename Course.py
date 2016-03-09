#!/usr/bin/python 
# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt4.QtGui import QDialog
from Ui_Course import Ui_dialog
import sys
from PyQt4 import QtCore, QtGui
import urllib
import urllib2
import cookielib
import cStringIO
from PIL import Image
from bs4 import BeautifulSoup
import re
import os
import time

reload(sys)
sys.setdefaultencoding('utf8')

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Dialog(QDialog, Ui_dialog):
    """
    Class documentation goes here.
    """
    
        
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        self.mainUrl = ''
        self.host = ''
        self.ss = ''
        self.userName = ''
        self.password = ''
        self.yourName = ''
        self.imgurl = ''
        self.loginVIEWSTATE = ''
        self.loggined = False
        self.sHome = ''
        self.paths = "D:/Python/downloadCode/"
        self.dic = {}
        self.dicTeacher = []
        self.teacherCode = {}
        if not os.path.isdir(self.paths):
            os.makedirs(self.paths)
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
    @QtCore.pyqtSignature("")
    def on_rb_bzy_clicked(self):
        """
        Slot documentation goes here.
        """
        self.lb.setText(u"本专业选课")
        
        # TODO: not implemented yet
    
    @QtCore.pyqtSignature("")
    def on_b_ok_clicked(self):
        """
        Slot documentation goes here.
        """
        headers = {
            #    '(Request-Line)':'GET /%28' + ss + '%29/xsxk.aspx?xh=41211052&xm=Ñ§Éú&gnmkdm=N121101 HTTP/1.1',
                'Host':self.host,
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            #    'Accept-Encoding':'gzip, deflate',
                'Referer':'http://' + self.host + '/' + self.ss + '/xs_main.aspx?xh=' + self.userName,
                'Connection':'keep-alive'
        }
        for index in xrange(self.lw_choose.count()):
            code = unicode(str(self.lw_choose.item(index).text()).split(',')[-1], "utf8")
            url = self.dic[unicode(str(self.lw_choose.item(index).text()).split(',')[6], "utf8")]
            row = int(str(self.lw_choose.item(index).text()).split(',')[0])
            req3 = urllib2.Request(
                headers = headers,
                url = url
            #    url = 'http://' + host + '/%28' + ss + '%29/xsxjs.aspx?xkkh=' + xkkh + '&xh=41211052'
            )
            cookie = cookielib.CookieJar()#创建cookie
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))#创建应用cookie进行访问的'浏览器'
            result3 = opener.open(req3)
            s3 = unicode(result3.read(),'gbk')
            soupS3 = BeautifulSoup(s3).find("table",class_="formlist")
            soupTrS3 = BeautifulSoup(str(soupS3)).find_all("tr")
            while unicode(str(soupTrS3[row+1]), "utf8").find("checked") == -1:
                soupCourses = BeautifulSoup(s3).find_all("input")
                reCourse = re.compile(r"value=\"(.*?)\"")
                VIEWSTATE = reCourse.search(str(soupCourses[2])).group(1)
                VIEWSTATEGENERATOR = reCourse.search(str(soupCourses[3])).group(1)
                headerOfCourse = {
                    'Host':self.host,
                    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
                    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                #    'Accept-Encoding':'gzip, deflate',
                    'Referer':url,#'http://' + host + '/%28' + ss + '%29/xsxjs.aspx?xkkh=' + xkkh + '&xh=' + userName,
                    'Connection':'keep-alive',
                    'Content-Type':'application/x-www-form-urlencoded',
                #    'Content-Length':'591'
                }
                courseData = {
                    '__EVENTTARGET':'Button1',
                    '__EVENTARGUMENT':'',
                    '__VIEWSTATE':VIEWSTATE,
                    #需要获取
                    '__VIEWSTATEGENERATOR':VIEWSTATEGENERATOR,
                    'xkkh':code,
                    'RadioButtonList1':'1'
                }
                postCourseData = urllib.urlencode(courseData)
                reqCourse = urllib2.Request(
                    headers = headerOfCourse,
                    url = url,
                    data = postCourseData
                )
                result4 = opener.open(reqCourse)
                s4 = unicode(result4.read(),'gbk')
                
                result3 = opener.open(req3)
                s3 = unicode(result3.read(),'gbk')
                soupS3 = BeautifulSoup(s3).find("table",class_="formlist")
                soupTrS3 = BeautifulSoup(str(soupS3)).find_all("tr")
                time.sleep(5)
                
        self.lb.setText(unicode("刷课完毕！", "utf8"))
        #self.lb.setText(u"开始刷课……")
        # TODO: not implemented yet
    
    def ImageScale(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(self.paths + "/aaa.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.code.setIcon(icon)
    
    def gDownloadWithFilename(self, url,savePath,file): 
        try: 
            urlopen=urllib.URLopener() 
            fp = urlopen.open(url) 
            data = fp.read() 
            fp.close() 
            file=open(savePath + file,'w+b') 
            file.write(data) 
            file.close()
        except IOError, error: 
            print "DOWNLOAD %s ERROR!==>>%s" % (url, error) 
        except Exception, e: 
            print "Exception==>>" + e 
    
    @QtCore.pyqtSignature("")
    def on_b_login_clicked(self):
        """
        Slot documentation goes here.
        """
        self.l_zt.setText(u"状态：准备登录...")
        self.loggined = False
        cookie = cookielib.CookieJar()#创建cookie
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))#创建应用cookie进行访问的'浏览器'
        soupVIEWSTATE = BeautifulSoup(urllib2.urlopen(self.mainUrl,timeout = 120).read()).find("input")
        reVIEWSTATE = re.compile(r"value=\"(.*?)\"")
        self.loginVIEWSTATE = reVIEWSTATE.search(str(soupVIEWSTATE)).group(1)
        self.userName = str(self.tb_id.text())
        self.password = str(self.tb_pw.text())
        self.yourName = str(self.tb_name.text())
        #self.ImageScale()
        #authcode = str(self.b_code.text())
        data = {
            '__VIEWSTATE':self.loginVIEWSTATE,
            '__VIEWSTATEGENERATOR':'92719903',
            'txtUserName':self.userName,
            'TextBox2':self.password,
            'txtSecretCode':str(self.b_code.text()),
            'RadioButtonList1':self.yourName,#'Ñ§Éú',
            'Button1':'',
            'lbLanguage':'',
            'hidPdrs':'',
            'hidsc':''
        }
        postData = urllib.urlencode(data)
        req = urllib2.Request(
            #    headers = header,
            url = 'http://' + self.host + '/' + self.ss + '/default2.aspx',
            data = postData
        )
        result = opener.open(req) 
        s = unicode(result.read(),'gbk')
        self.sHome = s
        if s.find(u"退出") > -1:
            self.loggined = True
        if s.find(u"验证码不正确") > -1:
            self.l_zt.setText(u"状态：验证码不正确")
        if self.loggined:
            self.l_zt.setText(u"状态：已登录")
        if not self.loggined:
            exit()
        headers = {
            #    '(Request-Line)':'GET /%28' + ss + '%29/xsxk.aspx?xh=41211052&xm=Ñ§Éú&gnmkdm=N121101 HTTP/1.1',
                'Host':self.host,
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            #    'Accept-Encoding':'gzip, deflate',
                'Referer':'http://' + self.host + '/' + self.ss + '/xs_main.aspx?xh=' + self.userName,
                'Connection':'keep-alive'
        }
        req2 = urllib2.Request(
            headers = headers,
            url = 'http://' + self.host + '/' + self.ss + '/xsxk.aspx?xh=' + self.userName + '&xm=' + self.yourName + '&gnmkdm=N121101'
        )
        result2 = opener.open(req2)
        sCourses = result2.read().decode("gbk", "ignore")
        soupCourses = BeautifulSoup(sCourses).find("table",class_="datelist")
        soupTr = BeautifulSoup(str(soupCourses)).find_all("tr")
        soupA = BeautifulSoup(str(soupTr[len(soupTr)-1])).find_all("a")
        if soupA == []:
            pages = 1
        else:
            pages = int(soupA[len(soupA)-1].string)
        docPage = sCourses
        soupPage = BeautifulSoup(docPage).find_all("input")
        for sp in soupPage:
            if str(sp).find("zymc") > -1:
                rePage = re.compile(r"value=\"(.*?)\"")
                major = rePage.search(str(sp)).group(1)
        pageHeaders = {
            'Host':self.host,
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        #    'Accept-Encoding':'gzip, deflate',
            'Referer':'http://' + self.host + '/'+ self.ss + '/xsxk.aspx?xh='+ self.userName +'&xm='+ self.yourName +'&gnmkdm=N121101',
            'Connection':'keep-alive',
            'Content-Type':'application/x-www-form-urlencoded',
        #    'Content-Length':'20361'
        }
        #print pages
        for p in range(pages):
            soupCourses = BeautifulSoup(docPage).find("table",class_="datelist")
            soupTr = BeautifulSoup(str(soupCourses)).find_all("tr")
            for i in range(len(soupTr)):
                if i != 0 and i != len(soupTr)-1:
            #        print i
                    soupTd = BeautifulSoup(str(soupTr[i])).find_all('td')
                    reCourse = re.compile(r"open\(\'(.*?)\'\,\'xsxjs")
                    ans = reCourse.search(str(soupTd[1]))
                    urlCourse = ans.group(1)
                    urlCourseComp = 'http://' + self.host + '/' + self.ss + '/' + urlCourse
                    urlCourseComp =  urlCourseComp.replace("&amp;","&")
                    courseName = BeautifulSoup(str(soupTd[1])).string
        #            print courseName
                    self.dic.setdefault(courseName,urlCourseComp)
            #        dic[unicode(s,"gb2312")]#查询
            
            if p != pages - 1:
                soupPage = BeautifulSoup(docPage).find_all("input")
                for sp in soupPage:
                    if str(sp).find("VIEWSTATE") > -1 and str(sp).find("VIEWSTATEGENERATOR") == -1:
                        rePage = re.compile(r"value=\"(.*?)\"")
                        pageVIEWSTATE = rePage.search(str(sp)).group(1)
                    if str(sp).find("VIEWSTATEGENERATOR") > -1 :
                        rePage = re.compile(r"value=\"(.*?)\"")
                        pageVIEWSTATEGENERATOR = rePage.search(str(sp)).group(1)
                postPageData = urllib.urlencode({
                    '__EVENTTARGET':'kcmcgrid:_ctl14:_ctl'+str(p+1),
                    '__EVENTARGUMENT':'',
                    '__VIEWSTATE':pageVIEWSTATE,
                    '__VIEWSTATEGENERATOR':pageVIEWSTATEGENERATOR,
                    'zymc':major,
                    'xx':''
                })
                reqPage = urllib2.Request(
                    headers = pageHeaders,
                    url = 'http://' + self.host + '/' + self.ss + '/xsxk.aspx?xh=' + self.userName + '&xm=' + self.yourName + '&gnmkdm=N121101',
                    data = postPageData
                )
                resultPage = opener.open(reqPage)
                docPage = resultPage.read()
            #print docPage
        for index in xrange(self.lw_course.count()):
            self.lw_course.takeItem(0)
        dicIndex = 0
        for i in self.dic:
            item = QtGui.QListWidgetItem()
            self.lw_course.addItem(item)
            item = self.lw_course.item(dicIndex)
            item.setText(_translate("Dialog", i, None))
            dicIndex += 1
            # TODO: not implemented yet
    @QtCore.pyqtSignature("")
    def on_code_clicked(self):
        """
        Slot documentation goes here.
        """
        self.mainUrl = str(self.url.text())
        self.host = self.mainUrl.split('/')[2]
        self.ss = self.mainUrl.split('/')[3]
        self.imgurl = 'http://'+ self.host +'/' + self.ss + '/CheckCode.aspx'
        self.gDownloadWithFilename(self.imgurl, self.paths, 'aaa.gif')
        self.ImageScale()
        # TODO: not implemented yet
    
    @QtCore.pyqtSignature("QListWidgetItem*")
    def on_lw_course_itemClicked(self, item):
        """
        Slot documentation goes here.
        """
        self.dicTeacher = []
        self.lb.setText("start")
        courseName = str(item.text())
        #self.url = self.dic[unicode(courseName,"gb2312")]
        self.url = self.dic[unicode(courseName,'utf8')]
        #self.lb.setText(self.url)
        #xkkhRe = re.compile(r"xkkh=(.*?)&")
        #xkkh = xkkhRe.search(self.url).group(1)
        headers = {
            #    '(Request-Line)':'GET /%28' + ss + '%29/xsxk.aspx?xh=41211052&xm=Ñ§Éú&gnmkdm=N121101 HTTP/1.1',
                'Host':self.host,
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            #    'Accept-Encoding':'gzip, deflate',
                'Referer':'http://' + self.host + '/' + self.ss + '/xs_main.aspx?xh=' + self.userName,
                'Connection':'keep-alive'
        }
        req3 = urllib2.Request(
            headers = headers,
            url = self.url
        #    url = 'http://' + host + '/%28' + ss + '%29/xsxjs.aspx?xkkh=' + xkkh + '&xh=41211052'
        )
        
        cookie = cookielib.CookieJar()#创建cookie
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))#创建应用cookie进行访问的'浏览器'
        result3 = opener.open(req3)
        s3 = unicode(result3.read(),'gbk')
        soupS3 = BeautifulSoup(s3).find("table",class_="formlist")
        soupTrS3 = BeautifulSoup(str(soupS3)).find_all("tr")
        self.sq = 0
        index = 0
        for i in range(len(soupTrS3)):
            if str(soupTrS3[i]).find("tuchu") > -1:
                self.sq = 1
            else:
                self.sq = 0
            if i != 0:
                soupTdS3 = BeautifulSoup(str(soupTrS3[i])).find_all("td")
                reXkkh = re.compile(r"xkkh=(.*?)&amp;")
                xkkhs = reXkkh.search(str(soupTdS3[1])).group(1)
                teacherName = soupTdS3[1].string
                time = soupTdS3[5].string
                address = soupTdS3[6].string
                xy = soupTdS3[2].string
                self.dicTeacher.append(str(index)+","+teacherName+","+xy+","+time+","+address+","+str(self.sq)+","+unicode(str(item.text()), "utf8"))
                self.teacherCode.setdefault(str(index)+","+teacherName+","+xy+","+time+","+address+","+str(self.sq)+","+unicode(str(item.text()), "utf8"), unicode(xkkhs, "utf8"))
                index += 1
                self.lb.setText(unicode("打开完毕，请双击课程添加到刷课列表。你最好选择课程名前为1的课程。", "utf8"))
        iTeacher = 0
        
        for index in xrange(self.lw_msg.count()):
            self.lw_msg.takeItem(0)
        
        for it in self.dicTeacher:
            #self.lb.setText("aaa")
            item = QtGui.QListWidgetItem()
            self.lw_msg.addItem(item)
            item = self.lw_msg.item(iTeacher)
            item.setText(_translate("Dialog", unicode(str(it), "utf8"), None))
            iTeacher += 1
        # TODO: not implemented yet
    
    @QtCore.pyqtSignature("QListWidgetItem*")
    def on_lw_msg_itemDoubleClicked(self, item):
        """
        Slot documentation goes here.
        """
        #self.lb.setText(str(self.lw_choose.count()))
        index = 0
        b = True
        for i in range(self.lw_choose.count()):
            if str(self.lw_choose.item(index).text()).find(str(item.text())) > -1:
                self.lb.setText(unicode("待刷课程中含有该课程，请不要重复选择。", "utf8"))
                b = False
            index += 1
        if b:
            items = QtGui.QListWidgetItem()
            self.lw_choose.addItem(items)
            items = self.lw_choose.item(index)
            items.setText(_translate("Dialog", unicode(str(item.text()),"utf8")+unicode(",", "utf8")+unicode(str(self.teacherCode[unicode(str(item.text()),"utf8")]), "utf8"), None))
        # TODO: not implemented yet
    
    @QtCore.pyqtSignature("")
    def on_b_delete_clicked(self):
        """
        Slot documentation goes here.
        """
        self.lb.setText(unicode("现在上移、下移、删除、停止功能尚未开发，请期待下一版本...", "utf8"))
        # TODO: not implemented yet

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
    # TODO: not implemented yet
    
