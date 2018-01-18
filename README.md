### Windows ENV ###

## install python 3.5.0 ##
[https://www.python.org/ftp/python/3.5.0/python-3.5.0.exe]

## install PYQT DESIGNER 5 ###
 [https://downloads.sourceforge.net/project/pyqt/PyQt5/PyQt-5.6/PyQt5-5.6-gpl-Py3.5-Qt5.6.0-x32-2.exe]

# c:\Python35\python.exe -m pip install virtualenv
virtualenv --python=c:\Python35\python.exe dir_projeto\env

# active env
entre na pasta do projeto\env\Scripts e execute o comando -> source active.py ou active.bat

# install requirements.txt
pip install -r dir_projeto\requirements.txt

## Habilitar o device mixagem externo no windows