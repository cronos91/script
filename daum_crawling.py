import urllib2
import re
import random
from bs4 import BeautifulSoup
import sys
import time
reload(sys)
sys.setdefaultencoding("utf8")
 
 
f = open('output.txt', 'w')
 
class scrolled_data(object):
    def __init__(self, url):
        self.url = url
        self.source = urllib2.urlopen(self.url).read().decode('utf-8','ignore')
        self.soup = BeautifulSoup(self.source)
 
main_url1 = "http://board2.finance.daum.net/gaia/do/stock/list?pageIndex="
main_url2 = "&objCate1=1-P013&bbsId=stock&objCate2=2-005930&viewObj=1%3A2%3A0&forceTalkro=T#mainInputArea"

for x in range(1,1000):
	data = scrolled_data(main_url1+str(x)+main_url2)
	board_list = data.soup.findAll('tr', attrs={'class':'last'})
	#Get boards
	for each in board_list:
		list = each.contents
		#should access odd number
		for y in range(1,len(list),2):
			if y == 1:
				print "####Subject####"
				print list[y].a.string 
				f.write("####Subjet####\n")
				f.write(list[y].a.string+'\n')
				link = "http://board2.finance.daum.net/gaia/do/stock/"+list[y].a['href']
				time.sleep(random.random()+random.randrange(5,6))
				contents = scrolled_data(link)
				print "####Contents####"
				f.write("####Contents####\n")
				if contents.soup.find('div', attrs={'id':'bbsContent'}):
					print contents.soup.find('div',attrs={'id':'bbsContent'}).get_text()
					f.write(contents.soup.find('div',attrs={'id':'bbsContent'}).get_text()+'\n')
					if contents.soup.find('iframe', attrs={'id':'commentList'}):
						comment_url = "http://board2.finance.daum.net/"+contents.soup.find('iframe', attrs={'id':'commentList'})['src']
						comment = scrolled_data(comment_url)
						list2 = comment.soup.findAll('dd', attrs={'class':'content'})
						for w in list2:
							print "####Comment####"
							print w.get_text()
							f.write("####Comment####")
							f.write(w.get_text()+'\n')
					else:
						continue
				else:
					continue
			if y == 3:
				print "####Nickname####"
				print list[y].a.string
				f.write("####Nickname####\n")
				f.write(list[y].a.string+'\n')
			if y == 5:
				print "####Recommand####"
				print list[y].string
				f.write("####Recommand####\n")
				f.write(list[y].string+'\n')	
			if y == 7:
				print "####Hits####"
				print list[y].string
				f.write("####Hits####\n")
				f.write(list[y].string+'\n')
			if y == 9:
				print "####Datetime####"
				print list[y].string
				f.write("####Datetime####\n")
				f.write(list[y].string+'\n')
f.close()
