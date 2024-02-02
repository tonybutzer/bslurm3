cat:
	cat Makefile


all:
	(cd .. ; make all)


publish:
	git add .
	git commit -m "auto commit for jira tracking make - nov2023"
	git push
git: publish

big:
	find . -size +20M
