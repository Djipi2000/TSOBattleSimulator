@echo off
coverage run --source=. -m unittest discover -s tests/
coverage html
coverage report
pause
