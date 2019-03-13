###使用scrapy框架编写的爬取boss直聘的小爬虫
>* 一直听说boss直聘反爬厉害，可是，这次练手却意外的没有遭遇403。这让我很是惊讶，仅仅编写了items，spider，以及pipeline，设置了一个请求头（都没有用随机请求头），也没有上代理池啥的，就把全国的爬虫岗位信息爬取了，存储到Mysql中，并简单使用pandas和numpy处理了下数据并可视化了一下。
>* 不过可视化并没有做到预期，再学习一段时间后继续把这个数据以其他方式（如词云）再做一下（本来是想把工作地点、岗位描述做词云；薪资和地区做地图可视化，只是现在做出来的好难看，就没有放上来）。
>* 接下来应该会继续练习使用scrapy框架爬拉钩或者其他比如租房、学术（知网）以及一些反爬比较厉害的。之所以要找虐，是因为selenium效率还是不够高，而且selenium我个人感觉更像是测试网站的，作为爬虫的辅助还行，真的要大量数据，，，估计效率还是慢了些。最近在知乎看到一篇js逆向解析的，感觉要多学习逆向的知识，觉得逆向解析才是真正的爬虫技术吧。
>*本代码于2019-03-12测试通过。

###下面简单看看可视化的效果吧（使用了pyecharts）
![城市岗位数量柱状图](https://github.com/wanli6a/spider_jobs-visual/blob/master/vis_photos/city_count1.JPG)

![饼状分布图](https://github.com/wanli6a/spider_jobs-visual/blob/master/vis_photos/spider0.gif)

![地图分布](https://github.com/wanli6a/spider_jobs-visual/blob/master/vis_photos/spider.gif)
