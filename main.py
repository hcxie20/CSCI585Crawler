import os

from spider.spider import MySpider as MS


if __name__ == "__main__":
    a = MS()
    while True:
        url = input("URL(exit): ")
        if url != "exit":
            a.get_url(url)
        else:
            break