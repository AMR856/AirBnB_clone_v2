#!/usr/bin/python3
"""A module here to do stuff"""
from fabric.api import local
from datetime import datetime
import os
def do_pack():
    """A function to make a tar file fro the folder"""
    try:
        if os.path.isdir("versions") is False:
            local("mkdir versions")
        theDateVar = datetime.now().strftime("%Y%m%d%H%M%S")
        theFileName = f"versions/web_static_{theDateVar}.taz"
        local(f"tar -cvzf {theFileName} web_static")
        return f"{theFileName}"
    except Exception as Anything:
        return None
