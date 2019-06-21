# 6.20-Project-File
Details are shown in the gist<br>
## Pre-prepare if using:<br>
### flask setup
1. Begin by creating a new project directory:
```bash
$ mkdir project_test1
```
2. cd to the target file: <br>
```bash
$ cd project_test1
```
3. Within "project_test1", create a new directory called "server". 
```bash
$ mkdir server
$ cd server
```
4. enable virtual environment:
```bash
$ python3.7 -m venv env
$ source env/bin/activate
```
5. Install Flask along with the Flask-CORS extension:
```bash
(env)$ pip install Flask==1.0.2 Flask-Cors==3.0.7
```
6. Copy _app.py_ to the server directory
7. Run the app:(you can go to  http://localhost:5000/all or  http://localhost:5000/fail to see if it works)
```bash
(env)$ python app.py
```
### Vue setup
In a new terminal<br>
1. Install Vue CLI if you don't have it:
```bash
$ npm install -g @vue/cli@3.7.0
```
2. cd to project_test1:
```bash
$ cd project_test1
```
3. within "project-test1", initialize a new Vue project called client:
```bash
$ vue create client
```
The detailed initialization:
> This will require you to answer a few questions about the project. Use the down arrow key to highlight "Manually select features", and then press enter. Next, you'll need to select the features you'd like to install. For this tutorial, select "Babel", "Router", and "Linter / Formatter" like so:
```bash
Vue CLI v3.7.0
? Please pick a preset: Manually select features
? Check the features needed for your project:
 ◉ Babel
 ◯ TypeScript
 ◯ Progressive Web App (PWA) Support
❯◉ Router
 ◯ Vuex
 ◯ CSS Pre-processors
 ◉ Linter / Formatter
 ◯ Unit Testing
 ◯ E2E Testing
 ```
 >Use the history mode for the router. Select "ESLint + Airbnb config" for the linter and "Lint on save". Finally, select the "In package.json" option so that configuration is placed in the package.json file instead of in separate configuration files. You should see something similar to:
```bash
Vue CLI v3.7.0
? Please pick a preset: Manually select features
? Check the features needed for your project: Babel, Router, Linter
? Use history mode for router? Yes
? Pick a linter / formatter config: Airbnb
? Pick additional lint features: Lint on save
? Where do you prefer placing config for Babel, PostCSS, ESLint, etc.? In package.json
? Save this as a preset for future projects? (y/N) No
```
4. Delete or replace following files:<br>
    a. In _client_/_src_, remove _views_ folder.<br>
    b. In _client_/_src_, replace _App.vue_, _main.js_ and _router.js_ with the same-name file I provide.<br>
    c. In _client_/_src_/_components_, delete _HelloWorld.vue_. Copy my _csv_list.vue_ and _select_list.vue_ into the folder.
5.Back to terminal, cd into the client file:
```bash
$ cd client
```
6. install following things:
```bash
$ npm install axios@0.18.0 --save
$ npm install bootstrap@4.3.1 --save
$ npm install --save bootstrap-vue
```
7. Run the project(make sure the Flask is running in another terminal)
```bash
$ npm run serve
```
8. You may have some error, if you have anything else need to install, just follow the messages from the termianl.<br>
9. the url will be shown on the terminal, either add "/" or "/fail" to see if it works.
