### 运行环境
1. Mac or Linux
2. pip install -r requirements.txt
3. python main.py

### 思路
1. 基于Python 2.7编写
2. 先分层抓取页面链接存入set
3. 逐个判断链接是否正常（为提高效率可采用多线程方式）
4. 不正常的链接存入log文件夹下，按照日期分类

### 预览效果

```
正在判断 xxxx
--------------
正在判断 xxxx
--------------
...
```

### TODO
1. log文件夹位置问题
2. 抓取时exception的处理
3. 抓取时多线程的处理

