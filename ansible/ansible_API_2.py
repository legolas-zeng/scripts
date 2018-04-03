# -*-coding:utf-8 -*-
import json
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase

class ResultCallback(CallbackBase):
    def v2_runner_on_ok(self, result, **kwargs):
        host = result._host
        print(json.dumps({host.name: result._result}, indent=4))


# 初始化需要的对象
Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])

# module_path参数指定本地ansible模块包的路径
loader = DataLoader()
options = Options(connection='smart', module_path='/usr/lib/python2.7/dist-packages/ansible/modules', forks=5, become=None, become_method=None, become_user="root", check=False, diff=False)
passwords = dict(vault_pass='secret')

# 实例化ResultCallback来处理结果
results_callback = ResultCallback()

# 创建库存(inventory)并传递给VariableManager
inventory = InventoryManager(loader=loader, sources='/etc/ansible/hosts') #../conf/hosts是定义hosts
variable_manager = VariableManager(loader=loader, inventory=inventory)

# 创建任务
play_source =  dict(
        name = "Ansible Play",
        hosts = "cephnode",
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='touch /tmp/7.txt'), register='shell_out'), #定义一条任务，如有多条任务也应按照这样的方式定义
         ]
    )
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# 开始执行
tqm = None
try:
    tqm = TaskQueueManager(
              inventory=inventory,
              variable_manager=variable_manager,
              loader=loader,
              options=options,
              passwords=passwords,
              stdout_callback=results_callback,  # 使用自定义回调代替“default”回调插件（如不需要stdout_callback参数则按照默认的方式输出）
          )
    result = tqm.run(play)
finally:
    if tqm is not None:
        tqm.cleanup()