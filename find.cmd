@echo off

@REM Check the number of factors
if "%~1"=="" (
    echo No parameters was entered.
    exit /b 1
)

if "%~2"=="" (
    python find_native_python.py %1
) else (
    echo Too many parameters. Please enter only 1 parameter.
    exit /b 1
)



