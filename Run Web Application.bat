@ECHO OFF

:existsLoop
if not exist web-application (
	rmdir /S /Q web-application
	git clone https://github.com/taggagii/web-application
	goto existsLoop
) else (
	cd web-application
)
pipenv install 
pipenv run app.py
