# Flask Project:  Last Update **24-05-2021:   13:20**


## App Details

**Description:** - This app is designed to be a photography instructional tool.  Stay tuned as the repository updates for more information. There will a Home route, an "About" route and a route for photos lists and instructions.  To run the app in local development, make sure you include the folllowing code in ```app.py```. -  ```app.run(debug=True, port=8000, host='0.0.0.0')```. 

Use the command ```python app.py```

You will see a URL like this one in your Command Line interface or Terminal. http://0.0.0.0.20:8000/

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

+ Important deployment files include
  + A Heroku ```procfile```
  + requirements.txt
  + runtime.txt
  + A Python file as application entry point.   ```app.py``` is the entry point for this project.
  + Heroku CLI.  Git Version Control

#### Deployment

+ ```heroku create``` (you may first have to use ```heroku login``` in the CLI) 

+ A buildpack for your app should be specified in your Heroku Dashboard.  Mine is for Python,

+ Included a Procfile - ```web: gunicorn app:appi```  - This command will use the app module (fielname) and the name of the app declared in the entry point. A Procfile is used by Heroku to declare what command should be executed to start your app.

+ ```git push heroku main```  - use this git command to push changes to the repistory hosted by Heroku (as well as the repository you will use on GitHub)

+ If you are using local server debugging (i.e. ```app.run(debug=True, port=8000, host='0.0.0.0'```) make sure this is **switched off/commented** out in production)

+ It took me a lot of Googling and reading to learn the process of deploying and common "gotchas" when deploying an app like this. These are just a few of the links I used to get to successful deployment.
  + https://www.codecademy.com/articles/deploying-a-flask-app 
  + https://dev.to/techparida/how-to-deploy-a-flask-app-on-heroku-heb
  + https://www.codecademy.com/articles/deploying-a-flask-app


## Photo Tutorial Notes

+ 1) - Photo Sharpness - 
  + IMG_7440   f/9  1/4000sec  ISO-3200  at 100mm focal length.  But there's plenty of sunlight in these photos
  + IMB_7441  f/9 1/250sec  ISO-200 at 75mm focal length


### The App is currently deployed to
  + https://aqueous-thicket-63067.herokuapp.com/


https://git.heroku.com/aqueous-thicket-63067.git