import requests
from send_email import send_email

topic = "tesla"
api_key = "6daf760d4e034c99b883c27b17d9dd9b"
url = f"https://newsapi.org/v2/everything?q={topic}&" \
      "from=2024-05-20&sortBy=publishedAt&apiKey=" \
      "6daf760d4e034c99b883c27b17d9dd9b&language=en"
# Make request
request = requests.get(url)

# Get a dictionary data
content = request.json()

# Access the article title and description
body = "Subject: Today's news\n\n"
for article in content["articles"][:20]:
    if article["title"] is not None:
        body += article["title"] + "\n" \
                + (article["description"] or "") + "\n" \
                + article["url"] + "\n\n"

body = body.encode("utf-8")
send_email(message=body)
