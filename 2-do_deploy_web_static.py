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
    fileNameAll = archive_path.split('/')[1]
    fileNameWithoutExt = fileNameAll.split('.')[0]

    if put(archive_path, f"/tmp/{fileNameAll}").failed is True:
        return False
    if run(f"mkdir -p /data/web_static/releases/{fileNameWithoutExt}/").failed is True:
        return False
    if run(f"tar -xzf /tmp/{fileNameAll} -C /data/web_static/releases/{fileNameWithoutExt}/").failed is True:
        return False
    if run(f"/tmp/{fileNameAll}").failed is True:
        return False
    if run(f"mv //data/web_static/releases/{fileNameWithoutExt}/web_static/* /data/web_static/releases/{fileNameWithoutExt}/").failed is True:
        return False
    if run(f"rm -rf /data/web_static/releases/{fileNameWithoutExt}/web_static").failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run(f"ln -s /data/web_static/releases/{fileNameWithoutExt} /data/web_static/current").failed is True:
        return False
