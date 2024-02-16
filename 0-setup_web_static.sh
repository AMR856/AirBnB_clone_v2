#!/usr/bin/env bash
# A script to configure some stuff
sudo apt-get -y upgrade
sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p /data/ /data/web_static/ /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
echo "Hi Nginx" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -HR ubuntu:ubuntu /data/
sudo sed -i '39i#\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
