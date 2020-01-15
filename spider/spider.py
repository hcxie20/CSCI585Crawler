import time
import urllib
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
import re


class spider(object):
    def __init__(self, headless=True, dtLoadPicture=True, disableGPU=True):
        self.chrome_option = webdriver.ChromeOptions()

        self.mkdir("./download")

        if dtLoadPicture == True:
            prefs = {"profile.managed_default_content_settings.images":2}
            self.chrome_option.add_experimental_option("prefs",prefs)
        if headless == True:
            self.chrome_option.add_argument("--headless")
        if disableGPU == True:
            self.chrome_option.add_argument("--disable-gpu")

        self.chrome_option.add_argument('user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1')

        self.browser = None

        self.start_browser()

    def boot_up_browser(self):
        self.browser = webdriver.Chrome(options=self.chrome_option)
        self.browser.implicitly_wait(10)

    def start_browser(self):
        self.boot_up_browser()
        pass

    def get_url(self, url):
        pass

    def img_tag(self):
        pass

    def download(self, urls, filenames, path):
        print("Start downloading...")
        l = len(urls)

        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1')]
        urllib.request.install_opener(opener)

        for i in range(l):
            print("  page {0:03d}/{1}".format(i + 1, l))
            urllib.request.urlretrieve(urls[i], path + "/" + filenames[i])
        pass

    @staticmethod
    def mkdir(dir):
        if not os.path.exists(dir):
            os.mkdir(dir)
        return True


class MySpider(spider):
    def start_browser(self):
        print("585 spider v 0.1")
        self.boot_up_browser()

    def get_url(self, url):
        print("Getting url...")
        self.browser.get(url)
        title = self.browser.title
        print(title)
        self.mkdir("./download/"+title)

        imgs = self.browser.find_elements_by_tag_name("img")

        urls = [None] * len(imgs)
        filenames = [None] * len(imgs)

        for i in range(len(imgs)):
            urls[i] = imgs[i].get_attribute("src")
            filenames[i] = "{0:02d}.jpg".format(i+1)

        self.download(urls, filenames, "./download/"+title)


if __name__ == "__main__":
    a = MySpider()
    url = "http://bytes.usc.edu/cs585/s20_db0ds1ml2agi/lectures/DataModeling/slides.html"
    a.get_url(url)
