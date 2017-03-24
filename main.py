#!/usr/bin/env python3

import git
from flask import Flask, request
app = Flask(__name__)

debug = True

branch = None
pusher = None
clone_url = None
repo_name = None
directory = None

@app.route("/")
def default():
    return "SRPM - builder"

@app.route("/payload", methods=["POST"])
def process_hooks():

    if  not request.headers["X-Github-Event"] or not request.json:
        return "This is not a github webhook!", 405

    branch = request.json["ref"][request.json["ref"].rfind("/")+1:]
    pusher = request.json["pusher"]
    clone_url = request.json["repository"]["clone_url"]
    repo_name = request.json["repository"]["full_name"]
   
    if debug:
        print(request.json)
        print(pusher)
        print(branch)
        print(clone_url)
        print(repo_name)

    directory = git.clone(clone_url, repo_name, pusher["name"], branch)



    branch = None
    pusher = None
    clone_url = None
    repo_name = None
    directory = None
    return "Proccessing...", 200

if __name__ == "__main__":
    app.run(host="138.197.100.149")
