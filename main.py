from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.twitter_modoki.v1 import twitterModokiRouter as v1
from api.twitter_modoki.v2 import twitterModokiRouter as v2

app = FastAPI()

origins = [
   "*"
   # "http://localhost",
   # "http://localhost:3000",
   # "https://n2freevas-playsite-idy82kfmc-n2studio.vercel.app"
]

app.add_middleware(
   CORSMiddleware,
   allow_origins = origins,
   allow_credentials = True,
   allow_methods = ["*"],
   allow_headers=["*"],
)

app.include_router(v1, prefix="/twitter-modoki", tags=['TwitterModoki'])
app.include_router(v2, prefix="/twitter-modoki/v2", tags=['TwitterModoki2'])

@app.get('/')
async def health():
   return {"health": "OK"}
