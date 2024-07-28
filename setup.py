from fabric.api import env, put, run

env.hosts = ["54.173.213.141", "3.80.19.61"]

def do_deploy(archive_path):
    if not archive_path:
        return False

    # Upload the archive to the /tmp/ directory of the web server
    put(archive_path, '/tmp/')

    # Extract the archive in the proper directory
    run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/'.format(archive_path.split("/")[-1].split(".")[0]))

    # Remove the archive from the /tmp/ directory
    run('rm /tmp/{}'.format(archive_path.split("/")[-1]))

    # Move the contents to the correct directory
    run('mv /data/web_static/releases/web_static/* /data/web_static/releases/web_static_{}/'.format(archive_path.split("/")[-1].split(".")[0]))

    # Delete the symbolic link
    run('rm -rf /data/web_static/current')

    # Create a new symbolic link
    run('ln -s /data/web_static/releases/web_static_{}/ /data/web_static/current'.format(archive_path.split("/")[-1].split(".")[0]))
"setup" 28L, 983C
