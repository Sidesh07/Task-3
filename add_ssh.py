import requests

def add_ssh_key_to_gitlab(api_url, api_token, ssh_key, title):
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    data = {
        "title": title,
        "key": ssh_key
    }
    try:
        response = requests.post(f"{api_url}/user/keys", headers=headers, json=data)
        if response.status_code == 201:
            print("SSH key added successfully to GitLab.")
        else:
            print(f"Failed to add SSH key to GitLab: {response.status_code}, {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while communicating with GitLab: {e}")

if __name__ == "__main__":
    gitlab_api_url = "https://gitlab.rapidinnovation.tech/api/v4"
    gitlab_api_token = "glpat-_Q5-bKQBZMMkX_KJ9F3v"
    ssh_key = """ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC+mWHxKdpqrP+I/c01vvPnAZBeUYT7TCXeiFqzi8+YcTU5Omvb/76B2foOG65vrStoHT8K0W6cUYj8w5GFQWZTopGSVZHXkZZpQ0rljiKLJAaHe5pJmUKS04viaFiwi3hDvYSR3PCjtl7EQsyo3/7AsbRTNzhQMB9SpFShx15ypexwxKTszAwG5mtNKjosly+4v0K+E89McYGp4qQxsMsNCYECexOz6FiH5zZE2YEVrV1LpULRwZQ/5JTsD19fEBIqBKmV3LhMhh/FrppvLtuimdoK3SnqO6OnQXic3qoNfEDGeOe683ZRF/aEJbx/jSUQOPgnV3asPKJ8Gx59YtvzppsBIortQWM9cnRNTbSKk5/nWXGPmQhXA7I8WHaBl0osRLhEHxK9uPpzK2NejXyvYfnPMoQSi9HxKUv9Z9QR97+F+b6QCAIKmf/U+S2TvL+Xom3x45tizQaI9W25QLerxuEn9GOXVOQPyfkLTIOZ5gKKJoq6PLewW4mTZKuBjP4VyTKw+gg2pwoRMpJ5gf5+UE/kODDKDMYLF5NYz65jRTEcciD08LBhpxz3dZG8ZiVnpiHM57MbgKK5PNrfUzUhEYTPcKK2lgWXuT1UvGaR4n+VSZBcBo2+Vtagz5VO7YwPWf8iMD5yBVg0ZPRTJDUoxp5hjtnTLbRBPX7Vm91McQ== sidesh@rapidinnovation.dev"""
    ssh_key_title = "My SSH Key"
    add_ssh_key_to_gitlab(gitlab_api_url, gitlab_api_token, ssh_key, ssh_key_title)
