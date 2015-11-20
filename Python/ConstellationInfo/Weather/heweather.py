# -*- coding: utf-8 -*-
import urllib2
import json

def getWeather(apikey,city):
    #get weather
    weather = ''
    if(not apikey and not city):
        return weather
    try:
        url = 'http://apis.baidu.com/heweather/weather/free?city=%s' % city
        req = urllib2.Request(url)
        req.add_header("apikey",apikey)
        resp = urllib2.urlopen(req)
        content = resp.read()
        if(content):
            weather = content.decode('utf-8')
    except Exception,e:
        print 'request weather information of [%s] error:%s' % (city,e.message)

    return weather

def getBaseInfo(weatherInfo):
    #get basic information of city
    baseInfo = []
    if(not weatherInfo):
        return weatherInfo
    try:
        jsonObj = json.loads(weatherInfo)
        weather = jsonObj['HeWeather data service 3.0'][0]
        status = weather['status']
        if(status == 'ok'):
            basic = weather['basic']

            city = basic['city']    #city name
            cnty = basic['cnty']    #country
            id = basic['id']        #city id
            lat = basic['lat']      #latitude
            lon = basic['lon']      #lontitude

            update = basic['update']
            loc = update['loc']     #location tim
            utc = update['utc']     #UTC time

            baseInfo.append(city)
            baseInfo.append(cnty)
            baseInfo.append(id)
            baseInfo.append(lat)
            baseInfo.append(lon)
            baseInfo.append(loc)
            baseInfo.append(utc)
        else:
            print 'json status is %s' % status
    except Exception ,e:
        print 'parse json,get basic information error :' + e.message
    return baseInfo

def getWeatherNow(weatherInfo):
    #weather of now
    weatherNow = []
    if(not weatherInfo):
        return weatherNow
    try:
        jsonObj = json.loads(weatherInfo)
        weather = jsonObj['HeWeather data service 3.0'][0]
        status = weather['status']
        if(status == 'ok'):
            nowInfo = weather['now']
            cond = nowInfo['cond']
            condCode = cond['code']     #weather code
            condTxt = cond['txt']       #weather description
            
            fl = nowInfo['fl']          #feels like
            hum = nowInfo['hum']        #relative humidity(%)
            pcpn = nowInfo['pcpn']      #precipitation(mm)
            pres = nowInfo['pres']      #air pressure
            tmp = nowInfo['tmp']        #temperature
            vis = nowInfo['vis']        #visibility(km)
            wind = nowInfo['wind']
            windDeg = wind['deg']       #wind direction (306 deg)
            windDir = wind['dir']       #wind direction
            windSc = wind['sc']         #wind power
            windSpd = wind['spd']       #wind speed(kmph)
            
            weatherNow.append(condCode)
            weatherNow.append(condTxt)

            weatherNow.append(fl)
            weatherNow.append(hum)

            weatherNow.append(pcpn)
            weatherNow.append(pres)
            weatherNow.append(tmp)
            weatherNow.append(vis)

            weatherNow.append(windDeg)
            weatherNow.append(windDir)
            weatherNow.append(windSc)
            weatherNow.append(windSpd)

        else:
            print 'json status is %s' % status
    except Exception,e:
        print 'parse json,get weather of now error :' + e.message

    return weatherNow

def getAirQuality(weatherInfo):
    #get air quality, for china only
    airQuality = []
    if(not weatherInfo):
        return weatherInfo
    try:
        jsonObj = json.loads(weatherInfo)
        weather = jsonObj['HeWeather data service 3.0'][0]
        status = weather['status']
        if(status == 'ok'):
            qirInfo = weather['aqi']
            city = qirInfo['city']

            aqi = city['aqi']   #air quality index
            co = city['co']     #The average carbon monoxide for 1 hour(ug/m2)
            no2 = city['no2']   #The average nitrogen dioxide for 1 hour(ug/m2)
            o3 = city['o3']     #The average ozone for 1 hour(ug/m2)
            pm10 = city['pm10'] #The average PM1.0 for 1 hour(ug/m2)
            pm25 = city['pm25'] #The average PM2.5 for 1 hour(ug/m2)
            qlty = city['qlty'] #Air quality category
            so2 = city['so2']   #The average sulfur dioxide for 1 hour(ug/m2)

            airQuality.append(aqi)
            airQuality.append(co)
            airQuality.append(no2)
            airQuality.append(o3)
            airQuality.append(pm10)
            airQuality.append(pm25)
            airQuality.append(qlty)
            airQuality.append(so2)
        else:
            print 'json status is %s' % status
    except Exception ,e:
        print 'parse json, get air quality error:' + e.message
    return airQuality

