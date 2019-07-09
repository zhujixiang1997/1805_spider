安装mongodb数据库
  参考网站：http://www.runoob.com/mongodb/mongodb-create-database.html

  用法：
     进入mongo
     mongo
    （1）查看mongodb数据库
       show dbs 命令
       >show dbs;


    (2) 创建mongodb数据库
       use  数据库名 (此数据库名可以不存在，会自动创建)
       eg: use  spider;

       db.spider.insert({"name":'jay', 'address':'shanghai'})

    (3) 删除数据库
       use  选取数据库名
       eg: use test;

       db.dropDatabase()

    (4) 创建集合
        集合等同于mysql中的表
        use  数据库名 (此数据库名可以不存在，会自动创建)
        db.createCollection(集合名称)
        eg: db.createCollection("student")

        创建集合同时也就创建了数据库

        在 MongoDB 中，你不需要创建集合。当你插入一些文档时，MongoDB 会自动创建集合。


    (5) 插入文档
        use 数据库名
        往集合插入数据
        db.book.insert([{title: 'MongoDB 教程',
            description: 'MongoDB 是一个 Nosql 数据库',
            by: '菜鸟教程',
            url: 'http://www.runoob.com',
            tags: ['mongodb', 'database', 'NoSQL'],
            likes: 100
        }, {title: 'python 教程',
            description: 'python 是一个 很好的语言',
            by: '菜鸟教程',
            url: 'http://www.python.com',
            tags: ['python'],
            likes: 100
        }])


    (6) 查看文档内容
        use 数据库名
        直接查看json数据
        db.book.find()

        优雅方式查看json
        db.book.find().pretty()


        按照条件查询
        db.book.find({'title':'python 教程'}).pretty()

