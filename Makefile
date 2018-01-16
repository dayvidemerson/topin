deploy:
	git push heroku master
	heroku run python3 manage.py migrate

shell:
	heroku run python3 manage.py shell_plus