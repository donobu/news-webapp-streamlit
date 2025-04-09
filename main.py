import requests
import streamlit as st
from datetime import date, timedelta

# Get the date and minus one day from current day
# the change to iso format(YYYY-M-D)
today = date.today()
minus_one_day = today - timedelta(days=1)
minus_one_day = minus_one_day.isoformat()

country = "usa"

api_key = "**************************"
url = ("https://newsapi.org/v2/everything?"
       f"q={country}&"
       f"from={minus_one_day}&"
       "sortBy=publishedAt&"
       "language=en&"
       "apiKey=********************")

st.set_page_config(layout='wide')
st.title("Simple News Feeds")

col1, col2, col3 = st.columns(3)

# make a request
request = requests.get(url)
# Get a dictionary
content = request.json()

# Access article titles and descriptions
with col1:
    for article in content["articles"][:25]:
        st.subheader(article['title'])
        st.info(article['description'])
        st.write(article['url'])

with col2:
    for article in content["articles"][25:50]:
        st.subheader(article['title'])
        st.info(article['description'])
        st.write(f"[Source Link]({article['url']})")

with col3:
    for article in content["articles"][50:75]:
        st.subheader(article['title'])
        st.info(article['description'])
        st.write(article['url'])

