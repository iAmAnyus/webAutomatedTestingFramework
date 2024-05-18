#readConfig.py
import configparser
import sys,os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))

from config.conf import cm

HOST='HOST'

class ReadConfig(object):
    """配置文件读取类"""
    def __init__(self):
        self.config=configparser.RawConfigParser()
        self.config.read(cm.ini_file,encoding='utf-8')

    def _get(self,section,option):
        """获取配置项的值"""
        return self.config.get(section,option)

    def _set(self, section, option, value):
        """获取HOST部分的HOST配置项的值"""
        self.config.set(section, option, value)
        with open(cm.ini_file, 'w') as f:
            self.config.write(f)
    @property
    def url(self):
        return self._get(HOST, HOST)


ini = ReadConfig()

# if __name__ == '__main__':
#     print(ini.url)
