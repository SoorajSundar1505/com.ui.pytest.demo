@echo off

REM Assuming you are in the root directory of your project

REM Delete the contents of the REPORT folder
del /q Allure-Report\*.*

REM Run your tests and generate new Allure reports
pytest .\Tests\ -k order -m "sanity" -v --alluredir=Allure-Report

REM Open the Allure report in the browser (optional)
allure serve Allure-Report