def getHourlyForecast(weatherInfo):
    #get weather per hour(3 hour)
    data = []
    if(not weatherInfo):
        return weatherInfo
    try:
        jsonObj = json.loads(weatherInfo)
        weather = jsonObj['HeWeather data service 3.0'][0]
        status = weather['status']
        if(status == 'ok'):
            hourly_forecast = weather['hourly_forecast']
            if(hourly_forecast and len(hourly_forecast) > 0):
                for hourData in hourly_forecast:
                    date = hourData['date']		#date
                    hum = hourData['hum']		#relative humidity
                    pop = hourData['pop']		#probability of precipitation
                    pres = hourData['pres']		#air pressure
                    tmp = hourData['tmp']		#temperature

                    wind = hourData['wind']		
                    windDeg = wind['deg']		#wind direction (360deg)
                    windDir = wind['dir']		#wind direction
                    windSc = wind['sc']			#wind power
                    windSpd = wind['spd']		#wind speed
                    data.append((date,hum,pop,pres,tmp,windDeg,windDir,windSc,windSpd))

        else:
            print 'json status is %s' % status
    except Exception ,e:
        print 'parse json,get weather per hour error??' + e.message
    return data

def getDaylyForecast(weatherInfo):
    #weather of 7 days
    data = []

    try:
        jsonObj = json.loads(weatherInfo)
        weather = jsonObj['HeWeather data service 3.0'][0]
        status = weather['status']
        if(status == 'ok'):
            daily_forecast = weather['daily_forecast']
            if(daily_forecast and len(daily_forecast) > 0):
                for dayData in daily_forecast:
                    date = dayData['date']      #date

                    astro = dayData['astro']
                    astro_sr = astro['sr']      #sunrise time
                    astro_ss = astro['ss']      #sunset time 

                    cond = dayData['cond']
                    code_d = cond['code_d']     #weather code of daytime
                    code_n = cond['code_n']     #weather code of night
                    txt_d = cond['txt_d']       #weather of daytime
                    txt_n = cond['txt_n']       #weather of night

                    hum = dayData['hum']        #relative humidity
                    pcpn = dayData['pcpn']      #precipitation
                    pop = dayData['pop']        #probability of precipitation
                    pres = dayData['pres']      #air pressure
                    vis = dayData['vis']        #visibility

                    tmp = dayData['tmp']
                    tem_min = tmp['min']        #min temperature
                    tem_max = tmp['max']        #max temperature

                    wind = dayData['wind']      
                    wind_deg = wind['deg']      #wind direction (360deg)
                    wind_dir = wind['dir']      #wind direction
                    wind_sc = wind['sc']        #wind power
                    wind_spd = wind['spd']      #wind speed

                    data.append((date,astro_sr,astro_ss,code_d,code_n,txt_d,txt_n,hum,pcpn,pop,pres,vis,tem_min,tem_max,wind_deg,wind_dir,wind_sc,wind_spd))

        else:
            print 'json status is %s' % status
    except Exception ,e:
        print 'parse json,get weather of 7 days error??' + e.message
    return data

