# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv

class SpyderPipeline(object):

    def __init__(self):
        file = open('items.csv', 'w')
        self.csvwriter = csv.writer(file)
        self.csvwriter.writerow(['url'])

    def process_item(self, item, spider):
        self.csvwriter.writerow([item['url']])
        return item
