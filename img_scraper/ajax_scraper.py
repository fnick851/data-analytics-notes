import os.path

from lxml import etree
from selenium import webdriver

from download import download

request_url = 'https://movie.douban.com/subject_search?search_text=永野芽郁&cat=1002'

driver = webdriver.Chrome(os.path.dirname(
    os.path.realpath(__file__)) + '/' + 'chromedriver')
driver.get(request_url)

html = etree.HTML(driver.page_source)
src_xpath = "//div[@class='item-root']/a[@class='cover-link']/img[@class='cover']/@src"
srcs = html.xpath(src_xpath)

title_path = "//div[@class = 'item-root']/div[@class = 'detail']/div[@class = 'title']/a[@class = 'title-text']"
titles = html.xpath(title_path)

for src, title in zip(srcs, titles):
    download(src, title.text, 'ajax_scrapted_imgs')
