import requests
from bs4 import BeautifulSoup
import spacy
from collections import Counter

nlp = spacy.load("en_core_web_sm")

def fetch_website_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def analyze_website_content(content):
    doc = nlp(content)
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]
    return Counter(keywords).most_common(10)

def classify_website(keywords):
    categories = {
        "e-commerce": ["shop", "buy", "product", "cart"],
        "news": ["news", "breaking", "headline", "report"],
        "blog": ["blog", "post", "comment", "subscribe"],
        "social media": ["profile", "friend", "share", "like"]
        # 可以添加更多類別和對應的關鍵詞
    }
    
    category_scores = {category: 0 for category in categories}
    
    for keyword, _ in keywords:
        for category, category_keywords in categories.items():
            if keyword.lower() in category_keywords:
                category_scores[category] += 1
                
    return max(category_scores, key=category_scores.get)

def classify_website_from_url(url):
    content = fetch_website_content(url)
    if content:
        keywords = analyze_website_content(content[:1000000])
        category = classify_website(keywords)
        return category
    else:
        return "Unknown"

# 示例使用
url = "https://www.cnn.com"
category = classify_website_from_url(url)
print(f"The website {url} belongs to category: {category}")
