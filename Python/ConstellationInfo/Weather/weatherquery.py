# -*- coding: utf-8 -*-
import urllib2
import json

def getWeather(apikey,cityName,cityCode):
    #get weather of city in china
    weather = ''
    if(not apikey or not cityName or not cityCode):
        return weather
    try:
        url = 'http://apis.baidu.com/apistore/weatherservice/recentweathers?cityname=%s&cityid=%s' % (cityName,cityCode)
        req = urllib2.Request(url)
        req.add_header("apikey",apikey)
        resp = urllib2.urlopen(req)
        content = resp.read()
        if(content):
            weather = content.decode('utf-8')
    except Exception,e:
        print 'request weather information of [%s] error:%s' % (cityName,e.message)

    return weather

def getWeatherToday(weatherInfo):
    #get weather of today
    data = []
    try:
        jsonObj = json.loads(weatherInfo)
        errNum = jsonObj['errNum']          #error code
        errMsg = jsonObj['errMsg']          #result message
        if(errNum == 0):
            retData = jsonObj['retData']    

            city = retData['city']          #city name
            cityid = retData['cityid']      #city code

            today = retData['today']        
            date = today['date']            #date
            week = today['week']            #week
            curTemp = today['curTemp']      #current temperature
            aqi = today['aqi']              #air quality
            fengxiang = today['fengxiang']  #wind direction
            fengli = today['fengli']        #wind power
            hightemp = today['hightemp']    #max temperature
            lowtemp = today['lowtemp']      #min temperature
            type = today['type']            #weather

            suggestion = []
            index = today['index']
            if(index and len(index)):
                for i in index:
                    name = i['name']            #index of living
                    code = i['code']            #code
                    level = i['index']          #level
                    details = i['details']      #details
                    otherName = i['otherName']  #other
                    suggestion.append((name,code,level,details,otherName))
            
            data.append(city)
            data.append(cityid)
            data.append(date)
            data.append(week)
            data.append(curTemp)
            data.append(aqi)
            data.append(fengxiang)
            data.append(fengli)
            data.append(hightemp)
            data.append(lowtemp)
            data.append(type)
            data.append(suggestion)
        else:
            print 'json status is %s' % errMsg
    except Exception ,e:
        print 'parse json string,get weather of today error??' + e.message
    return data

def getWeatherNextFourDays(weatherInfo):
    #get weather information of next four days
    data = []
    try:
        jsonObj = json.loads(weatherInfo)
        errNum = jsonObj['errNum']          #error code
        errMsg = jsonObj['errMsg']          #error message
        if(errNum == 0):
            retData = jsonObj['retData']    
            forecast = retData['forecast']        
            if(forecast and len(forecast) > 0):
                for f in forecast:
                    date = f['date']            #date
                    week = f['week']            #week
                    fengxiang = f['fengxiang']  #wind direction
                    fengli = f['fengli']        #wind power
                    hightemp = f['hightemp']    #max temperature
                    lowtemp = f['lowtemp']      #min temperature
                    type = f['type']            #weather
                    data.append((date,week,fengxiang,fengli,hightemp,lowtemp,type))

        else:
            print 'json status is %s' % errMsg
    except Exception ,e:
        print 'parse json string,get weather of next 4 days error:' + e.message
    return data

def getWeatherHistorySevenDays(weatherInfo):
    #get weather information of last 7 days
    data = []
    try:
        jsonObj = json.loads(weatherInfo)
        errNum = jsonObj['errNum']          #error code
        errMsg = jsonObj['errMsg']          #error message
        if(errNum == 0):
            retData = jsonObj['retData']    
            history = retData['history']        
            if(history and len(history) > 0):
                for h in history:
                    date = h['date']            #date
                    week = h['week']            #week
                    aqi = h['aqi']              #air quality
                    fengxiang = h['fengxiang']  #wind direction
                    fengli = h['fengli']        #wind power
                    hightemp = h['hightemp']    #max temperature
                    lowtemp = h['lowtemp']      #min temperature
                    type = h['type']            #weather
                    data.append((date,week,aqi,fengxiang,fengli,hightemp,lowtemp,type))

        else:
            print 'json status is %s' % errMsg
    except Exception ,e:
        print '????json???????┣?，7?━?━???????━??:' + e.message
    return data

def getCityInfo(apikey,cityName):
    #query information of city,the city name not contain 'city/town'..(utf-8 urlencode)
    data = []
  
    if(not apikey or not cityName):
        return data
    try:
        cityInfo = ''
        url = 'http://apis.baidu.com/apistore/weatherservice/cityinfo?cityname=' + cityName
        req = urllib2.Request(url)
        req.add_header("apikey", apikey)
        resp = urllib2.urlopen(req)
        content = resp.read()
        if(content):
            cityInfo = content.decode('utf-8')
        if(cityInfo):
            jsonObj = json.loads(cityInfo)
            errNum = jsonObj['errNum']          #error code
            errMsg = jsonObj['retMsg']          #result message
            if(errNum == 0):
                retData = jsonObj['retData']
                
                tempCityName = retData['cityName']      #city name
                cityCode = retData['cityCode']          #city code
                provinceName = retData['provinceName']  #province name
                zipCode = retData['zipCode']            #post code
                telAreaCode = retData['telAreaCode']    #area code
                
                data.append(tempCityName) 
                data.append(cityCode) 
                data.append(provinceName) 
                data.append(zipCode) 
                data.append(telAreaCode) 
            else:
                print 'get information of [%s] fail: parse json string fail' % (cityName)
        else:
            print 'get information of [%s] fail: can`t get information of city' % (cityName)
    except Exception,e:
        print '????[%s]???????━????%s' % (cityName,e.message)
    return data

