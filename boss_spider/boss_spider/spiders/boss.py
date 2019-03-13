# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from boss_spider.items import BossSpiderItem
import re

# https://www.zhipin.com/job_detail/?query=%E7%88%AC%E8%99%AB&scity=100010000&industry=&position=
# 爬虫的Unicode：\u722c\u866b
#列表页url： https://www.zhipin.com/c100010000/?query=%E7%88%AC%E8%99%AB&page=2
#详情页url：https://www.zhipin.com/job_detail/0fa02126b6bda1221HF43dy-FlA~.html
class BossSpider(CrawlSpider):
    name = 'boss'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c100010000/?query=爬虫&page=1']
    rules = (
        # 列表页匹配规则,前面的都一样，从问号？query开始查“爬虫”，问号要转义；
        Rule(LinkExtractor(allow=r'.+\?query=%E7%88%AC%E8%99%AB&page=\d'),follow=True),
    #     详情页规则,这里和视频课程里不一样辣，需要自己设置正则咯，去在线正则测试检查匹配，再来写
        Rule(LinkExtractor(allow=r'.+job_detail/.*?.html'), callback='parse_detail', follow=False),
    )
    # response.xpath('//div[@class="name"]/h1/text()').get()
    def parse_detail(self, response):
        job_title = response.xpath('//div[@class="name"]/h1/text()').get()
        salary = response.xpath('//div[@class="name"]/span[@class="salary"]/text()').get().strip()
        # min_salary = re.match('([0-9]{5}|[0-9]{4})\-([0-9]{5})',salary).group(1)
        # max_salary = re.match('([0-9]{5}|[0-9]{4})\-([0-9]{5})',salary).group(2)
        company = response.xpath('//div[@class="job-sec"]/div[@class="name"]/text()').get()
        job_info = response.xpath('//div[contains(@class,"job-primary")]/div[@class="info-primary"]/p//text()').getall()
        area = job_info[0]
        experience = job_info[1]
        edu_background = job_info[2]
        time_info = response.xpath('//div[@class="job-sider"]/div[@class="sider-company"]/p[@class="gray"]/text()').get()
        pub_time = re.match('.*([0-9]{4}-[0-9]{2}-[0-9]{2})\s.*',time_info).group(1)

        item = BossSpiderItem(job_title=job_title,salary=salary,company=company,area=area,experience=experience,edu_background=edu_background,pub_time=pub_time)

        yield item
