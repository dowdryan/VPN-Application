from generate_keys import generate_keys
import subprocess

WG_CONF_PATH = "/etc/wireguard/wg0.conf"
WG_CLIENT_CONF_PATH = "/etc/wireguard/client.conf"

# Writes the server WireGuard configuration file that communicates with the client
# Replace IP addresses and ports as needed
def write_config(server_private_key, server_public_key):
    config = f"""
[Interface]
PrivateKey = {server_private_key}
Address = 0.0.0.0/32
ListenPort = 51820

[Peer]
PublicKey = {server_public_key}
AllowedIPs = 0.0.0.0/32
"""
    with open(WG_CONF_PATH, "w") as f:
        f.write(config)
    print(f"Config written to {WG_CONF_PATH}")

# Writes the client WireGuard configuration file
def write_client_config(client_private_key, client_public_key, endpoint):
    config = f"""
[Interface]
PrivateKey = {client_private_key}
Address = 10.0.0.2/24
DNS = 1.1.1.1, 1.0.0.1

[Peer]
PublicKey = {client_public_key}
Endpoint = {endpoint}:51820
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25
"""
    with open(WG_CLIENT_CONF_PATH, "w") as f:
        f.write(config)
    print(f"Config written to {WG_CLIENT_CONF_PATH}")

# Starts the VPN
def start_vpn():
    subprocess.run(["sudo", "wg-quick", "up", WG_CONF_PATH])
    subprocess.run(["sudo", "wg-quick", "up", WG_CLIENT_CONF_PATH])
    print("VPN started!")

# Stops the VPN
def stop_vpn():
    subprocess.run(["sudo", "wg-quick", "down", WG_CONF_PATH])
    subprocess.run(["sudo", "wg-quick", "down", WG_CLIENT_CONF_PATH])
    print("VPN stopped!")
    
# Check current public IP
result = subprocess.run(
    ["curl", "ifconfig.me"], capture_output=True, text=True
)
endpoint = result.stdout
    
# Configures the VPN by generating keys and writing config files
def configure_vpn():
    server_private, server_public = generate_keys()
    client_private, client_public = generate_keys()
    write_config(server_private, server_public)
    write_client_config(client_private, client_public, endpoint.strip())
    return server_private, server_public, client_private, client_public
