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
    #gitlab_api_url = url
    #gitlab_api_token = api
    #ssh_key=ssh
    #ssh_key_title = "My SSH Key"
    #add_ssh_key_to_gitlab(gitlab_api_url, gitlab_api_token, ssh_key, ssh_key_title)
