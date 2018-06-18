1 try:
2 from setuptools import setup
3 except ImportError:
4 from distutils.core import setup
5
6 config = {
7 'description': 'My Project',
8 'author': 'My Name',
9 'url': 'URL to get it at.',
10 'download_url': 'Where to download it.',
11 'author_email': 'My email.',
12 'version': '0.1',
13 'install_requires': ['nose'],
14 'packages': ['NAME'],
15 'scripts': [],
16 'name': 'projectname'
17 }
18
19 setup(**config)
