from bs4 import BeautifulSoup
import sys
import urllib2
import json

def parse(content):
    #parse html content
    res = None
    if content and len(content) > 0:
        try:
            soup = BeautifulSoup(content,"html.parser")
            values = []
            box = soup.find('div', {'class' : 'content clearfix'})
            words = box.find('div',{'class':'words'})
            wordsText = words.get_text()
            wordsText = wordsText.replace('\r','').replace('\n','')
            trs = box.find_all('tr')
            if len(trs) < 5:
                print 'can not find 5 tr from div box:' + box
            else:
                tr0 = trs[0]
                tds = tr0.find_all('td')
                if len(tds) != 4:
                    print 'can not find 4 td from tr0:' + tr0
                else:
                    synthesize = str(len(tds[1].find_all('i')))
                    love = str(len(tds[3].find_all('i')))
                    values.append(('synthesize', synthesize))
                    values.append(('love', love))
                    
                tr1 = trs[1]
                tds = tr1.find_all('td')
                if len(tds) != 4:
                    print 'can not find 4 td from tr1:' + tr1
                else:
                    work = str(len(tds[1].find_all('i')))
                    manage = str(len(tds[3].find_all('i')))
                    values.append(('work', work))
                    values.append(('manage', manage))

                tr2 = trs[2]
                tds = tr2.find_all('td')
                if len(tds) != 4:
                    print 'can not find 4 td from tr2:' + tr2
                else:
                    health = tds[1].get_text()
                    talk = tds[3].get_text()
                    values.append(('health', health.replace('%','')))
                    values.append(('talk', talk.replace('%','')))

                tr3 = trs[3]
                tds = tr3.find_all('td')
                if len(tds) != 4:
                    print 'can not find 4 td from tr3:' + tr3
                else:
                    color = tds[1].get_text()
                    num = tds[3].get_text()
                    values.append(('color', color))
                    values.append(('num', num))
                    
                tr4 = trs[4]
                tds = tr4.find_all('td')
                if len(tds) != 4:
                    print 'can not find 4 td from tr4:' + tr4
                else:
                    star = tds[1].get_text()
                    values.append(('star', star))
    
                values.append(('wordsText', wordsText))
                res = values
        except Exception,e:
            print 'try get parse error:' + e.message
    else:
        print 'html content is empty or null!'
    return res

def getPageContent(url):
    #get page html
    content = ''
    if url and len(url) > 0:
        try:
            content = urllib2.urlopen(url).read()    
        except Exception,e:
            print 'Try get html page error:' + e.message
    return content

def parseUrl(url):
    html = getPageContent(url)
    result = parse(html)
    if result:
        resStr = ''
        for v in result:
            resStr += v[0] + ':' + v[1] + '\t'
        return resStr
    else:
        return ''

if __name__ == '__main__':
    testUrl = 'http://astro.sina.com.cn/fate_day_Aries/'
    parseUrl(testUrl)

