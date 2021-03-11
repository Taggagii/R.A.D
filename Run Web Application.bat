@ECHO OFF

:full
rmdir /S /Q web-application

git clone https://github.com/taggagii/web-application

cd web-application
pipenv install
start pipenv run app.py

:closeProcessLoop
if exist bye.txt (
	taskkill /f /im pipenv.exe
	cd ..
	goto full
)
goto closeProcessLoop

