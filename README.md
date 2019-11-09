# <center>circR2Cancer v1.0开发</center>
## 版本
+ Python版本 3.6.6 
+ Django版本 1.10.6
+ MySQL版本 8.0
+ Pycharm 2018.04
## 安装教程
### 略
## 导入项目和数据库迁移
### <font color=red>在看完每个步骤时请注意红色部分字体再执行该步骤操作</font>
1. 将压缩包的“project”文件夹解压到目录(自定)，打开pycharm，File->open,选择指定目录下的cirRNA项目文件夹

2. 使用快捷键<font color="lightblue">ctrl+shift+N</font>打开<font color="lightblue">settings.py</font>文件, <font color="lightblue">ctrl+F</font>搜索<font color="lightblue">“databases =”</font>, 修改其中的<font color="lightblue">PASSWORD</font>为开发者的mysql数据库的root用户的密码<font color="red">(原开发者的密码为12345s)</font>
3. 使用快捷键<font color="lightblue">ctrl+shift+N</font>打开<font color="lightblue">views.py</font>文件,<font color="lightblue">ctrl+F</font>搜索”12345s",将所有搜索结果替换成开发者的mysql数据库的root用户的密码<font color="red">(原开发者的密码为12345s)</font>
4. 打开pycharm的terminal(快捷键Alt+F12),输入以下两条指令
    + `python manage.py makemigrations`
    + `python manage.py migrate`
5. 打开mysql,执行如下命令
    + `use mysql;`
    + `SET @@global.sql_mode= ''`(单引号而非双引号)
6. 将压缩包的<font color="lightblue">Table</font>文件夹(存放excel数据表)解压到目录 <font color="lightblue">E:\table</font> 中, 然后将压缩包的<font color="lightblue">DataHandle</font>文件夹解压到任意目录中，用pycharm打开该文件夹(用新窗口打开)，依次运行其中的.py文件<font color="red">(此即为导入数据库,若Table文件夹位置自定，则需要修改每个.py文件中的路径,若数据库root用户的密码不为"12345s",也需要将.py文件中对应的"12345s"替换成开发者的MySQL数据库root用户的密码)</font>
7. 点击运行项目cirRNA,或者打开terminal输入如下指令
    + `python manage.py runserver`

## 代码实现大体介绍
### 1. <font color="lightblue">views.py</font> 模块
        位于cirRNA目录下，主要关注index(主页),browse(浏览),    search(搜索), download(下载), about(关于)，detail(详情)函数，此即为网站相应页面的业务逻辑
### 2. <font color="lightblue">urls.py</font> 模块
        位于cirRNA目录下，此模块用于配置相应页面的url
### 3. <font color="lightblue">models.py</font> 模块
        位于cirRNA目录下，主要用于将数据库中的字段映射类，即可编写一个类，然后在terminal中执行数据库迁移的命令：
+ python manage.py makemigrations
+ python manage.py migrate
执行之后即可在数据库的cirrna数据库中找到对应的数据表（空表）
### 4. <font color="lightblue">DataHandle</font>文件夹
        其中存放了实现将相应的excel表格导入到数据库中的py文件，请读者自行阅读模仿相应做法即可
### 5. <font color="lightblue">html</font> 文件
        这些文件存放在cirRNA/circRNAInfo/templates目录下,为对应的前端页面代码，实现细节请读者自行理解(尤其是bootstraptable部分)    
