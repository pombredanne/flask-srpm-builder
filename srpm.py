#!/usr/bin/env python3

from pyrpm.spec import Spec, replace_macros

def parse_spec(package_name, path):
    spec = Spec.from_file(str(path + "/" + package_name + ".spec"))
    
    print(spec.version)
    print(spec.sources[0])  # http://llvm.org/releases/%{version}/%{name}-%{version}.src.tar.xz
    print(replace_macros(spec.sources[0], spec))  # http://llvm.org/releases/3.8.0/llvm-3.8.0.src.tar.xz

#    for package in spec.packages:
#        print(f'{package.name}: {package.summary if hasattr(package, "summary") else spec.summary}')
