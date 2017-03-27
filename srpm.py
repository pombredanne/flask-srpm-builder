#!/usr/bin/env python3

from pyrpm.spec import Spec, replace_macros
import os

def spec_build_srpm(package_name, path):
    os.system("set -x; rpmbuild --define \"_topdir " + path + "/rpmbuild" + "\"" + " -bs " + path + "/rpmbuild/SPECS/" + package_name + ".spec")

def spec_fetch_sources(package_name, path):
    spec = Spec.from_file(str(path + "/" + package_name + ".spec"))

    for s in spec.sources:
        source = replace_macros(s, spec)

        if source.find("http://") >= 0:
            os.system("wget " + source)
            os.system("mv " + source[source.rfind("/")+1:] + " " + path + "/rpmbuild/SOURCES/")
        else:
            os.system("cp " + path + "/" + source + " " + path + "/rpmbuild/SOURCES/")

#    print(spec.version)
#    print(spec.sources[0])
#    print(replace_macros(spec.sources[0], spec))

def generate_rpmbuild(package_name, path):
    os.system("mkdir -p " + path + "/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}")
    os.system("cp " + path + "/" + package_name + ".spec " + path + "/rpmbuild/SPECS/")

