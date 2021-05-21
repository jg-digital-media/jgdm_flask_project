# Flask Project:  Last Update **21-05-2021:   09:5**


## App Details

This app is designed to be a photography instructional tool.  Stay tuned as the repository updates for more information


## Deployed to Heroku

### Developer Notes - Heroku Deployment Instructions

+ I'm using the installer for Windows, Git Bash and Heroku CLI for this deployment.

+ Heroku App name: ```jgdm-flask-project```

+ I used used the Windows installer ```CLI 7.53.0``` to install and use Heroku. I then updated it to 7.54.0 via the CLI. 

  + **Commands**
  + heroku login
  + heroku create
  + heroku restart
  + heroku update
  + heroku help
  + heroku --version
  + heroku local
  + heroku open
  + heroku logs --tail

  
#### Deployment

+ ```heroku create``` (you may first have to use ```heroku login``` in the CLI)
 

+ A buildpack for your app should be specified in your Heroku Dashboard.  Mine is for Python,

+ Included a Procfile - ```web: gunicorn app:appi```  - This command will use the app module (fielname) and the name of the app declared in the entry point. A Procfile is used by Heroku to declare what command should be executed to start your app.

+ ```git push heroku main```  - use this git command to push changes to the repistory hosted by Heroku (as well as the repository you will use on GitHub)

+ If you are using local server debugging (i.e. ```app.run(debug=True, port=8000, host='0.0.0.0'```) make sure this is **switched off/commented** out in production)

+ It took me a lot of Googling and reading to learn the process of deploying and common "gotchas" when deploying and app like this. These are just a few of the links I used to get to auccessfull deployment
  + https://www.codecademy.com/articles/deploying-a-flask-app 
  + https://dev.to/techparida/how-to-deploy-a-flask-app-on-heroku-heb
  + https://www.codecademy.com/articles/deploying-a-flask-app



### The App is currently deployed to
  + https://aqueous-thicket-63067.herokuapp.com/


https://git.heroku.com/aqueous-thicket-63067.git