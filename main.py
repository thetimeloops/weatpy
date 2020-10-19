import requests as req
from bs4 import BeautifulSoup as bs
while True:
    location = input("Whats yo location: ")
    header = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
    output = req.get("http://www.google.com/search",params={'q':f"{location} weather"},headers=header)
    parsed = bs(output.text, "html.parser")
    try:
        found_class=parsed.find("span",{"id":"wob_tm"})
        found_class2=parsed.find("div",{"id":"wob_loc"})
        print(found_class.text)
        print(found_class2.text)
        print("------------------------------")
        print(parsed.find("div",{"id":"wob_wc"}).text)
        break
    except:
        print(f"{location} is not a location")
#location = output.text.find("°C")
#print(output.text[location-2]+output.text[location-1])
