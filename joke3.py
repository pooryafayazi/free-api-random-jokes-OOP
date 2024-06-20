from abc import ABC, abstractmethod
import requests

class Joke(ABC):
    @abstractmethod
    def get_random_joke(self):
        pass

class A(Joke):
    def get_random_joke(self):
        url = "https://v2.jokeapi.dev/joke/Any"
        response = requests.get(url)
        data = response.json()
        if data["type"] == "single":
            joke = data["joke"]
            return joke 
        else:
            setup = data["setup"]
            delivery = data["delivery"]
            return setup , delivery

class B(Joke):
    def get_random_joke(self):
        url = "https://icanhazdadjoke.com/"
        headers = {"Accept": "application/json"}
        response = requests.get(url, headers=headers)
        data = response.json()
        joke = data["joke"]
        return joke
        
class C(Joke):
    def get_random_joke(self):
        url = "https://icanhazdadjoke.com/"
        headers = {"Accept": "application/json"}
        response = requests.get(url, headers=headers)
        data = response.json()
        joke = data["joke"]
        return joke



a_joke = A()
print("Joke from site A:")
print(a_joke.get_random_joke())

b_joke = B()
print("\nJoke from site B:")
print(b_joke.get_random_joke())

c_joke = C()
print("\nJoke from site C:")
print(c_joke.get_random_joke())
