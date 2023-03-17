## TechZApi

Python wrapper for the TechZApi

- Base Url : api.techzbots.live
- Documentation : [Click Here](https://api.techzbots.live/docs)
- Updates Channel : [TechZBots](https://telegram.me/TechZBots)
- Support Group : [TechZBots Support](https://telegram.me/TechZBots_Support)

### Requirements

- API_KEY : Create your own key, from [here](https://telegram.me/TechZApiBot)
- TechZApi Credits : You will get 10000 Free credits, Need More contact us at [TechZBots Support](https://telegram.me/TechZBots_Support)

### Installation

- Install latest version using
```
$ pip install -U techzapi
```

- Use the above command to update also

### Usage

To get latest releases from gogo anime

```
from techzapi.api import TechZApi

GogoApi = TechZApi.Gogo("Your Api Key")

print(GogoApi.latest())
```