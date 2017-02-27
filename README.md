### 运行步骤
1. Mac or Linux
2. pip install -r requirements.txt
3. python main.py

### 思路
1. 基于Python 2.7编写
2. 先分层抓取页面链接存入set
3. 逐个判断链接是否正常（为提高效率采用多线程方式）
4. 不正常的链接存入log文件夹下，按照日期分类

### 预览效果

```
正在判断 xxxx
--------------
正在判断 xxxx
--------------
...

用时： 0:01:38.973820
```

### 定时检测
可通过crontab来实现


### 改进
可以使用Python自身log库进行日志记录
