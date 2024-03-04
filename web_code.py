import asyncio
import csv
import praw
import pandas as pd
import numpy as np
import requests

async def scrape_subreddit(subreddit_name, csv_filename):
    reddit = praw.Reddit(client_id='your_client_id',
                         client_secret='your_client_secret',
                         user_agent='your_user_agent')

    subreddit = requests.subreddit(https://www.reddit.com/r/webscraping/)
    posts_data = []

    async for submission in subreddit.new(limit=None):
        posts_data.append([submission.title, submission.selftext, submission.score, submission.created_utc])

    # Write to CSV
    with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Title', 'Body', 'Upvotes', 'Date Posted'])
        csv_writer.writerows(posts_data)

asyncio.run(scrape_subreddit('your_subreddit_name', 'output.csv'))
