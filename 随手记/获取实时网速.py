# coding=utf-8
# @Time    : 2020/3/30 17:31
# @Author  : zwa
# @Motto   ：❤lqp

import wmi
import time
import platform

def get_network_flow(os):
    '''监控window平台下网卡的实时的流量信息
    通过当前总流量和一秒后的总流量的差值，来统计实时的网卡流量信息;
    返回的流量单位是KB
    '''
    if os == "Windows":
        c = wmi.WMI()
        for interfacePerTcp in c.Win32_PerfRawData_Tcpip_TCPv4():
            sentflow = float(interfacePerTcp.SegmentsSentPersec)  #已发送的流量
            receivedflow = float(interfacePerTcp.SegmentsReceivedPersec) #接收的流量
            present_flow = sentflow+receivedflow    #算出当前的总流量
        time.sleep(1)
        for interfacePerTcp in c.Win32_PerfRawData_Tcpip_TCPv4():
           sentflow = float(interfacePerTcp.SegmentsSentPersec)  #已发送的流量
           receivedflow = float(interfacePerTcp.SegmentsReceivedPersec) #接收的流量
           per_last_present_flow = sentflow+receivedflow     #算出1秒后当前的总流量
        present_network_flow = (per_last_present_flow - present_flow)/1024
        print("当前流量为：{0}KB".format("%.2f"%present_network_flow))
        return "%.2f"%present_network_flow

if __name__ =="__main__":
    os = platform.system()
    while 1:
        flow = get_network_flow(os)
        print("{0}KB".format(flow))
