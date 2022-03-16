from newspaper import Article


def summarize_article(url):
    article = Article(url)

    article.download()
    article.parse()

    article.download('punkt')
    article.nlp()

    print("Author: " + str(article.authors))

    date = article.publish_date
    print("Publish Date: " + str(date.strftime("%m/%d/%Y")))

    print("Top Image Url:" + str(article.top_image))

    image_string = "All Images:"
    for image in article.images:
        image_string += "\n\t" + image
    print(image_string)

    print("A Quick Article Summary")
    print("--------------------------------")
    print(article.summary)



summarize_article("https://www.nytimes.com/2022/03/15/technology/intel-factory-germany.html")
