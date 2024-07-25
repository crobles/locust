from locust import HttpUser, TaskSet, task, between
import json
import random

# Cargar los datos del archivo JSON
archivo_json = 'fakeData.json'
with open(archivo_json, 'r', encoding='utf-8') as f:
    datos = json.load(f)

class UserTasks(TaskSet):

    """@task
    def create_cache(self):
        # Realizar una solicitud POST a la ruta /create
        response = self.client.post("/create", json=random.choice(datos))
        print(f"Create response status: {response.status_code}, response: {response.text}")

    @task
    def read_cache(self):
        # Realizar una solicitud GET a la ruta /read
        # Dependiendo de cómo funcione tu API, es posible que necesites pasar parámetros en la URL o el cuerpo de la solicitud
        data = random.choice(datos)
        response = self.client.get("/read")
        print(f"Read response status: {response.status_code}, response: {response.text}")

    @task
    def update_cache(self):
        # Realizar una solicitud PUT a la ruta /update
        response = self.client.put("/update", json=random.choice(datos))
        print(f"Update response status: {response.status_code}, response: {response.text}")

    @task
    def delete_cache(self):
        # Realizar una solicitud DELETE a la ruta /delete
        data = random.choice(datos)
        response = self.client.delete("/delete")
        print(f"Delete response status: {response.status_code}, response: {response.text}")"""
        
    @task
    def cache(self):
        # Realizar una solicitud POST a la ruta /create
        response = self.client.post("/cache", json=random.choice(datos))
        print(f"Create response status: {response.status_code}, response: {response.text}")

class WebsiteUser(HttpUser):
    tasks = [UserTasks]
    wait_time = between(1, 5)