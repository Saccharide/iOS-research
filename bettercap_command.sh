

# To use bettercap to capture outgoing and incoming traffic:
# Included tcp proxy and a customized module to capture the tcp dump of the request.
sudo bettercap -X -T 192.168.8.208 --proxy-https --tcp-proxy --tcp-proxy-upstream api.xbcs.net:8443 --proxy --tcp-proxy-module tcp-dump.rb


