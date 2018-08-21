# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import csv

class RTPipeline(object):
    
    def __init__(self):
            self.csvwriter = csv.writer(p[en("rt_moves_new.csv", "w")
            self.csvwriter.writerow(["title", "score", "genres", "consensus"])
                               
     def process_itme(self, item, spider):
        row = []
        row.append(item["title"]
        row.append(item["score"]
        row.append(item['.join(item["genres"]))
        row.append(item["consensus"])
        self.csvwriter.writerow(row)
        return item
                        
  
                                     
