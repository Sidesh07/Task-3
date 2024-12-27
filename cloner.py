import subprocess

def clone_repo_with_branch(repo_url, branch_name):
    """Clone a Git repository using SSH and checkout a specific branch."""
    print(f"Cloning the repository from {repo_url} and checking out branch '{branch_name}'...")

    # Clone the repository and checkout the specific branch
    subprocess.run(['git', 'clone', '-b', branch_name, repo_url], check=True)
    
    print(f"Repository cloned and switched to branch '{branch_name}'.")

# Example usage
repo_url = 'git@gitlab.rapidinnovation.tech:root/backend-nest-pro.git'  # SSH URL of the repository
branch_name = 'sidesh'  # The branch you want to clone

# Clone the repository with the specific branch
clone_repo_with_branch(repo_url, branch_name)
