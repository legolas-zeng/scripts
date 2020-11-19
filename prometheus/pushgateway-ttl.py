# coding=utf-8
from urllib import request
import time
from random import randint, random
from datetime import timedelta
from timeit import default_timer as timer
import requests
from  prometheus_client import push_to_gateway,delete_from_gateway,pushadd_to_gateway,CollectorRegistry, Summary, Counter,Gauge

target_url = "http://192.168.3.16:9091/metrics/job/some_job"
GATEWAY = "http://192.168.3.16:9091"
def push_data():

    data='''\
# TYPE processed_items counter
# HELP processed_items The total number of processed items.
processed_items 123456
'''
    # req = request.Request(target_url, data=data)
    resp = requests.post(target_url, data=data)
    print(resp)

def push_date_gateway():
    registry = CollectorRegistry()
    g = Gauge('job_last_success_unixtime', 'Last time a batch job successfully finished', registry=registry)
    g.set("1005521")
    push_to_gateway(GATEWAY, job='batchA', registry=registry)

def delete_date_gateway():
    delete_from_gateway(GATEWAY,job="batchA")


def pushadd_date_gateway():
    registry = CollectorRegistry()
    pushadd_to_gateway(GATEWAY, "my_job",registry)

def linux_proc():
    REGISTRY = CollectorRegistry(auto_describe=False)
    linux_proc_error = Gauge(f'linux_proc_error', f"LINUX_进程异常指标", ["instance", "A00_iid", "iexe", "iparam", "icwd"],
                             registry=REGISTRY)
    linux_proc_info_list = ["instance", "A00_iid", "iexe", "iparam", "icwd", "pid", "name", "status", "is_running",
                            "exe", "cmdline", "parent", "username", "port"]
    linux_proc_info = Gauge("linux_proc_info", "LINUX_进程信息指标", linux_proc_info_list, registry=REGISTRY)
    metric_list = ["io_read_count", "io_write_count", "io_read_bytes", "io_write_bytes", "cpu_user", "cpu_system",
                   "cpu_children_user", "cpu_children_system", "cpu_iowait", "memory_rss", "memory_vms",
                   "memory_shared", "memory_swap", "memory_text", "memory_data", "num_open_files", "num_fds_limit",
                   "num_fds", "cpu_num", "num_threads", "num_children", "cpu_percent", "memory_percent", "durn"]


if __name__ == '__main__':
    push_date_gateway()