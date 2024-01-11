#!/usr/bin/python3
'''Fabric script to generate .tgz archive'''
from fabric.api import local
from datetime import datetime
from fabric.decorators import runs_once
import os


@runs_once
def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""

    # Create the versions folder if it doesn't exist
    if not os.path.exists("versions"):
        local("mkdir versions")

    # Generate the archive name
    now = datetime.now()
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
        now.year,
        now.month,
        now.day,
        now.hour,
        now.minute,
        now.second
    )

    # Create the tar archive
    result = local("tar -cvzf versions/{} web_static".format(archive_name))

    # Check if the archive has been correctly generated
    if result.succeeded:
        return "versions/{}".format(archive_name)
    else:
        return None


if __name__ == "__main__":
    do_pack()
