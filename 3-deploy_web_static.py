#!/usr/bin/python3
"""
    Fabric script that creates and distributes an archive to webservers,
    using the function deploy
"""


from fabric.api import env, run, local, put, runs_once
from datetime import datetime
from os.path import exists

env.hosts = ['100.25.21.246', '3.85.41.202']
env.user = 'ubuntu'
env.key_filename = '/home/vagrant/.ssh/authorized_keys'


@runs_once
def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    try:
        local("mkdir -p versions")
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_path = "versions/web_static_{}.tgz".format(current_time)
        local("tar -cvzf {} web_static".format(file_path))
        return file_path
    except Exception as e:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not exists(archive_path):
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
        run("mv {}/web_static/* {}".format(remote_rel_path, remote_rel_path))

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


def deploy():
    """
    Deploy the web_static content to web servers
    """
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)
