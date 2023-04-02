from fastapi.testclient import TestClient
from fastapi import status
from movie import app

client = TestClient(app)


def test_search_movies():
    response = client.get("/movie/search", params={"query": "avatar"})

    assert response.status_code == status.HTTP_200_OK

    result = response.json()

    movies = result.get("search", [])

    assert len(movies) > 0


def test_get_movie_details():
    imdb_id = "tt0499549"

    response = client.get(f"/movie/{imdb_id}")

    assert response.status_code == status.HTTP_200_OK

    result = response.json()

    assert response.status_code == status.HTTP_200_OK

    title = result.get("title", "")

    assert title == "Avatar"
