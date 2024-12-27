import subprocess

def install_and_enable_docker_linux():
    """Install and enable Docker on Linux (Ubuntu/Debian)."""
    print("Installing Docker on Linux (Ubuntu/Debian)...")

    # Update package list
    subprocess.run(['sudo', 'apt-get', 'update'], check=True)
    
    # Install Docker
    subprocess.run(['sudo', 'apt-get', 'install', '-y', 'docker.io'], check=True)
    
    # Start Docker service
    subprocess.run(['sudo', 'systemctl', 'start', 'docker'], check=True)
    
    # Enable Docker to start on boot
    subprocess.run(['sudo', 'systemctl', 'enable', 'docker'], check=True)
    
    print("Docker installed and started successfully on Linux.")

# Run the function to install and enable Docker
install_and_enable_docker_linux()
