# -*- coding: utf8 -*-
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest
import json

# 配置地域和可用区
#Region_ID = ['cn-beijing','cn-hongkong']
Region_ID = ['cn-beijing']
# 配置access
Prod_ID = {'项目1':{'access_key_id':'********',
                     'access_key_secret':'**********'},
           '项目2':{'access_key_id':'',
                     'access_key_secret':''},}

def get_data(key):
    # 创建AcsClient实例
    client = AcsClient(
       "*********",
       "***************",
       key
    );
    # 创建request，并设置参数
    request = DescribeInstancesRequest.DescribeInstancesRequest()
    request.set_PageSize(10)
    # 发起API请求并显示返回值
    # response = client.do_action_with_exception(request)

    request.set_accept_format('json')
    # 发起请求，获取数据
    #result = json.loads(client.do_action_with_exception(request)).get('Instances').get('Instance')
    result = json.loads(client.do_action_with_exception(request)).get('Instances').get('Instance')
    return result

def handle_data(key):
    data = get_data(key)
    result = []
    print (data)
    for line in data:
        data = (
            line.get('InstanceId'), # 实例ID
            line.get('InstanceName'), # 名称
            # line.get('PublicIpAddress').get('IpAddress')[0],
            # line.get('InnerIpAddress').get('IpAddress')[0],
            line.get('NetworkInterfaces').get('NetworkInterface')[0].get('PrimaryIpAddress'), # 私有ip
            line.get('EipAddress').get('IpAddress'),
            #line.get('OSName'), # 操作系统
            line.get('RegionId'), # 地区
            line.get('VpcAttributes').get('VpcId'), # vpc
            doupai, # 项目名称
        )
        result.append(data)
    print (result)
    return result



if __name__ == '__main__':
    for Region in Region_ID:
        handle_data(Region)
