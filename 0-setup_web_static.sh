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
if [ ! -f "/data/web_static/releases/test/index.html" ]; then
	echo "$sample_text" > /data/web_static/releases/test/index.html
fi

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder
# If the symbolic link already exists, it should be deleted and recreated every time the script is ran
if [ -h "/data/web_static/current" ]; then
	sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist).
# This should be recursive; everything inside should be created/owned by this user/group.
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
path_to_file="/etc/nginx/sites-available/default"
string_to_find='server_name _;'
string_to_append='\\n\tlocation /hbnb_static/ {\n\t\talias /var/www/devshowcase.tech/hbnb_static;\n\t}'
# string_to_append='
#    \tlocation /hbnb_static/ {
#    \t\troot /var/www/devshowcase.tech;
#    \t\talias /var/www/devshowcase.tech/hbnb_static;
# \t}'
if ! grep -q "location /hbnb_static/" "$path_to_file"; then
	sed -i "/$string_to_find/a$string_to_append" /etc/nginx/sites-available/default
fi

# restart Nginx after updating the configuration
sudo service nginx restart
