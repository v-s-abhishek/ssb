import subprocess

def configure_firewall():
    rules = [
        'netsh advfirewall firewall add rule name="Allow SSH" dir=in action=allow protocol=TCP localport=22',
        'netsh advfirewall firewall add rule name="Allow HTTP" dir=in action=allow protocol=TCP localport=80',
        'netsh advfirewall firewall add rule name="Allow HTTPS" dir=in action=allow protocol=TCP localport=443'
    ]

    for rule in rules:
        subprocess.run(rule, shell=True)

    print("Firewall configured successfully.")

configure_firewall()
