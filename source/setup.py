import sys
from cx_Freeze import setup, Executable

base = None

executables = [
    Executable('xmlchange.py', base=base)
]

setup (
name = "xmltoexcel",
version = "1.0",
description = "hunterhug",
executables=executables
)
