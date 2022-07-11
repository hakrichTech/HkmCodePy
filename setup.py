# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hkmConfig']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'HkmCodePy-hkmConfig',
    'version': '0.0.3',
    'description': '@HkmCode Configuration system package',
    'long_description': 'file: README.md',
    'author': 'Hakeem Shamavu',
    'author_email': 'hakeemshamavu@hakrichteam.com',
    'maintainer': 'Hakeem Shamavu',
    'maintainer_email': 'hakeemshamavu@hakrichteam.com',
    'url': 'https://github.com/hakrichTech/HkmCodePy',
    'packages': packages,
    'package_data': package_data,
    'entry_points':{
        'console_scripts': [
                'hkmconfig = hkmConfig:main',
            ]
    },
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
