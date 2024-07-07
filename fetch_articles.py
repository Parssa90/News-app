import requests

def fetch_articles(api_key):
    url = "https://eventregistry.org/api/v1/article/getArticles"
    data = {
        "action": "getArticles",
        "keyword": "Australia",
        "articlesPage": 1,
        "articlesCount": 10,
        "articlesSortBy": "date",
        "articlesSortByAsc": False,
        "articlesArticleBodyLen": -1,
        "resultType": "articles",
        "dataType": [
            "news",
            "pr"
        ],
        "apiKey": "7407cd18-ccee-4fab-b3bd-ee345b9b29d4",
        "forceMaxDataTimeWindow": 20
    }

    try:
        response = requests.get(url, json=data)
        response.raise_for_status()  # Raise an exception for 4xx/5xx status codes
        content = response.json()
        articles = content['articles']['results']
        return articles
    except requests.exceptions.RequestException as e:
        print(f"Error fetching articles: {e}")
        return []

if __name__ == "__main__":
    # Example usage:
    api_key = "7407cd18-ccee-4fab-b3bd-ee345b9b29d4"  # Replace with your actual API key
    articles = fetch_articles(api_key)
    for article in articles[:20]:
        print(f"Title: {article['title']}")
        print(f"Body: {article['body']}")
        print("\n")
