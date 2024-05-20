#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os,sys,re
import yaml

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
from config.conf import cm
from utils.times import running_time

class inspect(object):
    @running_time
    def inspect_element(self):
        """
        检查所有的元素是否正确
        只能做一个简单的检查
        """
        for files in os.listdir(cm.ELEMENT_PATH):
            _path = os.path.join(cm.ELEMENT_PATH, files)
            with open(_path, encoding='utf-8') as f:
                data = yaml.safe_load(f)
            for k in data.values():
                try:
                    pattern, value = k.split('==')
                except ValueError:
                    raise Exception("{} : {} 元素表达式中没有`==`".format(_path, k))
                if pattern not in cm.LOCATE_MODE:
                    raise Exception('%s中元素【%s】没有指定类型' % (_path, k))
                else:
                    assert value, '%s中元素【%s】类型与值不匹配' % (_path, k)


# if __name__ == '__main__':
#     inspect = inspect();
#     inspect.inspect_element();
