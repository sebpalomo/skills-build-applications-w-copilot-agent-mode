from bson import ObjectId
from datetime import timedelta

def get_test_data():
    return {
        "users": [
            {"_id": ObjectId(), "name": "Thor", "email": "thor@asgard.com", "age": 1500},
            {"_id": ObjectId(), "name": "Iron Man", "email": "tony@starkindustries.com", "age": 48},
            {"_id": ObjectId(), "name": "Hulk", "email": "bruce@banner.com", "age": 49},
            {"_id": ObjectId(), "name": "Black Widow", "email": "natasha@shield.com", "age": 35},
            {"_id": ObjectId(), "name": "Captain America", "email": "steve@avengers.com", "age": 105},
        ],
        "teams": [
            {"_id": ObjectId(), "name": "Avengers", "members": []},
        ],
        "activities": [
            {"_id": ObjectId(), "user": None, "type": "Running", "duration": 30 * 60, "calories_burned": 300},
            {"_id": ObjectId(), "user": None, "type": "Cycling", "duration": 60 * 60, "calories_burned": 600},
        ],
        "leaderboard": [
            {"_id": ObjectId(), "user": None, "score": 100},
            {"_id": ObjectId(), "user": None, "score": 90},
        ],
        "workouts": [
            {"_id": ObjectId(), "name": "Morning Yoga", "description": "A relaxing yoga session", "duration": 30},
            {"_id": ObjectId(), "name": "Strength Training", "description": "Building muscle strength", "duration": 45},
        ],
    }