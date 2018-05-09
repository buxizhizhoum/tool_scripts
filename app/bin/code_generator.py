#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
generate duplicated code
"""
import string
from string import Template

temp_template = string.Template("Hello $name ,your website is $message")
print(temp_template.substitute(name='大CC', message='http://blog.me115.com'))

