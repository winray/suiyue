# suiyue
A thought share website.
岁阅，一个思想分享网站。

## 关于部署

### 环境要求

- 要求操作系统为Ubuntu 14.04 64/32版本及以上或其他类Unix系统
- 要求Python 2.7.10或更新版本
- 安装Tornado框架。Tornado框架的安装可通过

    ```
    sudo pip install tornado
    ```

    命令安装
- 安装Python访问MySQL库，可通过 

    ```
    sudo pip install mysql-connector-python
    ```
    命令安装
- 要求MySQL 5.6.25或更新版本数据库

### 代码获取
- 代码已经部署到github仓库里，仓库地址为[https://github.com/winray/suiyue](https://github.com/winray/suiyue)，也可通过git命令
 
    ```
    git clone https://github.com/winray/suiyue
    ```
    
    直接获取。下载的包里还含有数据库建立文件。
    
### 数据库部署
- 首先在你的MySQL上新建一个用户，并开启相关读写权限
- 用新建的用户登录到MySQL创建一个新的数据库，在MySQL登录界面输入如下命令新建数据库：

    ```
    CREATE DATABASE `suiyue`
    CHARACTER SET 'utf8'
    COLLATE 'utf8_general_ci';
    ```
    
- 打开获取的代码包，解压后可以获得一个叫suiyue_database_new.txt 的文件，依次输入其中的MySQL建表语句即可建立数据库

### 运行代码
- 开启MySQL数据库
- 在运行代码前，需要对代码做一些修改
- 在models文件夹下有db.py 文件，此文件用于修改数据库相关信息。在此文件上配置你之前建立的MySQL用户名信息并保存
- 在根目录下有server.py文件，可通过设置该文件的Port参数指定端口
- 设置完毕后，可通过以下命令开启服务器

    ```
    python server.py
    ```
    
    **注意：若端口指定在1024以内需要加sudo超级用户权限**
- 接下来可打开连接 [http://localhost:8000/](http://localhost:8000/) 查看服务器是否启动，端口随你修改的端口改变
