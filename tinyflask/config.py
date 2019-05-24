from os import getenv

__all__ = ["app_globals"]

app_globals = {
    "name": "A tiny flask",
    "author": "One Awesome Dev",
    "version": "0.0.1",
    "host": getenv("HOST", "127.0.0.1"),
    "port": getenv("PORT", "5000"),
    "url": getenv("URL", "http://127.0.0.1:5000"),
}
