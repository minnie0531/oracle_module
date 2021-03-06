from setuptools import setup, find_packages

setup(name='oracle_custom', # 패키지 명
version='1.0.0.0', #version
description='cx_oracle custom module',
author='YMS',
author_email='youemail@domain.com',
url='YMS',
license='MIT', # MIT에서 정한 표준 라이센스 따른다
py_modules=['oracle_helper'], # 패키지에 포함되는 모듈
python_requires='>=3',
install_requires=['cx_oracle','sqlAlchmey'], # 패키지 사용을 위해 필요한 추가 설치 패키지
packages=['oralce_custom'] # 패키지가 들어있는 폴더
)

