@echo off
echo ### Adding Python and Python\Scripts to PATH
echo ### - set PATH^=%%PATH%%^;C:\Python34\^;C:\Python34\Scripts
echo. 
set PATH=%PATH%;C:\Python34\;C:\Python34\Scripts

Echo ### Set the Project Dir to 'd'
echo ### - set d^=ChessWWW
echo.
set d=ChessWWW
echo.

echo ### Files to run pep8 and pyflakes on.
echo ### - set lintfiles^=%%d%%/[FILENAME].py %%d%%/[FILENAME2].py
echo.
set lintfiles=%d%/index.py %d%/elo.py
echo.

echo ### Running and Saving Pep8 data.
echo ### - pep8 %%lintfiles%% ^> pep8.log
pep8 %lintfiles% > pep8.log
echo Done!
echo.

echo ### Running and Saving Pylint data.
echo ### - pyflakes %%lintfiles%% ^> pylint.log
pylint --rcfile=pylint.rc %lintfiles% > pylint.log
echo Done!
echo.

start pep8.log
start pylint.log