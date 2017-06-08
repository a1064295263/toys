from setuptools import setup

setup(
    name='joke',
    author="chenx",
    version="1.0",
    author_email="chenjiandongx@qq.com",
    description="Please smile",
    py_modules=['jokes'],
    entry_points={
        'console_scripts':['joke=jokes:withBs']
    }
)
