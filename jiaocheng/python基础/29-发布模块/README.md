#模块发布安装过程

1.确认编写好模块

2.在模块的根目录上创建setup.py文件
文件内容大致如下：
```
from setuptools import find_packages,setup
setup(
    name = 'kellan-test', #包名称
    version = '0.1', #版本
    author = 'Kellan', #作者
    description="A small example package", #描述
    url = "www.kellantest.com", #项目主页
    packages = find_packages() #
            )

```

3.执行``` python(3) setup.py bulid``` 构建模块

4.执行```python(3) setup.py sdist bdist_egg``` 压缩模块

5.安装就是把压缩包解压 python(3) setup.py install
