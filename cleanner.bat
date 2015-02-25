echo ### - Deleteing files ^& Removeing dirs
echo ### --- del *.coverage
echo ### --- del *.log
echo ### --- RD /S /Q coverage
echo ### --- RD /S /Q python_tests_xml
echo ### --- RD /S /Q __pycache__
echo ### --- RD /S /Q webapp\__pycache__
echo ### --- RD /S /Q webapp_tests\__pycache__

del *.coverage*
del *.log
RD /S /Q coverage
RD /S /Q python_tests_xml
RD /S /Q __pycache__
RD /S /Q webapp\__pycache__
RD /S /Q webapp_tests\__pycache__
RD /S /Q webapp\db17b1a5c2b2f6d370af2c59c885d5db\*.db-journal