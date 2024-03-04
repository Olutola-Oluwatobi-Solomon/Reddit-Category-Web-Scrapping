import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def scrape_subreddit(subreddit_name, csv_filename):
    subreddit_url = f'https://www.reddit.com/r/Foodforthought/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    try:
        response = requests.get(subreddit_url, headers=headers)
        response.raise_for_status()  # Check if the request was successful

        soup = BeautifulSoup(response.text, 'html.parser')

        posts_data = []

        for post in soup.find_all('div', class_='Post'):
            title = post.find('h3', class_='s1hgmujp-2 eiyPCF')
            body = post.find('div', class_='s1hgmujp-3 eLpsZl')
            upvotes = post.find('div', class_='s5c1hyd-3 cbbOKC')

            # Check if any of the elements are None before extracting text
            if title and body and upvotes:
                title_text = title.text.strip()
                body_text = body.text.strip()
                upvotes_text = upvotes.text.strip()
                date_posted = datetime.utcfromtimestamp(int(post['data-click-id'])).strftime('%Y-%m-%d %H:%M:%S')

                posts_data.append([title_text, body_text, upvotes_text, date_posted])

        if posts_data:
            with open(csv_first_scrap_of_Reddit, 'w', newline='', encoding='utf-8') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(['Title', 'Body', 'Upvotes', 'Date Posted'])
                csv_writer.writerows(posts_data)
            print(f"Scraping successful. Data written to '{csv_first_scrap_of_Reddit}'")
        else:
            print("No data scraped from the subreddit.")

    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print ("Other Request Error:", err)

# Define your CSV filename
csv_first_scrap_of_Reddit = 'output.csv'

# Call the scraping function with the defined CSV filename
scrape_subreddit('r/webscraping', csv_first_scrap_of_Reddit)
