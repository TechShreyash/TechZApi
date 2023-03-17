import requests


class TechZApi:
    """## TechZApi

    Python wrapper for the TechZApi

    - Base Url : api.techzbots.live
    - Documentation : [Click Here](https://api.techzbots.live/docs)
    - Updates Channel : [TechZBots](https://telegram.me/TechZBots)
    - Support Group : [TechZBots Support](https://telegram.me/TechZBots_Support)
    """

    class Gogo:
        """
        ### GogoAnime Api
        """

        def __init__(self, API_KEY) -> None:
            self.base = "https://api.techzbots.live"
            self.api_key = API_KEY

        def latest(self, page=1):
            """
            Get latest releases from GogoAnime

            - page : Page number (Default : 1)
            """
            data = requests.get(
                f"{self.base}/gogo/latest?api_key={self.api_key}&page={page}"
            ).json()
            return data["results"]

        def anime(self, anime):
            """
            Get anime details from GogoAnime

            - anime : Anime id
            """
            data = requests.get(
                f"{self.base}/gogo/anime?id={anime}&api_key={self.api_key}"
            ).json()
            return data["results"]

        def search(self, query):
            """
            Search anime from GogoAnime

            - query : Anime name
            """
            data = requests.get(
                f"{self.base}/gogo/search/?query={query}&api_key={self.api_key}"
            ).json()
            return data["results"]

        def episode(self, episode, lang="sub"):
            """
            Get episode links from GogoAnime (Download And Stream Links)

            - episode : Episode id, Ex : horimiya-dub-episode-3
            - lang : sub or dub or both
            """
            data = requests.get(
                f"{self.base}/gogo/episode?id={episode}&api_key={self.api_key}&lang={lang}"
            ).json()["results"]
            return data

        def stream(self, url):
            """
            Get m3u8 stream links from GogoAnime

            - url : Episode url"""
            url = str(requests.utils.quote(url))
            data = requests.get(
                f"{self.base}/gogo/stream?url={url}&api_key={self.api_key}"
            ).json()
            return data["results"]

    class MkvCinemas:
        def __init__(self, API_KEY) -> None:
            self.base = "https://api.techzbots.live"
            self.api_key = API_KEY

        def add_task(self, url, max=5):
            """
            Add gdtot scrapping task to queue

            - url : Url of the movie / series
            - max : Max number of links to fetch (Default : 5)
            """
            url = str(requests.utils.quote(url))
            data = requests.get(
                f"{self.base}/mkvcinemas/add_task?api_key={self.api_key}&url={url}&max={max}"
            ).json()
            return data

        def get_task(self, hash):
            """Get status of your task
            If your task is processing then it will return the no of links scrapped
            If completed then it will return the gdtot links with title and size info
            If failed then this will return the error

            - hash : Hash id of task
            """
            data = requests.get(
                f"{self.base}/mkvcinemas/get_task?api_key={self.api_key}&hash={hash}"
            ).json()
            return data
