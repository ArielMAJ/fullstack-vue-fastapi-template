from fastapi import FastAPI


def test_app_is_fastapi_app():
    from api.vercel import app

    assert isinstance(app, FastAPI)
    assert app.title == "fastapi-backend-template"
