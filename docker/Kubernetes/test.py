# coding=utf-8
import requests, json, yaml

f = open("nginx1.yaml")
kk = yaml.load(f)
# print(kk)
ngnixYaml = yaml.dump(kk)
# print(ngnixYaml)
Heads = {'Content-Type': 'application/yaml'}
address = 'http://192.168.56.110:8080'
api = 'apis/extensions/v1beta1/namespaces/default/deployments'

url = address + '/' + api
print(url)
heads = {}
req = requests.post(url, data=ngnixYaml, headers=Heads)
# req.encoding = "utf-8"
print(req.text)