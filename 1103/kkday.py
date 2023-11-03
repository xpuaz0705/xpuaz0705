# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 20:34:35 2023

@author: USER
"""
from bs4 import BeautifulSoup
import requests

url = 'https://www.kkday.com/zh-tw/area_api/ajax_get_page_data?countryCode=A01-001&cityCode=A01-001-00018'

header = {
    'Cookie':'csrf_cookie_name=9e1349ac30454203bf4a499b747ee195; KKWEB=a%3A4%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22f355d2707c0d9160ed3c43d7312d805a%22%3Bs%3A7%3A%22channel%22%3Bs%3A5%3A%22GUEST%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1699014426%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7Dde5e4f529503eddeda8484d1f495b028; country_lang=zh-tw; currency=TWD; CID=7725; UD1=tw; UD2=crazy; KKUD=f355d2707c0d9160ed3c43d7312d805a; _gcl_au=1.1.1417361994.1699014428; _gcl_aw=GCL.1699014429.Cj0KCQjwtJKqBhCaARIsAN_yS_knl14S1ifZQFqSXWkW5WqWYu52Bd8mEu0Sv74JBwolS0WEStNSsikaAusvEALw_wcB; _gid=GA1.2.1084304861.1699014429; _gac_UA-49763723-1=1.1699014429.Cj0KCQjwtJKqBhCaARIsAN_yS_knl14S1ifZQFqSXWkW5WqWYu52Bd8mEu0Sv74JBwolS0WEStNSsikaAusvEALw_wcB; _gac_UA-117438867-1=1.1699014429.Cj0KCQjwtJKqBhCaARIsAN_yS_knl14S1ifZQFqSXWkW5WqWYu52Bd8mEu0Sv74JBwolS0WEStNSsikaAusvEALw_wcB; _hjFirstSeen=1; _hjIncludedInSessionSample_628088=0; _hjSession_628088=eyJpZCI6Ijk2OTA1MzI1LTlkYWEtNDJiMS1hYWU4LWFhY2QzOGY2N2RiYSIsImNyZWF0ZWQiOjE2OTkwMTQ0Mjg3MDIsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6dHJ1ZX0=; _hjAbsoluteSessionInProgress=0; _fbp=fb.1.1699014428714.1478213441; rskxRunCookie=0; rCookie=yveo6jqjhdf069e0q3x44owloilbo66; _ga=GA1.2.1488266297.1699014428; _hjSessionUser_628088=eyJpZCI6IjkwODdmMWE0LTQ0YWYtNWEwMS1iYmZjLTUxNzYyNzhjNThiZSIsImNyZWF0ZWQiOjE2OTkwMTQ0Mjg3MDEsImV4aXN0aW5nIjp0cnVlfQ==; lastRskxRun=1699014872039; CookieConsent={stamp:%27h+FgiFCu9vNpvj8Wu7bPOmIx00KAG2YAOyqPSw3yIgQOCIZpCxGMTw==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1699014872621%2Cregion:%27tw%27}; datadome=vjU9qHQBuTURXEY9plGNJqfOLi2dQGEvN4hYl1KBMZNRhv7HsAbY7RRLs0Mvb~59bUpYKca1BIXSsgaTZj22FOB0KItKDw9t4W8q7PnGKdpeOVyo4BGkq9eBel3~iIix; _ga_RJJY5WQFKP=GS1.1.1699014428.1.1.1699015088.60.0.0',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'    
    }

data = requests.get(url,headers=header).text
print(data)