#模块发布安装过程

1.确认编写好模块

2.在模块的根目录上创建setup.py文件
文件内容大致如下：
```
from distutils.core import setup
setup(name='test',version='1.0',description='a test python packge', author='Kellan Fan', py_modules=['bao.Gcc', 'bao.Pots']) 
```
就是做一些信息说明，其中```py_modules```就是你要发布的模块列表

3.执行``` python(3) setup.py bulid``` 构建模块

4.执行```python(3) setup.py sdist``` 压缩模块

5.安装就是把压缩包解压 python(3) setup.py install
