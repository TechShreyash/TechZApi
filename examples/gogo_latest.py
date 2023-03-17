from techzapi.api import TechZApi

GogoApi = TechZApi.Gogo("DVZTAR")

print(GogoApi.latest())
