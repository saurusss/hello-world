from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus

url = 'http://api.seibro.or.kr/openapi/service/StockSvc/getStkIsinByNmN1'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '서비스키', quote_plus('secnNm') : '삼성' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print(response_body)