def getSuggestion(weatherInfo):
    #get suggestion 
    data = []

    if(not weatherInfo):
        return weatherInfo
    try:
        jsonObj = json.loads(weatherInfo)
        weather = jsonObj['HeWeather data service 3.0'][0]
        status = weather['status']
        if(status == 'ok'):
            suggestion = weather['suggestion']
            
            comf = suggestion['comf'] 
            comf_brf = comf['brf']
            comf_txt = comf['txt']

            cw = suggestion['cw']
            cw_brf = cw['brf']
            cw_txt = cw['txt']

            drsg = suggestion['drsg']
            drsg_brf = drsg['brf']
            drsg_txt = drsg['txt']

            flu = suggestion['flu']
            flu_brf = flu['brf']
            flu_txt = flu['txt']

            sport = suggestion['sport']
            sport_brf = sport['brf']
            sport_txt = sport['txt']

            trav = suggestion['trav']
            trav_brf = trav['brf']
            trav_txt = trav['txt']

            uv = suggestion['uv']
            uv_brf = uv['brf']
            uv_txt = uv['txt']

            data.append((comf_brf,comf_txt))
            data.append((cw_brf,cw_txt))
            data.append((drsg_brf,drsg_txt))
            data.append((flu_brf,flu_txt))
            data.append((sport_brf,sport_txt))
            data.append((trav_brf,trav_txt))
            data.append((uv_brf,uv_txt))
        else:
            print 'json status is %s' % status
    except Exception ,e:
        print 'parse json,get suggestion error:' + e.message
    return data

