from cx_Freeze import setup, Executable

setup(name='foto_acessorh.py',version='1.0',description='programa feito por wellington juvenal F.Fonseca para pegar as fotos da acesso RH',options={'build_exe': {'packages': ['site-packages']}},executables=[Executable(script='foto_acessorh.py',base=None,icon = 'null')])