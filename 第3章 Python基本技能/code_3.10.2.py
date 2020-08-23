# -*- coding: utf-8 -*-

"""
3.10.2 打包成模块安装文件
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wxgl",
    version="0.3.0",
    author="xufive",
    author_email="xufive@outlook.com",
    description="A 3d library based pyOpenGL.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xufie/wxgl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)