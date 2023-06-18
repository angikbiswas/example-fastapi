from fastapi import FastAPI
from . import model
from .database import engine
from .routers import user,post,dental,auth,vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware


#print(settings.databae_username)
model.Base.metadata.create_all(bind=engine)
app= FastAPI()
origins=["https://www.google.com", "https://www.youtube.com"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],


)

app.include_router(user.router)
app.include_router(post.router)
app.include_router(dental.router) 
app.include_router(auth.router)
app.include_router(vote.router)           


@app.get("/")
def root():
    return{"message":"wellcome to my api!!"}








    




   

