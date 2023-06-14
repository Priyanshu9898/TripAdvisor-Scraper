from types import NoneType
from bs4 import BeautifulSoup
import pandas as pd
import requests
import math

url = "https://www.tripadvisor.com/Hotel_Review-g297612-d12962806-Reviews-or0-Courtyard_by_Marriott_Surat-Surat_Surat_District_Gujarat.html#REVIEWS"


def fetchAndSaveData(url, path):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
     
    r = requests.get(url,headers=headers)
    
    print(r)
    
    with open(path, "w", encoding='utf-8') as f:
        f.write(r.text)

fetchAndSaveData(url, "data/tripAdvisor.html")


with open('data/tripAdvisor.html', 'r', encoding='utf-8') as f:
    data = f.read()

soup = BeautifulSoup(data, "lxml")


hotel_name = soup.find('h1', class_="biGQs").text
print("Hotel Name",  hotel_name)

hotel_address = soup.find('span', class_="oAPmj").text
print("Hotel Address", hotel_address)

hotel_rating = soup.find('span', class_="uwJeR").text
print("Hotel Rating", hotel_rating)

total_reviews = soup.find('span', class_="hkxYU").text
# print(total_reviews)

TotalNoReviews = total_reviews.split(" ")[0]
TotalNoReviews = int(TotalNoReviews.replace(",", ""))
print("Total No. of Reviews", TotalNoReviews)

TotalPages = math.ceil(TotalNoReviews/10);

print("Total Pages", TotalPages)


reviews_author = []
reviews_title = []
reviews_description = []
reviews_date = []
reviews_type = []
reviews_response = []
review_rating = []

for i in range(138, TotalPages):
    url = f"https://www.tripadvisor.com/Hotel_Review-g297612-d12962806-Reviews-or{i*10}-Courtyard_by_Marriott_Surat-Surat_Surat_District_Gujarat.html#REVIEWS"
    
    print(url)
    
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
     
    r = requests.get(url,headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    
    container = soup.find_all("div", class_="YibKl")

    for item in container:
        author = item.find('a', class_="ui_header_link").text
        title = item.find("div", class_="KgQgP").text
        description = item.find("span", class_="QewHA").text
        date = item.find("span", class_="teHYY").text.split(":")[1].strip()
        type=""
        if(item.find("span", class_="TDKzw")):
            type = item.find("span", class_="TDKzw").text.split(":")[1].strip()
            
        responseBox = item.find("div", class_="ajLyr")
        response = ""
        
        if(responseBox != NoneType):
            if(responseBox.find("span", class_="MInAm")):
                res = responseBox.find("span", class_="MInAm").text
            
                if(len(res) > 0):
                    response = res

        reviews_author.append(author)
        reviews_title.append(title)
        reviews_description.append(description)
        reviews_date.append(date)
        reviews_type.append(type)
        # reviews_response.append(response)
    
print(len(reviews_author))

data = {
    "Hotel Name": [hotel_name] + [""] * (len(reviews_author) - 1),
    "Hotel Address": [hotel_address] + [""] * (len(reviews_author) - 1),
    "Hotel Rating": [hotel_rating] + [""] * (len(reviews_author) - 1),
    "Author": reviews_author,
    "Review Rating": review_rating,
    "Review Title": reviews_title,
    "Review Description": reviews_description,
    "type": reviews_type,
    "Date": reviews_date,
    "Response": reviews_response
}

# Create the DataFrame
df = pd.DataFrame(data)

df.to_csv("output.csv", index=False)