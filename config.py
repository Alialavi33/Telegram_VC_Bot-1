HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ

    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["14466322"])
    API_HASH = environ["7a8af273b6f112a2e218d2e8eb431580"]
    SESSION_STRING = environ[
        "BAC-RMMOgyFHmTPUHx5PaV4yLrI3oN9MpvUkhKB8QrsmreUWvfQsfi2Xvkj9w-10FzU5NDXvtbo35ch-pkAfTDp0Jo7oKhJNQIju2WBI87uiNFqwmtS9_GahvDpu83wYMiQnVQPrNxzZsanDr8duMV3U52v8y0EWCX3k-JX3ekDKxvRoOm0L9v8STvZgym8AiSUjzio1dvvunNXswUHXbJU1rTDjFhVbCs9lDdvzyfZia01RwHrHa4pJfsKeVkX1BduRPfxlNrwdXONzFlWFMKMEQdKwp_Z56nls6hWjBd6hwLrUyttlhyUiAqDOmIeXScocnBNvRtvtaRnmaAgdecAAAAATQi0i0A"
    ]  # Check Readme for session
    ARQ_API_KEY = environ["ILZPLM-WQHUAH-ABJZZX-SNLYWW-ARQ"]
    CHAT_ID = int(environ["-1001778673594"])
    DEFAULT_SERVICE = environ.get("DEFAULT_SERVICE") or "youtube"
    BITRATE = int(environ["BITRATE"])

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 14371
    API_HASH = "e46b6c854d2bf58a0"
    ARQ_API_KEY = "Get this from @ARQRobot"
    CHAT_ID = -100546355432
    DEFAULT_SERVICE = "saavn"  # Must be one of "youtube"/"saavn"
    BITRATE = 512 # Must be 512/320

# don't make changes below this line
ARQ_API = "https://thearq.tech"
