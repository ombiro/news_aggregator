from newspaper import Article


def summarize_article(url):
    article = Article(url)

    article.download()
    article.parse()

    article.download('punkt')
    article.nlp()

    print("Author: " + str(article.authors))


summarize_article("https://www.nytimes.com/2022/03/14/technology/personaltech/apple-iphone-se-review.html")
