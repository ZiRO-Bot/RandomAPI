from fastapi import FastAPI

from routers import google, imagemanip

PREFIX = "/api/v1"

app = FastAPI()
app.include_router(google.router, prefix=PREFIX)
app.include_router(imagemanip.router, prefix=f"{PREFIX}/image")
