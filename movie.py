from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Union
import httpx
import humps

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

omdb_api_url = f"http://www.omdbapi.com/?apiKey=9c509cd0"


@app.get("/movie/search")
def search_movies(query: Union[str, None] = None):
    if not query:
        raise HTTPException(status_code=404, detail="Query is required")

    try:
        result = httpx.get(f"{omdb_api_url}&s={query}&page=1").json()

        return humps.camelize(result)
    except Exception as e:
        print("exception: ", e)

        raise HTTPException(status_code=500, detail="Unexpected error")


@app.get("/movie/{imdb_id}")
def get_movie_details(imdb_id: Union[str, None] = None):
    if not imdb_id:
        raise HTTPException(status_code=404, detail="Imdb ID is required")

    try:
        result = httpx.get(f"{omdb_api_url}&i={imdb_id}").json()

        return humps.camelize(result)
    except Exception as e:
        print("exception: ", e)

        raise HTTPException(status_code=500, detail="Unexpected error")
