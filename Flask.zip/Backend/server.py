from fastapi import FastAPI
from database import get_db
from spotify import fetch_user_minutes
from leaderboard import get_leaderboard

app = FastAPI()

@app.get("/auth/login")
def login():
    return {"message": "Redirect to Spotify OAuth"}

@app.get("/user/minutes")
def user_minutes():
    return fetch_user_minutes()

@app.post("/leaderboard")
def leaderboard():
    return get_leaderboard()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)