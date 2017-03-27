#!/usr/bin/env python3

import git
import srpm
from flask import Flask, request

app = Flask(__name__)

debug = True

branch = None
pusher = None
clone_url = None
full_name = None
path = None

@app.route("/")
def default():
    return "SRPM - builder"

@app.route("/payload", methods=["POST"])
def process_hooks():

    if request.headers["X-Github-Event"] == "ping":
        return "Pong...", 200

    if  not request.headers["X-Github-Event"] == "push" or not request.json:
        return "This is not a github webhook!", 405


    branch = request.json["ref"][request.json["ref"].rfind("/")+1:]
    pusher = request.json["pusher"]
    clone_url = request.json["repository"]["clone_url"]
    full_name = request.json["repository"]["full_name"]

    if debug:
        print(request.json)
        print(pusher)
        print("branh = " + branch)
        print("clone_url = " + clone_url)
        print("full_name = " + full_name)

    path = git.clone(clone_url, full_name, pusher["name"], branch)

    srpm.generate_rpmbuild(git.parse_name(full_name), path)
    srpm.spec_fetch_sources(git.parse_name(full_name), path)
    srpm.spec_build_srpm(git.parse_name(full_name), path)

    branch = None
    pusher = None
    clone_url = None
    full_name = None
    path = None
    return "Proccessing...", 200

if __name__ == "__main__":
    app.run(host="138.197.100.149")
