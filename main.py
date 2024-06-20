import requests
from send_email import send_email

api_key = "6daf760d4e034c99b883c27b17d9dd9b"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-05-20&sortBy=publishedAt&apiKey=" \
      "6daf760d4e034c99b883c27b17d9dd9b"
# Make request
request = requests.get(url)
# Get a dictionary data
content = request.json()
# Access the article title and description
body = ""
for article in content["articles"]:
    body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
