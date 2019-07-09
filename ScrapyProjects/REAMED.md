scrapy项目开发流程

准备工作：
    1.安装python虚拟环境
    2.安装pymysql，scrapy(twisted)
    
工程设计与开发
1.创建工程
    scrapy startproject project_name （project_name：BookToscrape）
    创建了一个scrapy项目工程
    
2.创建爬虫
    scrapy genspider spider_name (spider_name：toscrapy) domain (domain：books.toscrapy.com)

3.图片下载
    (1)创建一个图片处理pipeline文件(eg：image_pipeline.py)
    (2)添加配置信息 (settings.py)
    (3)校验spiders/spider_name.py
       检查爬虫文件里面图片url地址命名是否为image_url

4.数据持久化，保存数据到mysql
    4.1 通过orm保存item数据到mysql
    4.2 通过twisted库自带异步处理模块

5.数据持久化到mongodb
    