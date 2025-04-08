from bson import ObjectId

# Define users first
users = [
    {"_id": ObjectId(), "name": "John Doe", "email": "john@example.com", "age": 30},
    {"_id": ObjectId(), "name": "Jane Smith", "email": "jane@example.com", "age": 25},
    {"_id": ObjectId(), "name": "Alice Johnson", "email": "alice@example.com", "age": 28},
]

# Define test data
test_data = {
    "users": users,
    "teams": [
        {"_id": ObjectId(), "name": "Team A", "members": []},
        {"_id": ObjectId(), "name": "Team B", "members": []},
    ],
    "activities": [
        {"_id": ObjectId(), "user": users[0], "type": "Running", "duration": 60, "calories_burned": 500},
        {"_id": ObjectId(), "user": users[1], "type": "Cycling", "duration": 45, "calories_burned": 400},
    ],
    "leaderboard": [
        {"_id": ObjectId(), "user": users[0], "score": 100},
        {"_id": ObjectId(), "user": users[1], "score": 90},
    ],
    "workouts": [
        {"_id": ObjectId(), "name": "Morning Yoga", "description": "A relaxing yoga session", "duration": 30},
        {"_id": ObjectId(), "name": "Strength Training", "description": "Building muscle strength", "duration": 45},
    ]
}