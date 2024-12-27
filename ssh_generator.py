import os
import subprocess

# Define the path to the SSH key
ssh_key_path = os.path.expanduser("~/.ssh/id_rsa")
public_key_path = ssh_key_path + ".pub"

# Function to generate SSH key
def generate_ssh_key():
    # Check if the SSH key already exists
    if not os.path.exists(ssh_key_path):
        print("SSH key not found. Generating a new one...")
        # Generate a new SSH key
        subprocess.run(["ssh-keygen", "-t", "rsa", "-b", "4096", "-f", ssh_key_path, "-N", ""])
        print(f"SSH key generated and saved to {ssh_key_path}")
    else:
        print("SSH key already exists. Displaying the public key...")
        # Display the public key if it exists
        with open(public_key_path, "r") as pub_key_file:
            print(pub_key_file.read())

# Run the function
generate_ssh_key()
