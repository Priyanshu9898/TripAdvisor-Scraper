from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://www.booking.com/hotel/in/gateway-on-athwa-lines.en-gb.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYAQm4ARfIAQzYAQHoAQH4AQyIAgGoAgO4Ap2foKQGwAIB0gIkNjc1YjYyZTUtY2MzNy00NzgyLThmNjAtYTIyODVjYmJlZjU52AIG4AIB&sid=40e241e10965e997f44d83f0bc7add0d&all_sr_blocks=7471324_91461507_2_2_0;checkin=2023-06-25;checkout=2023-06-26;dest_id=-2112243;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=7471324_91461507_2_2_0;hpos=1;matching_block_id=7471324_91461507_2_2_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=7471324_91461507_2_2_0__800000;srepoch=1686638506;srpvid=47ad2f1433870370;type=total;ucfs=1&#tab-main"


def fetchAndSaveData(url, path):
    r = requests.get(url)
    
    print(r)
    
    with open(path, "w", encoding='utf-8') as f:
        f.write(r.text)

# fetchAndSaveData(url, "data/index.html")


with open('data/index.html', 'r', encoding='utf-8') as f:
    data = f.read()

soup = BeautifulSoup(data, "lxml")

# print(soup.prettify())


hotel_name = soup.find('h2', class_="d2fee87262").text

print(hotel_name)


hotel_address = soup.find('span', class_="hp_address_subtitle").text

print(hotel_address)


hotel_rating = soup.find('div', class_="b5cd09854e").text
print(hotel_rating)

# total_hotel_reviews = soup.find_all('span', class_="b5cd09854e")

# for i in total_hotel_reviews:
#     print(i.text)

reviews = soup.find_all('ul', class_="comments")

print(reviews)

review_url = url.split("#")[0] + "#tab-reviews"

# fetchAndSaveData(review_url, "data/review.html")

with open('data/review.html', 'r', encoding='utf-8') as f:
    review_data = f.read()

review_soup = BeautifulSoup(review_data, "lxml")

# print(review_soup.find_all('h3', class_="gallery-side-reviews-wrapper__title"))

# print(review_soup.find_all('div', class_="bui-grid__column-9"))

# print(review_soup.find('div', id_="review_list_page_container"))

element = soup.find(id='review_list_page_container')

print(review_soup.find_all('span', class_="c-review-block__row"))


# print(review_soup.find_all('div', class_="c-review-block__right"))
# print(review_list)

