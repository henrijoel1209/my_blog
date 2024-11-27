from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task(1)
    def index(self):
        self.client.get("/")

    @task(2)
    def about(self):
        self.client.get("/about")

    @task(3)
    def contact(self):
        self.client.get("/contact")

    @task(4)
    def categories(self):
        self.client.get("/categories")

    @task(5)
    def posts(self):
        self.client.get("/posts")

    @task(6)
    def create_post(self):
        self.client.post("/posts", json={"title": "Test Post", "content": "This is a test post."})

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
