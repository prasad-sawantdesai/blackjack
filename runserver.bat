@echo off
:: Activate virtual enviornment and run the server 
set message=activating virtual enviornment 
echo %message%

set message=Setting up project directory path ... 
echo %message%

set root=%cd%
::echo %root%

set env_activate_path=%root%\Scripts
::echo %env_activate_path%

set message=Actiavating virtual enviornment ... 
echo %message%

cd %env_activate_path%
call activate

set django_project_path=%root%\blackjack_project
::echo %django_project_path%

cd %django_project_path%

set message=Starting Django server ... 
echo %message%

call python manage.py runserver

