#!/usr/bin/python3
"""A module here to do stuff"""
from fabric.api import run, put
from fabric.api import env
import os

env.hosts = ['34.224.3.252', '100.25.129.71']


def do_deploy(archive_path):
    """Just be moduled for me"""
    if os.path.isfile(archive_path) is False:
        return False
    fileA = archive_path.split('/')[1]
    fileNo = fileA.split('.')[0]
    Path = '/data/web_static/releases/'
    if put(archive_path, f"/tmp/{fileA}").failed is True:
        return False
    if run("mkdir -p {}{}/".format(Path, fileNo)).failed is True:
        return False
    if run(f"tar -xzf /tmp/{fileA} -C {Path}{fileNo}/").failed is True:
        return False
    if run(f"/tmp/{fileA}").failed is True:
        return False
    if run(f"mv {Path}{fileNo}/web_static/* {Path}{fileNo}/").failed is True:
        return False
    if run(f"rm -rf {Path}{fileNo}/web_static").failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run(f"ln -s {Path}{fileNo} /data/web_static/current").failed is True:
        return False
