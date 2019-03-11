from distutils.core import setup
setup(name='test',version='1.0',description='a test python packge', author='Kellan Fan', py_modules=['bao.Gcc', 'bao.Pots'])

#这里面指定需要包含的py文件，注意没有后缀
#构建：python setup.py build
#生成发布压缩包： python setup.py sdist

#安装
#1. 找到模块的压缩包
#2. 解压
#3. 进入文件件夹
#4. 执行命令 python setup.py install
#注意：如果在install的时候，执行目录安装，可以使用 python setup.pinstall --prefix=安装路径
