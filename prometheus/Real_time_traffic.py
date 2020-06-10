# coding=utf-8
# @Time    : 2020/6/10 14:38
# @Author  : zwa
# @Motto   ：❤lqp

import prometheus_client
from prometheus_client import Counter
from prometheus_client import Gauge
from prometheus_client.core import CollectorRegistry
import psutil
import time
import requests
import socket

def get_key():
    key_info = psutil.net_io_counters(pernic=True).keys()

    recv = {}
    sent = {}

    for key in key_info:
        recv.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_recv)
        sent.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_sent)

    return key_info, recv, sent


def get_rate(func):
    key_info, old_recv, old_sent = func()
    time.sleep(1)
    key_info, now_recv, now_sent = func()
    net_in = {}
    net_out = {}
    for key in key_info:

        # 计算流量
        net_in.setdefault(key, now_recv.get(key) - old_recv.get(key))
        net_out.setdefault(key, now_sent.get(key) - old_sent.get(key))

    return key_info, net_in, net_out

# 打印多网卡 mac 和 ip 信息
def PrintNetIfAddr():
    dic = psutil.net_if_addrs()
    net_dic = {}
    net_dic['no_ip'] = []  # 无ip的网卡列表
    for adapter in dic:
        snicList = dic[adapter]
        mac = '无 mac 地址'
        ipv4 = '无 ipv4 地址'
        ipv6 = '无 ipv6 地址'
        for snic in snicList:
            if snic.family.name in {'AF_LINK', 'AF_PACKET'}:
                mac = snic.address
            elif snic.family.name == 'AF_INET':
                ipv4 = snic.address
            elif snic.family.name == 'AF_INET6':
                ipv6 = snic.address
        # print('%s, %s, %s, %s' % (adapter, mac, ipv4, ipv6))

        # 判断网卡名不在net_dic中时,并且网卡不是lo
        if adapter not in net_dic and adapter != 'lo':
            if not ipv4.startswith("无"):  # 判断ip地址不是以无开头
                net_dic[adapter] = ipv4  # 增加键值对
            else:
                net_dic['no_ip'].append(adapter)  # 无ip的网卡

    # print(net_dic)
    return net_dic

key_info, net_in, net_out = get_rate(get_key)

# ip=get_host_ip()  # 本机ip
hostname = socket.gethostname() # 主机名

REGISTRY = CollectorRegistry(auto_describe=False)
input = Gauge("network_traffic_input", hostname,['adapter_name','unit','ip','instance'],registry=REGISTRY)  # 流入
output = Gauge("network_traffic_output", hostname,['adapter_name','unit','ip','instance'],registry=REGISTRY)  # 流出


for key in key_info:
    net_addr = PrintNetIfAddr()
    # 判断网卡不是lo(回环网卡)以及 不是无ip的网卡
    if key != 'lo' and  key not in net_addr['no_ip']:
        # 流入和流出

        input.labels(ip=net_addr[key],adapter_name=key, unit="Byte",instance=hostname).inc(net_in.get(key))
        output.labels(ip=net_addr[key],adapter_name=key, unit="Byte",instance=hostname).inc(net_out.get(key))


requests.post("http://192.168.3.16:9091/metrics/job/network_traffic",data=prometheus_client.generate_latest(REGISTRY))
print("发送了一次网卡流量数据")
