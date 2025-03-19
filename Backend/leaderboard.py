from database import get_db

def get_leaderboard():
    db = get_db()
    top_users = db.leaderboard.find_one({}, {"_id": 0, "top_users": 1})
    return top_users if top_users else {"top_users": []}