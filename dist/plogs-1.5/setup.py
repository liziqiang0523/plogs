from setuptools import setup, find_packages
 
setup(
    name='plogs',  # 打包后的包文件名
    version='1.5',    #版本号
    keywords=["pip", "plogs"],    # 关键字
    description='pretty log',  # 说明
    long_description="彩色日志，文件夹下自动生成log日志目录，根据运行的文件命名log名称,json 日志",  #详细说明
    license="",  # 许可
    url='https://github.com/liziqiang0523/clog.git',
    author='liziqiang',
    author_email='739669518@qq.com',
    # packages=find_packages(),     #这个参数是导入目录下的所有__init__.py包
    include_package_data=True,
    platforms="any",
    install_requires=[],    # 引用到的第三方库
    # py_modules=['clog.DoRequest', 'clog.GetParams', 'clog.ServiceRequest',
    #             'clog.ts.constants', 'clog.ac.Agent2C',
    #             'clog.ts.ttypes', 'clog.ac.constants',
    #             'clog.__init__'],  # 你要打包的文件，这里用下面这个参数代替
    packages=['plogs','plogs.logzero' ] # 这个参数是导入目录下的所有__init__.py包
)
