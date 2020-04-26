# Using VS Code remote development in Docker container (Ptyhton & Flask)
The main purpose of this repo is to create a sample Python app and try out development using VS Code's Remote Development feature with Docker continers. 

Motivation:
I would like to develop, interpret and run my Python code remotely without installing Python interpreter and packages on my Windows machine. Instead spin up a Python Docker container with all required dependencies.

Main tasks I want to achieve:
- [X] Setup remote Python development with Visual Studio Code
- [X] Create some simple REST APIs with Flask to
    - [X] return static index.html at `"/"`
    - [X] return text "Hello World" under `"/hello"`
    - [X] return Top 250 movies from IMDb at `"/imdb/movies/top250"`
        - scrape Imdb Top 250 movies table from webpage "https://www.imdb.com/chart/top/?ref_=nv_mv_250",
        - parse into class in "/model/topMovie.py"
        - serialize objects and return as Json array 
        ```
        {
            "results": [
            {
                "rank": "1.",
                "rating": "9.2",
                "title": "Die Verurteilten"
            },
            ...
        }
        ```

## Developing inside a Container
The Visual Studio Code Remote - Containers extension lets you use a Docker container as a full-featured development environment. 
[VS Code Remote guide](https://code.visualstudio.com/docs/remote/containers#_quick-start-open-a-folder-in-a-container)

### Install Plugins
With the help of these plugins you can easily create and develop your Python code.

1. [Python plugin for local edit](https://marketplace.visualstudio.com/items?itemName=ms-python.python) 

2. [Remote Containers plugin](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

# How to setup development in remote Python Docker container
1. Create devcontainer.json file (Hit F1 and select 'Remote-containers Create container configuration files')
2. Create docker-compose.yml [Sample](https://github.com/microsoft/python-sample-tweeterapp/blob/master/.devcontainer/docker-compose.yml)
3. Create Dockerfile [Sample](https://github.com/microsoft/python-sample-tweeterapp/blob/master/.devcontainer/Dockerfile)
4. Move these files to folder named '.devcontainer'
6. Create a 'requirements.txt' and '.temp.txt' to define which Python dependencies needed to be installed for your app (E.g.: flask)
    - For install requirements run command: `pip install -r requirements.txt`
5. Add sample python code (app.py and static files) from [VS code try python](https://github.com/microsoft/vscode-remote-try-python)
6. Hit F1 and select 'Remote-Containers: Reopen Folder in Container'
    1. Then VS Code will be reopen your workspace in remote window, connected to the VS Code server which is running  inside the container to provide a fully functional but remote development environment (based on .devcontainer folder) with terminal support and etc..
7. Open terminal and run this command to start the app: 'flask run'
8. Hit F1 and select 'Forward a Port' 
    - In older versions 'Remote-Containers: Forward Port from Container'
9. Enter port number 5000.
10. Open your browser and navigate to `localhost:5000`
    - (In older versions Click "Open Browser" in the notification that appears to access the web app on this new port.)



