from locust import HttpUser, TaskSet, task, between
import json
import random

archivo_json = 'fakeData.json'
with open(archivo_json, 'r', encoding='utf-8') as f:
    datos = json.load(f)

class UserTasks(TaskSet):

    """@task
    def create_cache(self):
        self.client.post("/create", json=random.choice(datos))
        
    @task
    def read_cache(self):
        self.client.get("/read", json=random.choice(datos))
        
    @task
    def update_cache(self):
        self.client.put("/update", json=random.choice(datos))
        
    @task
    def delete_cache(self):
        self.client.delete("/delete", json=random.choice(datos))"""
        
    @task    
    def cache(self):
        self.client.post("/cache", json=random.choice(datos))

class WebsiteUser(HttpUser):
    tasks = [UserTasks]
    wait_time = between(1, 5)