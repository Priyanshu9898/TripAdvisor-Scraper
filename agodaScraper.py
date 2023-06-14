from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://www.agoda.com/en-in/lords-plaza-surat/hotel/surat-in.html?finalPriceView=1&isShowMobileAppPrice=false&cid=1891461&numberOfBedrooms=&familyMode=false&adults=2&children=0&rooms=1&maxRooms=0&checkIn=2023-06-22&isCalendarCallout=false&childAges=&numberOfGuest=0&missingChildAges=false&travellerType=1&showReviewSubmissionEntry=false&currencyCode=INR&isFreeOccSearch=false&tag=3cda3586-9ec8-88d2-2819-7b1e8bb3ad04&isCityHaveAsq=false&tspTypes=7,2,-1,-1&los=1&searchrequestid=8f1f3229-eefe-4385-b879-11d53c339799"


def fetchAndSaveData(url, path):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
     
    r = requests.get(url,headers=headers)
    
    print(r)
    
    with open(path, "w", encoding='utf-8') as f:
        f.write(r.text)

fetchAndSaveData(url, "data/agoda.html")


with open('data/agoda.html', 'r', encoding='utf-8') as f:
    data = f.read()

soup = BeautifulSoup(data, "lxml")

# print(soup.prettify())

reviewBox = soup.find_all("span" , class_="Review__SummaryContainer")

print(reviewBox)