from locust import HttpUser, task

class FrontEndUser(HttpUser):
    @task
    def home(self):
        self.client.get('')
        
    def login(self):
        self.client.get('login')
        
    def register(self):
        self.client.get('register')
        
    def twitter(self):
        self.client.get('twitter')
        
    def weather(self):
        self.client.get('weather')
        
    def routeStopInfo(self):
        self.client.get('routeStopInfo')
    
    def notFount(self):
        self.client.get('abcdef')
    
    