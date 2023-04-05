from setuptools import setup
import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable("your_script.py", base=base, icon="img/instabotify.ico")
]

build_options = {"packages": [], "include_files": ["img/"]}

setup(
    name="IG-Ultimate",
    version="1.0",
    description="Auto follower tool for instagram",
    options={"build_exe": build_options},
    executables=executables
)