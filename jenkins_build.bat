:A
@echo off
echo.
echo ##### START OF BUILD #####
echo.

echo ### Running cleanner.bat
call cleanner.bat 1> out.log 2> error.log
echo Done!
echo.

echo ### Adding Python and Python\Scripts to PATH
echo ### - set PATH^=%%PATH%%^;C:\Python34\^;C:\Python34\Scripts
echo. 
set PATH=%PATH%;C:\Python34\;C:\Python34\Scripts

Echo ### Set the Project Dir to 'd'
echo ### - set d^=ChessWWW
echo.
set d=wwwApp

echo ### Files to run pep8 and pyflakes on.
echo ### - set lintfiles^=%%d%%/[FILENAME].py %%d%%/[FILENAME2].py
echo.
set lintfiles=%d%/SessionLogon.py %d%/index.py

echo ### Each coverage must have its own line and be formatted
echo ### - coverage run -p [filename].py 1>> tests.log 2>> tests.log
echo.
echo +++++++++++++++++++ RUN  TESTS +++++++++++++++++++
echo coverage run -p jenkins_build.py 
echo coverage run -p more_jenkins_build.py
echo ::coverage run -p [FILENAME].py

set E=0

coverage run -p jenkins_build.py
if %ERRORLEVEL% GTR 0 set E=1

coverage run -p more_jenkins_build.py
if %ERRORLEVEL% GTR 0 set E=1

::coverage run -p [FILENAME].py

echo.
echo ++++++++++++++++++ END OF TESTS ++++++++++++++++++
echo.

echo ### Coverage Reports
echo ### - coverage combine
echo ### ----- Combines all the reports made from tests
echo ### - coverage html -d coverage
echo ### ----- Makes a folder with HTML resualts under coverage.
echo ### - coverage xml -o coverage/coverage.xml
echo ### ----- Saves a XML to the coverage dir with name coverage.xml
echo Creating coverage directory if non...
mkdir coverage 1>> out.log 2>> error.log
echo Combinng and outputing...
coverage combine 
coverage html -d coverage
coverage xml -o coverage/coverage.xml
echo Done!
echo.

echo ### Running and Saving Pep8 data.
echo ### pep8 %%lintfiles%% ^> pep8.log
pep8 %lintfiles% > pep8.log
echo Done!
echo.

echo ### Running and Saving Pylint data.
echo ### - pylint --rcfile=pylint.rc %%lintfiles%% ^> pylint.log
pylint --rcfile=pylint.rc %lintfiles% > pylint.log
echo Done!
echo.

echo.
echo ##### END OF BUILD #####
echo %E%
pause
echo.
EXIT /B %E%


