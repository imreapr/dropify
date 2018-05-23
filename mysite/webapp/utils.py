'''
This program is will take a given keyword and return a possible trendy product
to the user followed by asking them a series of questions about the product.
'''

from lxml import html
import requests

class ProductInfo:
    """docstring for ."""
    def __init__(self, arg):
        return
        #function finds name of product from link
    def name_finder(link):
        product_page = requests.get(link)
        tree = html.fromstring(product_page.text)
         #searches html for class product-name
        product_name = tree.xpath('//h1[@class="product-name"]/text()')[0]
        return product_name

        #function finds number of orders linked product has recieved
    def order_finder(link):
        product_page = requests.get(link)
        tree = html.fromstring(product_page.text)
        #searches html for class order-num
        orders = tree.xpath('//span[@class="order-num"]/text()')[0]
        order_num = ""
        for i in range(len(orders)):
            if orders[i] == " ":
                order_num = int(order_num)
                return order_num
            order_num = order_num + orders[i]
            i = i + 1

class  ProductCrawler:

    """docstring for  AppCrawler"""
    def __init__(self, starting_url):
        self.starting_url = starting_url

    def get_product_from_link(self,link):
        #number of product in list (Change this if you want a different product)
        product_counter = 0
        #gets given links html code and sorts through it for product names.
        start_page = requests.get(link)
        tree = html.fromstring(start_page.text)
        price = tree.xpath('//span[@class="value"]/text()')[product_counter]
        link = tree.xpath('//a[@class="history-item product "]/@href')[product_counter]
        orders = ProductInfo.order_finder("https:" + link) # START HERE
        name = ProductInfo.name_finder("https:" + link)
        product_counter = product_counter + 1
        #returns tuple of necessary product specs
        product_specs = (name, price, orders, link)
        return product_specs
    #creates an object called crawler with the link generated from views.py
    def crawler(self):
        self.get_product_from_link(self.starting_url)
        return


class Product:
    """docstring for Product."""
    def __init__(self, keyword, product_name, price, links):
        return
