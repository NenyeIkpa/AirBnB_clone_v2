#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

# Install Nginx if it not already installed
if ! command -v "nginx" &> /dev/null; then
	# Update package list
	sudo apt update
	# Install Nginx
	sudo apt install -y nginx
	# Adjust the firewall, enabling the most restrictive profile configured
	sudo ufw allow 'Nginx HTTP'
fi

# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
if [ ! -d "/data/web_static/releases/test/" ]; then
	sudo mkdir -p /data/web_static/releases/test/
fi

# Create the folder /data/web_static/shared/ if it doesn’t already exist
if [ ! -d "/data/web_static/shared" ]; then
        sudo mkdir -p /data/web_static/shared/
fi

# Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
sample_text="<html>
    <head>
        <title>Welcome to DevShowcase.tech!</title>
    </head>
    <body>
        <h1>Success! The devshowcase.tech server block is working!</h1>
    </body>
</html>"
echo "$sample_text" > /data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder
# If the symbolic link already exists, it should be deleted and recreated every time the script is ran
# -s creates the link; -f unlinks existing symlink and recreates the link
# sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
if [ -d "/data/web_static/current" ]; then
	rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist).
# This should be recursive; everything inside should be created/owned by this user/group.
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
path_to_file="/etc/nginx/sites-available/default"
if ! grep -q "location /hbnb_static/" "$path_to_file"; then
	sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
fi

sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'

# restart Nginx after updating the configuration
sudo service nginx restart
