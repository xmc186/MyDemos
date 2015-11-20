import heweather
import weatherquery
from urllib import quote
apiKey = '7a9c88f9af7b5b6f835968c1c60de8a8' 
cityName = '????'
cityCode = '101280601'
cityPintYin = 'shenzhen'

weatherInfo = heweather.getWeather(apiKey,cityPintYin)
if(weatherInfo):
    weatherNow = heweather.getWeatherNow(weatherInfo)
    if(weatherNow and len(weatherNow) > 0):
        print '<weather now>' 
        print 'weather code   	 :' + weatherNow[0].encode('gb2312') 
        print 'weather       	 :' + weatherNow[1].encode('gb2312') 
        print 'feels like        :' + weatherNow[2].encode('gb2312') 
        print 'relative humidity :' + weatherNow[3].encode('gb2312')
        print 'precipitation     :' + weatherNow[4].encode('gb2312') 
        print 'air pressure      :' + weatherNow[5].encode('gb2312')
        print 'temperature       :' + weatherNow[6].encode('gb2312') 
        print 'visibility        :' + weatherNow[7].encode('gb2312') 
        print 'wind deg       	 :' + weatherNow[8].encode('gb2312') 
        print 'wind direction    :' + weatherNow[9].encode('gb2312')
        print 'wind power        :' + weatherNow[10].encode('gb2312')
        print 'wind speed        :' + weatherNow[11].encode('gb2312')
        print '\n\r'
    else:
        print 'weather now:fail'


encodeName = (cityName.decode('gbk')).encode('utf-8')
encodeName = quote(encodeName)
weatherQuery = weatherquery.getWeather(apiKey,encodeName,cityCode)
if(weatherQuery):
    weatherToday = weatherquery.getWeatherToday(weatherQuery)
    if(weatherToday and len(weatherToday) > 0):
        print '<weather today>'
        print 'city name 		   :' + weatherToday[0].encode('gb2312')
        print 'city code 		   :' + weatherToday[1].encode('gb2312')
        print 'date 		       :' + weatherToday[2].encode('gb2312')
        print 'week    			   :' + weatherToday[3].encode('gb2312')
        print 'current temperature :' + weatherToday[4].encode('gb2312')
        print 'air quality		   :' + weatherToday[5].encode('gb2312')
        print 'wind direction      :' + weatherToday[6].encode('gb2312')
        print 'wind speed     	   :' + weatherToday[7].encode('gb2312')
        print 'max temperature 	   :' + weatherToday[8].encode('gb2312')
        print 'min temperature 	   :' + weatherToday[9].encode('gb2312')
        print 'weather     		   :' + weatherToday[10].encode('gb2312')
  
        print 'index of life 	   :'
        suggeston = weatherToday[11]
        if(suggeston and len(suggeston) > 0):
            for s in suggeston:
                print '     ' + s[0].encode('gb2312')
                print '     ' + s[1].encode('gb2312')
                print '     ' + s[2].encode('gb2312')
                print '     ' + s[3].encode('gb2312')
                print '     ' + s[4].encode('gb2312') + '\n\r'
        print '\n\r'
    else:
        print 'weather today:fail \n\r'