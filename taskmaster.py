# /usr/bin/env python
# -*- utf-8 -*-

import random
import queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

# 发送任务
task_queue = queue.Queue()
# 接收任务
result_queue = queue.Queue()
def task_q():
    return task_queue
def result_q():
    return result_queue
# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass
def server_start():
    # 把两个Queue都注册到网络上, callable参数关联了Queue对象
    QueueManager.register('get_task_queue', callable=task_q)
    QueueManager.register('get_result_queue', callable=result_q)
    # 绑定端口5000, 设置验证码'abc'
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 启动Queue
    manager.start()
    # 获得通过网络访问的Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 放几个任务
    for i in range(10):
        n = random.randint(0, 100)
        print('Put task %d.....' % n)
        task.put(n)
    # 从result队列读取结果
    print('Try get result')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result: %s' % r)
    # close
    manager.shutdown()
    print('master exit')
if __name__ == '__main__':
    freeze_support()
    server_start()
