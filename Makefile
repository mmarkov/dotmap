update:
	python update.py
	git commit -am "update version"
	git push origin master
	sudo python setup.py sdist upload -r pypi

test:
	flake8 .
	nosetests --with-coverage --cover-package=dotmap