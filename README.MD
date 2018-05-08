![](https://img.shields.io/badge/language-python2.7-orange.svg)


#### ELK
- [x] elk6.2.2
- [x] docker 1.17

注意：docker版本未配置高可用

#### RPC
python的RPC服务。脚本里都是些简单的测试功能。

服务端运行：`xml_rpc_server.py`

客户端运行：`test-RPC.py`

#### ansible
`ansible`2.3和2.0以及2.0以前的版本的用法不一样，详情看[这里](http://zenganiu.xyz/2018/02/27/ansible%E7%9A%84api%E5%A4%A7%E5%9D%91%E8%A7%A3%E6%9E%90/)。

测试运行：`ansible_api.py`和`test-ansible.py`将收集的信息发送至`http://192.168.2.120/api_host_info`

#### jenkins
`auto_tomcat.py`自动部署脚本，将maven自动发布到tomcat。
`rollback_tomcat.py`自动回滚。

#### 一键安装脚本
常用的安装脚本


#### supervisor
`supervisor_api.py`获取进程状态、控制进程。

#### 快递查询
快递鸟api提供服务

`test.py`测试脚本
`exp_company.py`测试脚本

#### mysql-docker
mysql主从配置的docker-compose文件

#### 爬虫
`豆瓣电影_表格_翻页.py` 爬取豆瓣电影，然后生成svg图。

`bad.py` 微博爬虫

