#!/usr/bin/env python3

import os

def clone(clone_url, full_name, author, branch, where="/tmp"):
    repo_name = full_name[full_name.rfind("/")+1:]
    d = where + "/" + author + "/" + repo_name + "/"
    os.system("mkdir -p " + d)
    os.system("rm -rf " + d + branch)
    os.system("git clone " + clone_url + " " + d + branch)
    os.system("cd " + d + branch + " ; git checkout " + branch)
    return d + branch
