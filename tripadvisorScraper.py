from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://www.tripadvisor.com/Hotel_Review-g297612-d12962806-Reviews-Courtyard_by_Marriott_Surat-Surat_Surat_District_Gujarat.html"


def fetchAndSaveData(url, path):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
     
    r = requests.get(url,headers=headers)
    
    # print(r)
    
    with open(path, "w", encoding='utf-8') as f:
        f.write(r.text)

# fetchAndSaveData(url, "data/trip.html")


with open('data/trip.html', 'r', encoding='utf-8') as f:
    data = f.read()

soup = BeautifulSoup(data, "lxml")

# print(soup.prettify())

hotel_name = soup.find('h1', class_="biGQs").text
print(hotel_name)

hotel_rating = soup.find('span', class_="uwJeR").text
print(hotel_rating)

hotel_address = soup.find('span', class_="oAPmj").text
print("Hotel Address", hotel_address)

total_reviews = soup.find('span', class_="hkxYU").text
# print(total_reviews)

TotalNoReviews = total_reviews.split(" ")[0]
TotalNoReviews = int(TotalNoReviews.replace(",", ""))
print(TotalNoReviews)

reviews = soup.find_all('div', class_="YibKl")

review_title = []
review_description = []

titles = soup.find_all('a', class_="Qwuub")

for title in titles:
    review_title.append(title.text)

# print(review_title)
print(len(review_title))



descriptions = soup.find_all('span', class_="QewHA")


for description in descriptions:
    review_description.append(description.text)

# print(review_description)
print(len(review_description))

reviews_author = []
reviews_title = []
reviews_description = []
reviews_date = []
reviews_type = []
reviews_response = []

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
    res = responseBox.find("span", class_="MInAm").text
        
    if(len(res) > 0):
        response = res
    
    ratingBox = item.find("span", class_="ui_bubble_rating")

    span_classes = ratingBox['class']
    
    if(len(span_classes) == 2):
        rating = span_classes[1].split("_")
        print(int(rating[1])/10) 


    reviews_author.append(author)
    reviews_title.append(title)
    reviews_description.append(description)
    reviews_date.append(date)
    reviews_type.append(type)
    reviews_response.append(response)
    
# Create a dictionary from the data
data = {
    "Hotel Name": [hotel_name] + [""] * (len(reviews_author) - 1),
    "Hotel Address": [hotel_address] + [""] * (len(reviews_author) - 1),
    "Hotel Rating": [hotel_rating] + [""] * (len(reviews_author) - 1),
    "Author": reviews_author,
    "Review Title": reviews_title,
    "Review Description": reviews_description,
    "type": reviews_type,
    "Date": reviews_date,
    "Response": reviews_response
}

# Create the DataFrame
df = pd.DataFrame(data)


# Print the DataFrame
# print(df)

df.to_csv("test.csv", index=False)

    

# i = 0
# for review in reviews:
#     i+=1
#     if(i == 4):
#         break
    
#     print(i)
#     title = reviews.find('a', class_="Qwuub")
#     print(title.text)