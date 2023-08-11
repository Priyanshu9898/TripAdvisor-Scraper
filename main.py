from bs4 import BeautifulSoup
import pandas as pd
import requests
import math


def fetchAndSaveData(url, path):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    try: 
        r = requests.get(url,headers=headers)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return
    print(r)
    try:
        with open(path, "w", encoding='utf-8') as f:
            f.write(r.text)
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: Input/output error.")


def getHotelData(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = f.read()
    except FileNotFoundError:
        print("Error: File not found.")
        data = ""
    
    soup = BeautifulSoup(data, "lxml")
    
    
    try:
        hotel_name = soup.find('h1', class_="biGQs").text
        print("Hotel Name: ",  hotel_name)
    except AttributeError:
        hotel_name = "Hotel Name not found."
        print("Error: Hotel Name not found.")

    try:
        hotel_address = soup.find('span', class_="oAPmj").text
        print("Hotel Address: ", hotel_address)
    except AttributeError:
        hotel_address = "Hotel Address not found."
        print("Error: Hotel Address not found.")

    try:
        hotel_rating = soup.find('span', class_="uwJeR").text
        print("Hotel Rating: ", hotel_rating)
    except AttributeError:
        hotel_rating = "Hotel Rating not found."
        print("Error: Hotel Rating not found.")
        
    try:
        total_reviews = soup.find('span', class_="hkxYU").text
    except AttributeError:
        print("Error: Total Reviews not found.")
        total_reviews = "0"

    TotalNoReviews = total_reviews.split(" ")[0]
    TotalNoReviews = int(TotalNoReviews.replace(",", ""))
    print("Total No. of Reviews: ", TotalNoReviews)

    TotalPages = math.ceil(TotalNoReviews/10);

    print("Total Pages: ", TotalPages)
    
    return hotel_name, hotel_address, hotel_rating, TotalNoReviews, TotalPages

def getReviews(url, TotalPages):
    reviews_author = []
    reviews_title = []
    reviews_description = []
    reviews_date = []
    reviews_type = []
    reviews_response = []
    review_rating = []
    
    for i in range(0, TotalPages):

        
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
        
        # url = f"https://www.tripadvisor.com/Hotel_Review-g297612-d12962806-Reviews-or{i*10}-Courtyard_by_Marriott_Surat-Surat_Surat_District_Gujarat.html#REVIEWS"
        
        # Replace 'Reviews-' with 'Reviews-or{page_number}-'
        modifiedURL = url.replace("Reviews-", f"Reviews-or{i*10}-")     
        
        print(modifiedURL)
        
        try:
            r = requests.get(modifiedURL, headers=headers)
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the URL: {e}")
            continue

        soup = BeautifulSoup(r.text, "lxml")

        try:
            container = soup.find_all("div", class_="YibKl")
        except AttributeError:
            print("Error: Container not found.")
            continue
        
        
        for item in container:
            try:
                author = item.find('a', class_="ui_header_link").text
            except AttributeError:
                author = ""

            try:
                title = item.find("div", class_="KgQgP").text
            except AttributeError:
                title = ""

            try:
                description = item.find("span", class_="QewHA").text
            except AttributeError:
                description = ""

            try:
                date = item.find("span", class_="teHYY").text.split(":")[1].strip()
            except (AttributeError, IndexError):
                date = ""

            type = ""
            if item.find("span", class_="TDKzw"):
                try:
                    type = item.find("span", class_="TDKzw").text.split(":")[1].strip()
                except IndexError:
                    type = ""
            
            responseBox = item.find("div", class_="ajLyr")
            response = ""
            
            if responseBox is not None:
                try:
                    res = responseBox.find("span", class_="MInAm").text
                    if len(res) > 0:
                        response = res
                except AttributeError:
                    response = ""
            
            
            try:
                ratingBox = item.find("span", class_="ui_bubble_rating")
                
                rating = None
                if ratingBox:
                    span_classes = ratingBox['class']
                    
                    if len(span_classes) == 2:
                        ls = span_classes[1].split("_")
                        rating = int(ls[1]) / 10
                else:
                    print("Rating box not found.")
            except AttributeError:
                print("Error: Attribute not found.")
            

            reviews_author.append(author)
            reviews_title.append(title)
            reviews_description.append(description)
            reviews_date.append(date)
            reviews_type.append(type)
            reviews_response.append(response)
            review_rating.append(rating)
        
    return reviews_author, reviews_title, reviews_description, reviews_date, reviews_type, reviews_response, review_rating

def createCSV( hotel_name, hotel_address, hotel_rating, reviews_author, reviews_title, reviews_description, reviews_date, reviews_type, reviews_response, review_rating):
    
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
    # print(df)
    # Save the DataFrame to a CSV file
    try:
        df.to_csv(f"output/{hotel_name}_reviews.csv", index=False)
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: Input/output error.")
    


if __name__ == "__main__":
    # url = "https://www.tripadvisor.com/Hotel_ReCourtyardrict_Gujarat.html#REVIEWS"
    # url = "https://www.tripadvisor.com/Hotel_Review-g297612-d12962806-Reviews-or0-Courtyard_by_Marriott_Surat-Surat_Surat_District_Gujarat.html#REVIEWS"
    
    url = input("Enter the TripAdvisor hotel URL: ")

    path = "data/tripAdvisor.html"
    
    fetchAndSaveData(url, path)
    
    hotel_name, hotel_address, hotel_rating, TotalNoReviews, TotalPages = getHotelData(path)
    # print(hotel_name, hotel_address, hotel_rating, TotalNoReviews, TotalPages)
    
    reviews_author, reviews_title, reviews_description, reviews_date, reviews_type, reviews_response, review_rating = getReviews(url, TotalPages)

    createCSV( hotel_name, hotel_address, hotel_rating, reviews_author, reviews_title, reviews_description, reviews_date, reviews_type, reviews_response, review_rating)