from techzapi.api import TechZApi

GogoApi = TechZApi.Gogo("Your Api Key")

print(GogoApi.latest())
