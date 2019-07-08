# REST API developed using VS CODE remote development solution in Ptyhton & Flask to fetch month-by-month Hungarian working time hours

The main purpose of this repo is to create a REST API in Python with Flask by using VS Code Remote Development feature. The API should be able to retrieve the working time hours month-by-month. I working on this porject in Visual Studio Code and I would like to interpret my Python code remote in the locally running Python Docker container without installing Python on my machine.

Main tasks I want to achieve:
- [X] Setup remote Python development with Visual Studio Code
- [ ] Create REST API in Python and Flask

## How to use VS Code
Visual Studio Code is an ideal free, lightweight development environment instead of the market leader IntellIJ IDEA ultimate which has built-in Spring Boot support.

Official guide link: [Click here..](https://code.visualstudio.com/docs/java/java-spring-boot)

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
5. Add sample python code (app.py and static files) from [VS code try python](https://github.com/microsoft/vscode-remote-try-python)
6. Hit F1 and select 'Remote-Containers: Reopen Folder in Container'
    1. Then VS Code will be reopen your workspace in remote window, connected to the VS Code server which is running  inside the container to provide a fully functional but remote development environment (based on .devcontainer folder) with terminal support and etc..
7. Open terminal and run this command to start the app: 'flask run'
8. Hit F1 and select 'Remote-Containers: Forward Port from Container'
9. Select port 5000.
10. Click "Open Browser" in the notification that appears to access the web app on this new port.



