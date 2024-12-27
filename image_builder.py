import subprocess
import os

def build_docker_image(dockerfile_directory, image_name='my_docker_image:latest'):
    """Build a Docker image from a Dockerfile."""
    print(f"Building Docker image from directory '{dockerfile_directory}'...")

    # Expand ~ to the full home directory path
    dockerfile_directory = os.path.expanduser(dockerfile_directory)

    # Change to the directory containing the Dockerfile
    os.chdir(dockerfile_directory)

    # Build the Docker image using sudo
    subprocess.run(['sudo', 'docker', 'build', '-t', image_name, '.'], check=True)
    
    print(f"Docker image '{image_name}' built successfully.")

def run_docker_container(image_name='my_docker_image:latest', container_name='my_container'):
    """Run a Docker container from the built image."""
    print(f"Running Docker container from image '{image_name}'...")

    # Check if the container already exists
    container_check = subprocess.run(['sudo', 'docker', 'ps', '-a', '--filter', f'name={container_name}', '--format', '{{.Names}}'], capture_output=True, text=True)
    
    if container_check.stdout.strip() == container_name:
        print(f"Container '{container_name}' already exists. Removing it...")
        # Stop and remove the existing container
        subprocess.run(['sudo', 'docker', 'rm', '-f', container_name], check=True)
        print(f"Container '{container_name}' removed.")

    # Run the Docker container using sudo
    subprocess.run(['sudo', 'docker', 'run', '-d', '--name', container_name, image_name], check=True)
    
    print(f"Docker container '{container_name}' is running.")

# Example usage
dockerfile_directory = '~/CODE/backend-nest-pro'  # Path to the directory containing your Dockerfile
image_name = 'nest'  # Name of the Docker image
container_name = 'nest_con'  # Name for the running container

# Build Docker image
build_docker_image(dockerfile_directory, image_name)

# Run Docker container
run_docker_container(image_name, container_name)
