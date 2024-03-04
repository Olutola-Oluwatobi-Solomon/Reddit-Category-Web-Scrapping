import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def scrape_subreddit(subreddit_name, csv_filename):
    # The URL of the subreddit you i want to scrape
    subreddit_url = f'https://www.reddit.com/r/webscraping/'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    response = requests.get(subreddit_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    posts_data = []

    # Extracting posts from Reddit
    for post in soup.find_all('div', class_='Post'):
        title = post.find('h2', class_='s1hgmujp-2 eiyPCF').text.strip()  # Adjust class based on Reddit's HTML structure
        body = post.find('div', class_='s1hgmujp-3 eLpsZl').text.strip()  # Adjust class based on Reddit's HTML structure
        upvotes = post.find('div', class_='s5c1hyd-3 cbbOKC').text.strip()  # Adjust class based on Reddit's HTML structure
        date_posted = datetime.utcfromtimestamp(int(post['data-click-id'])).strftime('%Y-%m-%d %H:%M:%S')

        posts_data.append([title, body, upvotes, date_posted])

    # Writing to CSV
    with open(csv_first_scrap_of_Reddit, 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Title', 'Body', 'Upvotes', 'Date Posted'])
        csv_writer.writerows(posts_data)

# Define your CSV filename
csv_first_scrap_of_Reddit = 'output.csv'

# Call the scraping function with the defined CSV filename
scrape_subreddit('r/webscraping', csv_first_scrap_of_Reddit)

# scrape_subreddit('r/webscraping', 'output.csv')