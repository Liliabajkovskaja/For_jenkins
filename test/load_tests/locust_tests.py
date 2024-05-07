from random import choice

from locust import FastHttpUser, task, between


class HelloWorldUser(FastHttpUser):

    # http://localhost:8000/api/users/
    @task
    def get_all_users(self):
        self.client.get("/api/users/")

    @task(2)
    def get_user(self):
        self.client.get(f"/api/users/{choice([1, 3, 5])}")

    wait_time = between(0, 1)
