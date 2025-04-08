from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout

class UserAPITestCase(APITestCase):
    def test_create_user(self):
        data = {"name": "John Doe", "email": "john@example.com", "age": 30}
        response = self.client.post("/api/users/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TeamAPITestCase(APITestCase):
    def test_create_team(self):
        data = {"name": "Team A", "members": []}
        response = self.client.post("/api/teams/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityAPITestCase(APITestCase):
    def test_create_activity(self):
        user = User.objects.create(name="John Doe", email="john@example.com", age=30)
        data = {"user": user.id, "type": "Running", "duration": 60, "calories_burned": 500}
        response = self.client.post("/api/activities/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LeaderboardAPITestCase(APITestCase):
    def test_create_leaderboard_entry(self):
        user = User.objects.create(name="John Doe", email="john@example.com", age=30)
        data = {"user": user.id, "score": 100}
        response = self.client.post("/api/leaderboard/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WorkoutAPITestCase(APITestCase):
    def test_create_workout(self):
        data = {"name": "Morning Yoga", "description": "A relaxing yoga session", "duration": 30}
        response = self.client.post("/api/workouts/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)