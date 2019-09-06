## Installation

### For local enviroment

1. Download the zip and unzip it, or clone the repository using the command
   `git clone https://github.com/Kevhann/HearthstoneCardDB.git`

2. Navigate to where you cloned/unzipped the folder.
3. In the root folder of the application "HearthstoneCardDB", activate the virtual enviroment byt running `source venv/bin/activate` You should see "(venv)" in your command line prompt
4. Install the project dependencies with command `pip install -r requirements.txt`
5. Launch the project with command `python run.py`

### Launch to heroku

Before launching to heroku, you need to have the files in your local git repository. If you cloned the repo, you need to delete the old .git folder. Create a new git repo with

```git create```

Create a new heroku project

```heroku create```

It should return with the name of your project in the format of 

```https://git.heroku.com/your-project-name.git```

Add the remote to your local git

```git remote add heroku https://git.heroku.com/your-project-name.git```

Add some configuration for heroku

```heroku config:set HEROKU=1```

Add a database to heroku

```heroku addons:add heroku-postgresql:hobby-dev```

Add and commit
```git add .```
```git commit -m "heroku"```

Push your project to heroku

```git push heroku master```
