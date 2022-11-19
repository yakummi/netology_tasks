import requests

class SuperHero():
    _superhero = []
    _intelligence = []
    def __init__(self, url: str, heroes=[]):
        self.url = url
        self.heroes = heroes

    def response(self):
        response = requests.get(self.url).json()
        for element in response:
            if element['name'] in self.heroes:
                self._superhero.append(element['name'])
                self._intelligence.append(element['powerstats']['intelligence'])
        return max(dict(zip(self._superhero, self._intelligence)))

hero = SuperHero('https://akabab.github.io/superhero-api/api/all.json', ['Hulk', 'Captain America', 'Thanos'])

