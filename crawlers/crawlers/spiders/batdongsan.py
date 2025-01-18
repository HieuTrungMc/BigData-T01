import scrapy
import re
from database.mariadb_handler import MariaDBHandler
from database.mongodb_handler import MongoDBHandler
from database.csv_handler import CSVHandler
from database.txt_handler import TXTHandler
class BatdongsanSpider(scrapy.Spider):
    name = 'batdongsan'
    allowed_domains = ['homedy.com']
    start_urls = ['https://homedy.com/du-an-can-ho']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.csv_handler = CSVHandler(file_name='batdongsan_data.csv')  
        self.txt_handler = TXTHandler(file_name='batdongsan_data.txt')
        self.mongodb_handler = MongoDBHandler(
            uri='mongodb+srv://hieutrungmc:verysafe@cluster0.0bbrp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0',
            db_name='batdongsan',
            collection_name='thongtin'
        )
        self.mariadb_handler = MariaDBHandler(
            host='host.docker.internal',
            user='root',
            password='sapassword',
            database='batdongsan'
        )
    def parse(self, response):
        for item in response.css('div.tab-content div.item'):
            data = self.extract_item_data(item)
            self.csv_handler.save_data(data)
            self.txt_handler.save_data(data)
            self.mongodb_handler.save_data(data)
            self.mariadb_handler.save_data(data)


    def extract_item_data(self, item):
        item_data = {}

        # Title extraction
        title_element = item.css('h2.name::text').get()
        item_data['title'] = (
            re.sub(r'\s+', ' ', title_element).strip() if title_element else 'N/A'
        )

        # Price extraction
        price_element = item.css('span.price::text').get()
        item_data['price'] = price_element if price_element else 'N/A'

        # Address extraction
        address_element = item.css('div.address::text').get()
        item_data['address'] = address_element.strip() if address_element else 'N/A'

        # Area extraction
        area_element = item.css('span.name-item::text').get()
        item_data['area'] = area_element.strip() if area_element else 'N/A'
        #print(item_data)
        return item_data
