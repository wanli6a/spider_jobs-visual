# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter
from pymysql import cursors
from twisted.enterprise import adbapi

# class BossSpiderPipeline(object):
#     def __init__(self):
#         self.fp = open('jobs.json','wb')
#         self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii =False)
#
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#     def close_spider(self):
#         self.fp.close()
#

class BossTwistedPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('pymysql', host='localhost',
                                    port=3306,
                                    user='root',
                                    password='wanli666',
                                    database='job_infos',
                                    charset='utf8',
                                    cursorclass=cursors.DictCursor)
        self._sql = None
    @property
    def sql(self):
        # self._sql0 ="""create table if not exists 'job_infos'(
        # 'id' int(10) unsigned NOT NULL AUTO_INCREMENT,
        # 'job_title' VARCHAR(255) NOT NULL ,
        # 'salary' VARCHAR(255) NOT NULL ,
        # 'company' VARCHAR(255) NOT NULL ,
        # 'area' VARCHAR (255) NOT NULL ,
        # 'experience' VARCHAR(255) NOT NULL ,
        # 'edu_background' TIME NOT NULL ,
        # 'pub_time' INT(10) NOT NULL ,
        #  PRIMARY KEY (`id`),
        #  CONSTRAINT MY_CONST UNIQUE (`company_name`,`company_website`)
        #   ) ENGINE=InnoDB DEFAULT CHARSET=utf8
        # """
        # with db.cursor() as cursor:
        #     cursor.execute(self._sql0)
        #     db.commit()
        if not self._sql:
            self._sql = """
               insert into job_info(id, job_title, salary, company, area, experience,edu_background, pub_time) values(null,%s,%s,%s,%s,%s,%s,%s)
               """
            return self._sql
        return self._sql
    def process_item(self, item,spider):
        defer= self.dbpool.runInteraction(self.insert_item, item)
        defer.addErrback(self.handle_error,item)
    def insert_item(self,cursor,item):
        cursor.execute(self.sql, (item['job_title'], item['salary'],item['company'], item['area'], item['experience'], item['edu_background'], item['pub_time']))

    def handle_error(self,error,spider):
        print('='*10+"error"+'='*10)
        print(error)
        print('=' * 10 + "error" + '=' * 10)
