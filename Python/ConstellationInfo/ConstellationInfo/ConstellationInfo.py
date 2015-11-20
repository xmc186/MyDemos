import sys
import parse
#file = open('tmp')
urls = []
urls.append(('aries','http://astro.sina.com.cn/fate_day_Aries/'))
urls.append(('taurus','http://astro.sina.com.cn/fate_day_Taurus/'))
urls.append(('gemini','http://astro.sina.com.cn/fate_day_Gemini/'))
urls.append(('cancer','http://astro.sina.com.cn/fate_day_Cancer/'))
urls.append(('leo','http://astro.sina.com.cn/fate_day_leo/'))
urls.append(('virgo','http://astro.sina.com.cn/fate_day_Virgo/'))
urls.append(('libra','http://astro.sina.com.cn/fate_day_Libra/'))
urls.append(('scorpio', 'http://astro.sina.com.cn/fate_day_Scorpio/'))
urls.append(('sagittarius','http://astro.sina.com.cn/fate_day_Sagittarius/'))
urls.append(('capricorn','http://astro.sina.com.cn/fate_day_Capricorn/'))
urls.append(('aquarius','http://astro.sina.com.cn/fate_day_Aquarius/'))
urls.append(('pisces','http://astro.sina.com.cn/fate_day_Pisces/'))

strLines = []
for v in urls:
    url = v[1]
    res = parse.parseUrl(url)
    fullRes = 'name:' + v[0] + '\t' + res
    strLines.append(fullRes)

try:
   fh = open("temp.txt", "a")
   try:
       for l in strLines:
           fh.write(l.encode('utf-8') + '\n')
   finally:
      print "Going to close the file"
      fh.close()
except IOError:
   print "Error: can\'t find file or read data"