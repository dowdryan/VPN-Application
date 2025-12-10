import tkinter as tk
import generate_client

# Adds buttons to start and stop the VPN
def start_click():
    generate_client.configure_vpn()
    generate_client.start_vpn()

def stop_click():
    generate_client.stop_vpn()

root = tk.Tk()
root.title("WireGuard VPN")

tk.Button(root, text="Start VPN", command=start_click).pack(pady=10)
tk.Button(root, text="Stop VPN", command=stop_click).pack(pady=10)

root.mainloop()
