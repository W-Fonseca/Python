import sys
from cx_Freeze import setup, Executable



setup(name = "Fotos_acessorh" ,
      version = "0.1" ,
      description = "" ,
      options = {'build_exe': {'packages': ['pacotew']}},
      executables = [Executable("foto_acessorh.py")])