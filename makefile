YEAR = $(shell date +%Y)
DAY = $(shell date +%d)

help: 
	@echo "Commands:"
	@echo " - help: 	show this help"
	@echo " - init: 	set up the project"
	@echo " - new:		create a new file for today"
	@echo " - readme: 	build the new readme with links"

init: 
	@echo "Setting up the project"
	# Using aoc package
	@touch ~/.config/aocd/token
	@cd setup && touch session.cookie 
	@echo "Creating the folder for the current year and day"
	@echo "CURDIR: $(CURDIR) YEAR: $(YEAR) DAY: $(DAY)"
	@mkdir -p $(CURDIR)/$(YEAR)/$(DAY)
	@make help

new: 
	@echo "Creating a new file for today"
	python3 setup/utils/new_file.py

readme:
	@echo "Building the new readme with links"
	@python3 setup/utils/build_md.py