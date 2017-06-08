from setuptools import setup

setup(
    name='girl',
    author="chenx",
    version="1.0",
    author_email="chenjiandongx@qq.com",
    description="Be a better boyfriend",
    py_modules=['girl', 'datetime'],
    entry_points={
        'console_scripts':['girl=girl:girlfriend']
    }
)
