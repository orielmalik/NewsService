import requests
import json

from model.Content import CONTENT

base_url = "http://localhost:5000/content"


def test_post_method():
    content_instance = CONTENT("alma","ds")
    payload = content_instance.to_dict()

    response = requests.post(
        base_url,
        headers={"Content-Type": "application/json"},
        json=payload
    )
    assert response.status_code ==200, "Response status code is not 200"
    assert response.json() == payload, f"Unexpected response: {response.json()}"


def test_delete_method():
    response = requests.delete(f"{base_url}?id={all}")
    print(response.json())
    assert response.status_code == 200, "Response status code is not 200"