if __name__ == '__main__':
    apiKey = '7a9c88f9af7b5b6f835968c1c60de8a8'
    city = 'shenzhen'
    
    weatherInfo = getWeather(apiKey,city)
    weatherNow = getWeatherNow(weatherInfo)
    if(weatherNow and len(weatherNow) > 0):
        print '<weather now>' 
        print 'weather code 	 :' + weatherNow[0].encode('gb2312') 
        print 'weater       	 :' + weatherNow[1].encode('gb2312')
        print 'feels like   	 :' + weatherNow[2].encode('gb2312') 
        print 'relative humidity :' + weatherNow[3].encode('gb2312')
        print 'precipitation	 :' + weatherNow[4].encode('gb2312') 
        print 'air pressure	 	 :' + weatherNow[5].encode('gb2312')
        print 'temperature		 :' + weatherNow[6].encode('gb2312') 
        print 'visibility		 :' + weatherNow[7].encode('gb2312') 
        print 'wind deg			 :' + weatherNow[8].encode('gb2312') 
        print 'wind direction	 :' + weatherNow[9].encode('gb2312')
        print 'wind power		 :' + weatherNow[10].encode('gb2312')
        print 'wind speed		 :' + weatherNow[11].encode('gb2312')
        print '\n\r'
    else:
        print 'weather now:fail'


    airQuality = getAirQuality(weatherInfo)
    if(airQuality and len(airQuality) > 0):
        print '<air quality>'
        print 'air quality index:' + airQuality[0].encode('gb2312') 
        print 'The average carbon monoxide for 1 hour(ug/m2):' + airQuality[1].encode('gb2312')
        print 'The average nitrogen dioxide for 1 hour(ug/m2):' + airQuality[2].encode('gb2312') 
        print 'The average ozone for 1 hour(ug/m2):' + airQuality[3].encode('gb2312')
        print 'The average PM1.0 for 1 hour(ug/m2):' + airQuality[4].encode('gb2312') 
        print 'The average PM2.5 for 1 hour(ug/m2):' + airQuality[5].encode('gb2312')
        print 'Air quality category:' + airQuality[6].encode('gb2312') 
        print 'The average sulfur dioxide for 1 hour(ug/m2):' + airQuality[7].encode('gb2312') 
        print '\n\r'
    else:
        print 'air quality:fail'

    baseInfo = getBaseInfo(weatherInfo)
    if(baseInfo and len(baseInfo) > 0):
        print '<basic information>'
        print 'city name	 :' + baseInfo[0].encode('gb2312') 
        print 'country		 :' + baseInfo[1].encode('gb2312')
        print 'city id		 :' + baseInfo[2].encode('gb2312') 
        print 'latitude		 :' + baseInfo[3].encode('gb2312')
        print 'lontitude	 :' + baseInfo[4].encode('gb2312') 
        print 'location time :' + baseInfo[5].encode('gb2312')
        print 'UTC time  	 :' + baseInfo[6].encode('gb2312') 
        print '\n\r'
    else:
        print 'basic information:fail'
        
    hourInfos = getHourlyForecast(weatherInfo)
    if(hourInfos and len(hourInfos) > 0):
        print '<1/3 hour weather>'
        for hData in hourInfos:
            print 'date							:' + hData[0].encode('gb2312') 
            print 'relative humidity			:' + hData[1].encode('gb2312')
            print 'probability of precipitation :' + hData[2].encode('gb2312') 
            print 'air pressure					:' + hData[3].encode('gb2312')
            print 'temperature					:' + hData[4].encode('gb2312') 
            print 'wind deg						:' + hData[5].encode('gb2312')
            print 'wind direction				:' + hData[6].encode('gb2312') 
            print 'wind power					:' + hData[7].encode('gb2312') 
            print 'wind speed					:' + hData[8].encode('gb2312') + '\n\r'
        print '\n\r'
    else:
        print '1/3 hour weather:fail'

    daylyInfo = getDaylyForecast(weatherInfo)
    if(daylyInfo and len(daylyInfo) > 0):
        print '<7 days weather>'
        for dayInfo in daylyInfo:
            print 'date							:' + dayInfo[0].encode('gb2312') 
            print 'sunrise time					:' + dayInfo[1].encode('gb2312')
            print 'sunset time					:' + dayInfo[2].encode('gb2312') 
            print 'weather code of daytime 		:' + dayInfo[3].encode('gb2312')
            print 'weather code of night		:' + dayInfo[4].encode('gb2312') 
            print 'weather of daytime			:' + dayInfo[5].encode('gb2312')
            print 'weather of night				:' + dayInfo[6].encode('gb2312') 
            print 'relative humidity			:' + dayInfo[7].encode('gb2312') 
            print 'precipitation				:' + dayInfo[8].encode('gb2312') 
            print 'probability of precipitation :' + dayInfo[9].encode('gb2312') 
            print 'air pressure					:' + dayInfo[10].encode('gb2312') 
            print 'visibility					:' + dayInfo[11].encode('gb2312') 
            print 'min temperature				:' + dayInfo[12].encode('gb2312') 
            print 'max temperature				:' + dayInfo[13].encode('gb2312') 
            print 'wind deg						:' + dayInfo[14].encode('gb2312') 
            print 'wind direction				:' + dayInfo[15].encode('gb2312') 
            print 'wind power					:' + dayInfo[16].encode('gb2312') 
            print 'wind speed					:' + dayInfo[17].encode('gb2312') + '\n\r'
        print '\n\r'
    else:
        print '7 days weather:fail'

    suggestion = getSuggestion(weatherInfo)
    if(suggestion and len(suggestion) >= 7):
        print '<index of life>'
        print 'comfort index	:' 
        print '     ' + suggestion[0][0].encode('gb2312') 
        print '     ' + suggestion[0][1].encode('gb2312') 
        print 'washing index	:' 
        print '     ' + suggestion[1][0].encode('gb2312') 
        print '     ' + suggestion[1][1].encode('gb2312')
        print 'dressing index	:' 
        print '     ' + suggestion[2][0].encode('gb2312') 
        print '     ' + suggestion[2][1].encode('gb2312') 
        print 'cold index		:' 
        print '     ' + suggestion[3][0].encode('gb2312') 
        print '     ' + suggestion[3][1].encode('gb2312')  
        print 'motility index	:' 
        print '     ' + suggestion[4][0].encode('gb2312') 
        print '     ' + suggestion[4][1].encode('gb2312')  
        print 'trip index		:' 
        print '     ' + suggestion[5][0].encode('gb2312') 
        print '     ' + suggestion[5][1].encode('gb2312')   
        print 'ultraviolet light:'
        print '     ' + suggestion[6][0].encode('gb2312') 
        print '     ' + suggestion[6][1].encode('gb2312')   
        print '\n\r'
    else:
        print 'index of life:fail'