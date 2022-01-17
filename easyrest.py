import os
from git.repo.base import Repo
from termcolor import colored
from pick import pick


projectname = input("type project name: ")


title = 'select a project type: '
options = ['Postgresql (sql)', 'Detabase (NoSQL)']

option, index = pick(options, title,
                     indicator='=>', default_index=0)


title2 = 'do you want to install dependencies ?'
options2 = ['yes', 'no']

depOption, index = pick(options2, title2,
                        indicator='=>', default_index=0)


optionUrl = str()

envToWrite = str()

if option == "Detabase (NoSQL)":

    optionUrl = "https://github.com/MauroMontan/fastApi-detaProject.git"
    envToWrite = "PROJECTKEY= 'here goes your deta project key'"

if option == 'Postgresql (sql)':
    optionUrl = "https://github.com/MauroMontan/FastApiPostgresProject.git"
    envToWrite = "DATABASE_URL = 'here goes your database URL'"


print(colored("\ngenerating project ...", "yellow"))
Repo.clone_from(optionUrl, projectname)


f = open(f'{projectname}/.env', 'a')


f.write(envToWrite)

f.close()


if depOption == "yes":

    try:
        print(colored("installing dependencies...", "yellow"))
        os.system(f"pip install -r {projectname}/requirements.txt")
    except:
        print(colored("could not install dependencies", "red"))

if depOption == "no":
    print(colored(
        f"type 'pip install -r requirements.txt' in your project folder\n", "magenta"))


print(colored(f"Project succesfuly created  \n ", "green"))
print(colored(f"- cd /{projectname}\n ", "magenta"))
print(colored(f"- uvicorn main:app --reload \n ", "green"))
print(colored(f"Have fun coding !\n ", "green"))
