# VPN-Application

Prerequisites:
Install WireGuard: ```sudo apt install wireguard```
Install Tkinter: ```sudo apt install python3-tk```

To start: ```sudo python3 GUI.py```
 - Hardcoded to automatically start the Wireguard client so you won't have to do it manually
 - Uses Tkinter to create a pop-up field where users can start and stop the VPN as they please.

Before running the file, make sure IPv4 fowarding is enabled by entering this command in the terminal ```net.ipv4.ip_forward=1```, then restart the server. 
 - This allows the computer to act as a router, making it possible to send IP packets between different network interfaces 

Issues:
 - Currently does not have a VPS to host the VPN
