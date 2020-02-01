from subprocess import call

call("pip freeze > requirements.txt", shell=True)