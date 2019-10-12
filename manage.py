# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 10:08:50 2019

@author: E201
"""

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)