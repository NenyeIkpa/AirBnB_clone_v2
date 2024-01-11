#!/usr/bin/python3
"""
    Fabric script that distributes an archive
    to web servers using do_deploy function
"""

from fabric.api import env, put, run, local
from datetime import datetime
import os

env.hosts = ['100.25.21.246', '3.85.41.202']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = archive_path.split('/')[-1]
        archive_no_ext = archive_name.split('.')[0]
        remote_tmp_path = "/tmp/{}".format(archive_name)
        remote_rel_path = "/data/web_static/releases/{}".format(archive_no_ext)

        # Upload the archive
        put(archive_path, remote_tmp_path)

        # Uncompress the archive
        run("mkdir -p {}".format(remote_rel_path))
        run("tar -xzf {} -C {}".format(remote_tmp_path, remote_rel_path))

        # Move contents of web_static folder
        run("mv {}web_static/* {}".format(remote_rel_path, remote_rel_path))

        # Remove the web_static folder
        run("rm -rf {}web_static".format(remote_rel_path))

        # Delete the archive from the server
        run("rm {}".format(remote_tmp_path))

        # Delete the current symbolic link
        run("rm -f /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(remote_rel_path))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Deployment failed: {}".format(str(e)))
        return False
