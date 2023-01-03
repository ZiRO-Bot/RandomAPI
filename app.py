from fastapi import FastAPI

from routers import google, imagemanip

app = FastAPI()
app.include_router(google.router)
app.include_router(imagemanip.router)
