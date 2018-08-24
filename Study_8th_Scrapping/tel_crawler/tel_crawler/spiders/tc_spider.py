# real command >> scrapy crawl TelephoneNo -o pl.csv
import scrapy
from selenium import webdriver
import time
from scrapy.selector import Selector

from tel_crawler.items import TCItem

class TCSpider(scrapy.Spider):
    name = "TelephoneNo"
    allowed_domains = ["114.co.kr"]
    start_urls = [
        # "https://www.114.co.kr/search/list.do?menuKey=116&searchWord=%EA%B4%91%ED%99%94%EB%AC%B8%EC%9A%B0%EC%B2%B4%EA%B5%AD#none"
        # "https://www.114.co.kr/search/list.do?menuKey=116&searchWord=광화문우체국#none"
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=인천부평5동우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=인천불로우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=인천삼덕아파트우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=인천신현동우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=인천연세대학교우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=인천연수2동우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=인천용현5동우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=인천운서동우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=인천유통센타우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=인천일신풍림우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=인천임학동우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=인천작전동우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=인천주안4동우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=인천주안8동우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=인천지방법원우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=인천지법부천지원우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=인천학익동우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=인하대학교우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=정부과천청사우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=정선애산우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제101군사우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제103군사우편출장소#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제105군사우편출장소#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제108군사우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제109군사우편출장소#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제114군사우편출장소#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제117군사우편출장소#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제123군사우편출장소#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제133군사우편출장소#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제138군사우편출장소#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제308군사우편출장소#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제309군사우편출장소#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제310군사우편출장소#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제31군사우편출장소#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제334군사우편출장소#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제383군사우편출장소#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제384군사우편출장소#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제502군사우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제505군사우편출장소#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제604군사우편출장소#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제71군사우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제76군사우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제78군사우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제800군사우편출장소#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제81군사우편출장소#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제82군사우편출장소#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제92군사우편출장소#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제97군사우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제천동현동우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제천서부우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=제천신백동우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=중부광역물류센터#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=진천초평우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=천안단국대학교우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=천안백석농공단지우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=천안산업단지우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=천안상명대학교우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=천안서부우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=천안신당동우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=천안한국기술대학교우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=청원화상우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=청주개신동우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=청주금천동우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=청주남이우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=청주남일우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=청주내덕동우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=청주대학교우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=청주분평동우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=청주사직동우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=청주석교동우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=청주시청우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=청주옥산우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=청주운천아파트우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=춘천남산우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=춘천석사동우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=춘천신북우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=춘천한계울우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=충남대학교우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=충남도청출장소#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=충북대학교우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=충주성내동우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=태백구문소동우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=태백황지동우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=택배방#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=파주광탄우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=파주금촌3동우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=파주동패우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=평택LG전자우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=평택대학교우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=평택서정우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=평택세교동우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=평택안정우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=평택이충동우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=평택하북우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=평택합정동우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=평택현화우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=포천선단우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=포천송우우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=포천이동우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=포천일동우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=하남석해우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=한국과학기술원우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=한국교원대학교우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=한국교통대학교우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=한국방송통신대학우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=한남대학교우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=한림대우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=한밭대학교우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=한밭산성우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=한신대학교우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=호서대학교우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=홍성금당우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=홍성남장우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=홍성역전우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=홍천갈마곡우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=화성동탄3동우체국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=화성와우우편취급국#none', 
        'https://www.114.co.kr/search/list.do?menuKey=116&searchWord=횡성북천우편취급국#none'
    ]

    def __init__(self):
        scrapy.Spider.__init__(self)
        self.browser = webdriver.Chrome(r"c:\util\chromedriver.exe")

    def parse(self, response):
        self.browser.get(response.url)
        time.sleep(3)

        html = self.browser.find_element_by_xpath('//*').get_attribute('outerHTML')
        selector = Selector(text=html)
        rows = selector.xpath('//*[@id="normalUl"]')

        for row in rows:
            item = TCItem() 
            item["officeName"] = row.xpath('./li[2]/dl/dt/a/text()')[0].extract()
            item["officeAddr"] = row.xpath('./li[2]/dl/dd/p/span/text()')[0].extract()
            item["telephoneNo"] = row.xpath('./li[2]/dl/dd/a[3]/text()')[0].extract()
            yield item
