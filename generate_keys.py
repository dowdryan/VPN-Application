import subprocess

# Generates Public & Private WireGuard keys
def generate_keys():
    private_key = subprocess.check_output(["wg", "genkey"]).decode().strip()
    public_key = subprocess.check_output(["wg", "pubkey"], input=private_key.encode()).decode().strip()
    return private_key, public_key

client_private, client_public = generate_keys()
