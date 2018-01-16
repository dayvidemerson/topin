deploy:
	git push heroku master

shell:
	heroku run python3 manage.py shell_plus