import requests
try:
    from bs4 import BeautifulSoup 
except ImportError:
    raise ImportError(
        "beautifulsoup4 is not installed. Install it with: pip install beautifulsoup4"
    )
import pandas as pd
url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")
data = []
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.find("p", class_="star-rating")["class"][1]
    data.append({"Title": title, "Price": price, "Rating": rating})
    #Convert to DataFrame
df = pd.DataFrame(data)
#Clean data (example)
df["Price"] = df["Price"].str.replace("Â£", "").astype(float)
#Save files
df.to_csv("books.csv", index=False)
df.to_json("books.json", orient="records", indent=4)

print("Data scraped and saved successfully!")