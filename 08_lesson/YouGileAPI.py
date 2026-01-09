import requests

class YouGileAPI:
    def __init__(self, base_url, token, user_id):
        self.base_url = base_url
        self.token = token
        self.user_id = user_id
    
    def create_project(self, title, role="admin"):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        
        data = {
            "title": title,
            "users": {self.user_id: role}
        }
        
        resp = requests.post(f"{self.base_url}projects", headers=headers, json=data)
        return resp
    
    def get_project(self, project_id):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        resp = requests.get(f"{self.base_url}projects/{project_id}", headers=headers)
        return resp
    
    def change_project(self, project_id, title = None, users = None):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

        data = {}

        if title is not None:
            data['title'] = title
        if users is not None:
            data['users'] = users

        resp = requests.put(f'{self.base_url}projects/{project_id}', headers=headers, json=data)
        return resp