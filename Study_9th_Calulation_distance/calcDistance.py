from math import sin, cos, sqrt, atan2, radians 
# approximate radius of earth in km
R = 6373.0 
# lat1 = radians(52.2296756) 
# lon1 = radians(21.0122287) 
# lat2 = radians(52.406374) 
# lon2 = radians(16.9251681) 

# lat1 = radians(37.8821732	) #가평북면우체국
# lon1 = radians( 127.5473771)
# lat2 = radians( 37.8310677	) # 가평우체국
# lon2 = radians( 127.5107432)
# # 엑셀 계산 6,540

lat1 = radians( 37.6858862	) # 고양가좌동(취)
lon1 = radians( 126.7194845)
lat2 = radians( 37.6829634	) # 고양대화동우체국
lon2 = radians( 126.7555092 )
# 엑셀 계산 3,219

dlon = lon2 - lon1 
dlat = lat2 - lat1
a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * \
   sin(dlon / 2)**2 
c = 2 * atan2(sqrt(a), sqrt(1 - a)) 
distance = R * c 
print("Result:", distance) 
print("Should be:", 278.546, "km")
# 파이썬 계산 6,531