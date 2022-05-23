from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from twilio.rest import Client

client = Client("TWILIO_CLIENT", "TWILIO_CLIENT")
driver = webdriver.Chrome(executable_path='PATH_TO_CHROME_DRIVER')
urlList = ["https://www.bestbuy.com/site/dune-steelbook-includes-digital-copy-4k-ultra-hd-blu-ray-blu-ray-includes-digital-copy-2021/6488959.p?skuId=6488959"]

itemDict = {}

for url in urlList:
    driver.get(url)

    el = driver.find_element_by_tag_name('body')
    str = el.text

    if(str.find("Pre-Order") == -1):
        if (str.find("Add to Cart") == -1): 
            itemDict[driver.title] = "not available :( \n" + url
        else:
            itemDict[driver.title] = "Available!\n" + url
    else:
        itemDict[driver.title] = "Available!\n" + url

driver.close()

results = ""
for x in itemDict.keys():
    results += x
    results += ": " + itemDict[x] + "\n" 

client.messages.create(to = "+PHONE_NUMBER_HERE", from_ = "+PHONE_NUMBER_HERE", body = results)