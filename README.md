# Karek

## Setup Instruction Steps (on Ubuntu 14.04)
Required:
* Python 3.4=<
* Pip
* Virtualenv

## Install Python 3
```
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6
```

## Install pip
```
apt-get -y install python-pip3
```

## Install Virtualenv Virtualenvwrapper

Installing virtualenv and virtualenvwrapper using pip:
```
sudo pip3 install virtualenv virtualenvwrapper
```
Add following lines in ~/.bashrc :
```
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```
Creating new environment:
```
virtualenv env-name
```
List of environments:
```
workon
```
Change environment:
```
workon env-name
```
Deactivate(Exit from) environmet:
```
deactivate
```
Delete environment:
```
rmvirtualenv env-name
```
In activated environment you can install packages using pip:
```
pip3 install django
```
or specified version
```
pip3 insatall django==1.8
```

## Import django project

For example:
```
git clone https://github.com/altyn/Karek.git
```
Export all required packages to requirements.txt:
```
pip3 freeze > requirements.txt
```
This way allow you to avoid "Package not found" and other types of errors in future:
```
pip3 install -r requirements.txt
```
If it required make migrations, type following commands:

```
python manage.py makemigrations
python manage.py migrate
```
After that, if:
* Dependecies satisfied
* Requirements installed
* Migrations passed
```
python manage.py runserver localhost:8000
```
and follow in browser http://localhost:8000
