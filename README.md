# 6.20-Project-File
Details are shown in the gist<br>
## Pre-prepare if using:<br>
### flask setup
cd to the target file: <br>
```bash
$ cd project_test1
```
cd to server file:
```bash
$ cd server
```
enable virtual environment:
```bash
$ python3.7 -m venv env
$ source env/bin/activate
```
Install Flask along with the Flask-CORS extension:
```bash
(env)$ pip install Flask==1.0.2 Flask-Cors==3.0.7
```
Run the app:
```bash
(env)$ python app.py
```
### Vue setup
In a new terminal<br>
Install Vue CLI if you don't have it:
```bash
$ npm install -g @vue/cli@3.7.0
```
cd to project_test1:
```bash
$ cd project_test1
```
If you want to create a new vue project you should type: `$ vue create client`(detail:https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/) , here you just do the following to run:
```bash
$ cd client
$ npm run serve
```
You may have some error, just install following things:
```bash
$ npm install axios@0.18.0 --save
$ npm install bootstrap@4.3.1 --save
```
If you have anything else need to install, just follow the messages from the termianl. 
