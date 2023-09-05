from setuptools import setup, find_packages

# 项目名称
name = "myproject"

# 项目版本
version = "0.1.0"

# 项目描述
description = "A simple Python project."

# 项目作者
author = "Minghe.xie"

# 项目作者的电子邮件地址
author_email = "1633828622@qq.com"

# 项目的URL
url = "https://github.com/Xieminghe/qqqq"

# 项目的许可证
# license = "MIT"

# 项目的依赖项
install_requires = [
      
      numpy>=1.0
    # 依赖项列表，例如 "numpy>=1.0" 或 "requests"
]

setup(
    name=name,
    version=version,
    description=description,
    author=author,
    author_email=author_email,
    url=url,
    license=license,
    packages=find_packages(),  # 自动查找项目中的所有包
    install_requires=install_requires,
)
