echo ### - Deleteing files ^& Removeing dirs
echo ### --- del *.coverage
echo ### --- del *.log
echo ### --- RD /S /Q coverage
echo ### --- RD /S /Q python_tests_xml
echo ### --- RD /S /Q __pycache__
echo ### --- RD /S /Q wwwApp\__pycache__
echo ### --- RD /S /Q wwwTests\__pycache__

del *.coverage*
del *.log
RD /S /Q coverage
RD /S /Q python_tests_xml
RD /S /Q __pycache__
RD /S /Q wwwApp\__pycache__
RD /S /Q wwwTests\__pycache__
