#!/usr/bin/env python3

import os

def parse_name(full_name):
    repo_name = full_name[full_name.rfind("/")+1:]
    if repo_name.find("-fedora") >= 0:
        repo_name = repo_name[:-7]
    print("parse_name: " + repo_name)
    return repo_name


def clone(clone_url, full_name, author, branch, where="/tmp"):
    repo_name = parse_name(full_name)
    d = where + "/" + author + "/" + repo_name + "/"
    os.system("mkdir -p " + d)
    os.system("rm -rf " + d + branch)
    os.system("git clone " + clone_url + " " + d + branch)
    os.system("cd " + d + branch + " ; git checkout " + branch)
    return d + branch

