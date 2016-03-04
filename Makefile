LIST = build-essential gcc libxml2 python-dev python3-dev python-pip \
git nginx redis-server python-software-properties nodejs python-virtualenv \
postgresql postgresql-contrib postgresql-server-dev-9.3 libpq-dev libjpeg-dev

default:
	# ####################################
	# UPDATE & INSTALL REQUIRED PROGRAMS #
	# ####################################

	curl -sL https://deb.nodesource.com/setup_5.x | sudo -E bash -
	sudo apt-get update
	sudo apt-get install $(LIST)

	# #############
	# NPM GLOBALS #
	# #############

	cp restorus/config/.npmrc $(HOME)/.npmrc

	# ############################
	# INSTALL GLOBAL NPM MODULES #
	# ############################

	npm install npm -g
	npm install bower -g

	# ############
	# VIRTUALENV #
	# ############

	virtualenv -p /usr/bin/python3 ../

	# #############################
	# # LOCAL PYTHON REQUIREMENTS #
	# #############################

	../bin/pip install -r requirements.txt
	mkdir assets
	mkdir media

	# ###########
	# # TEST DB #
	# ###########

	sudo su - postgres
	createdb restorus
	createuser -P -s restorus

	# ####################
	# BOWER REQUIREMENTS #
	# ####################

	bower install

	# #######
	# NGINX #
	# #######

	sudo cp restorus/config/restorus.conf /etc/nginx/sites-available/restorus.conf
	sudo ln -s /etc/nginx/sites-available/restorus.conf /etc/nginx/sites-enabled/restorus.conf
	sudo service nginx restart

	# ###########
	# RUN TESTS #
	# ###########

	../bin/python manage.py test

	# ###################################
	# MAKE COMPLETE, HAVE A NICE DAY.   #
	# IT IS RECOMMENDED THAT YOU REBOOT #
	# BEFORE RUNNING THE APPLICATION    #
	# ###################################