def getCityList(apikey,cityName):
     #query city list , the city name not contain 'city/town'.. ..(utf-8 urlencode)
    data = []
  
    if(not apikey or not cityName):
        return data
    try:
        cityInfo = ''
        url = 'http://apis.baidu.com/apistore/weatherservice/citylist?cityname=' + encodeName
        
        req = urllib2.Request(url)
        req.add_header("apikey",apikey)
        resp = urllib2.urlopen(req)
        content = resp.read()
        if(content):
            cityInfo = content.decode('utf-8')
        if(cityInfo):
            jsonObj = json.loads(cityInfo)
            errNum = jsonObj['errNum']          #error code
            errMsg = jsonObj['errMsg']          #result message
            if(errNum == 0):
                retData = jsonObj['retData']
                if(retData and len(retData)):
                    for r in retData:
                        province_cn = r['province_cn']  #province 
                        district_cn = r['district_cn']  #area
                        name_cn = r['name_cn']          #chinese name
                        name_en = r['name_en']          #english name
                        area_id = r['area_id']          #area id
                        data.append((province_cn,district_cn,name_cn,name_en,area_id))
                
            else:
                print 'get city list of [%s] fail:%s' % (cityName,errMsg)
        else:
            print 'get city list of [%s] fail:can`t get information' % (cityName)
    except Exception,e:
        print 'get city list of [%s] error:%s' % (cityName,e.message)
    return data

if __name__ == '__main__':
    apiKey = '7a9c88f9af7b5b6f835968c1c60de8a8'
    cityName = ''
    cityCode = '101280601'
    encodeName = (cityName.decode('gbk')).encode('utf-8')
    encodeName = quote(encodeName)
    cityInfo = getCityInfo(apiKey,encodeName)
    if(cityInfo and len(cityInfo) > 0):
        print '<city information>'
        print 'city name:' + cityInfo[0].encode('gb2312')
        print 'city code:' + cityInfo[1].encode('gb2312')
        print 'province :' + cityInfo[2].encode('gb2312')
        print 'post code:' + cityInfo[3].encode('gb2312')
        print 'area code' + cityInfo[4].encode('gb2312')
        print '\n\r'
    else:
        print 'city information: fail \n\r'
    
    cityList = getCityList(apiKey,encodeName)
    if(cityList and len(cityList) > 0):
        print '<city list>'
        for c in cityList:
            print '     province    :' + c[0].encode('gb2312')
            print '     area        :' + c[1].encode('gb2312')
            print '     chiness name:' + c[2].encode('gb2312')
            print '     english name:' + c[3].encode('gb2312')
            print '     area id     :' + c[4].encode('gb2312')
            print '\n\r'
        print '\n\r'
    else:
        print 'get city list :fail \n\r'

    weathderInfo = getWeather(apiKey,cityName,cityCode)
    weatherToday = getWeatherToday(weathderInfo)
    if(weatherToday and len(weatherToday) > 0):
        print '<weather of today>'
        print 'city name 		   :' + weatherToday[0].encode('gb2312')
        print 'city code 		   :' + weatherToday[1].encode('gb2312')
        print 'date      		   :' + weatherToday[2].encode('gb2312')
        print 'week      		   :' + weatherToday[3].encode('gb2312')
        print 'current temperature :' + weatherToday[4].encode('gb2312')
        print 'air quality         :' + weatherToday[5].encode('gb2312')
        print 'wind direction      :' + weatherToday[6].encode('gb2312')
        print 'wind power     	   :' + weatherToday[7].encode('gb2312')
        print 'max temperatur 	   :' + weatherToday[8].encode('gb2312')
        print 'min temperatur 	   :' + weatherToday[9].encode('gb2312')
        print 'weather		       :' + weatherToday[10].encode('gb2312')
  
        print 'index of live :'
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
        print 'weather of today:fail \n\r'

    nextFourDays = getWeatherNextFourDays(weathderInfo)
    if(nextFourDays and len(nextFourDays) > 0):
        print '<weather of next 4 days>'
        for n in nextFourDays:
            print 'data       		 :' + n[0].encode('gb2312')
            print 'week       		 :' + n[1].encode('gb2312')
            print 'wind direction    :' + n[2].encode('gb2312')
            print 'wind power        :' + n[3].encode('gb2312')
            print 'max temperature   :' + n[4].encode('gb2312')
            print 'min temperature   :' + n[5].encode('gb2312')
            print 'wether   	     :' + n[6].encode('gb2312') + '\n\r'
    else:
        print 'weather of next 4 days:fail'

    historySevenDays = getWeatherHistorySevenDays(weathderInfo)
    if(historySevenDays and len(historySevenDays) > 0):
        print '<weather of latest 7 days>'
        for n in historySevenDays:
            print 'data            :' + n[0].encode('gb2312')
            print 'week            :' + n[1].encode('gb2312')
            print 'air quality     :' + n[2].encode('gb2312')
            print 'wind direction  :' + n[3].encode('gb2312')
            print 'wind power      :' + n[4].encode('gb2312')
            print 'max temperature :' + n[5].encode('gb2312')
            print 'min temperature :' + n[6].encode('gb2312')
            print 'weather         :' + n[7].encode('gb2312') + '\n\r'
    else:
        print 'weather of latest 7 days:fail'