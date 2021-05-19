# Flask Project:  Last Update **19-05-2021:   11:47**

## Served at Heroku

### Developer Notes - Heroku Deployment Instructions

+ I'm using the installer for Windows, Git Bash and Heroku CLI for this deployment.

+ Heroku App name: ```jgdm-flask-project```

+ Used the installer ```CLI 7.53.0```. I then updated it to 7.54.0 via the CLI. 

  + **Commands**
  + heroku update
  + heroku help
  + heroku --version

  
#### Deployment

+ ```heroku create```  (you may first have to use ```heroku login``` in the CLI)
  

https://git.heroku.com/aqueous-thicket-63067.git | https://aqueous-thicket-63067.herokuapp.com/ git

+ A buildpack for your app should be specified in your Heroku Dashboard.  Mine is for Python,

+ Included a Procfile - ```web: gunicorn gettingstarted.wsgi```

+ ```git push heroku main```

... 