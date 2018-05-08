#!/usr/bin/env python
# -*- coding: utf-8 -*-
import oss2
import requests
from itertools import islice
url = 'https://47.94.84.109'
im_list = '_catalog'
headers={'Accept': 'application/vnd.docker.distribution.manifest.v2+json'}

def get_all_image_list(url,im_list):
    info = requests.get(url + "/v2/" + im_list, auth=('doupai', 'Doupai123'), verify=False).content
    print info

def get_image_digest(url,):
    pass

#get_image_list(url,im_list)


auth = oss2.Auth('**********', '*************')
bucket = oss2.Bucket(auth, 'oss-cn-beijing.aliyuncs.com', 'oss存储')

for obj in oss2.ObjectIterator(bucket, prefix='docker/registry/v2/blobs'):
    #result = bucket.batch_delete_objects(obj.key)
    print('file: ' + obj.key)


