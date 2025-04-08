from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout
from django.test import TestCase

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

class UserModelTest(TestCase):
    def setUp(self):
        User.objects.create(username="testuser", email="testuser@example.com", password="password123")

    def test_user_creation(self):
        user = User.objects.get(username="testuser")
        self.assertEqual(user.email, "testuser@example.com")

class TeamModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username="teamuser", email="teamuser@example.com", password="password123")
        Team.objects.create(name="Test Team", members=[user])

    def test_team_creation(self):
        team = Team.objects.get(name="Test Team")
        self.assertEqual(team.name, "Test Team")

class ActivityModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username="activityuser", email="activityuser@example.com", password="password123")
        Activity.objects.create(user=user, activity_type="Running", duration="01:00:00")

    def test_activity_creation(self):
        activity = Activity.objects.get(activity_type="Running")
        self.assertEqual(activity.duration, "01:00:00")

class LeaderboardModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username="leaderuser", email="leaderuser@example.com", password="password123")
        Leaderboard.objects.create(user=user, score=100)

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.get(score=100)
        self.assertEqual(leaderboard.user.username, "leaderuser")

class WorkoutModelTest(TestCase):
    def setUp(self):
        Workout.objects.create(name="Test Workout", description="A test workout description")

    def test_workout_creation(self):
        workout = Workout.objects.get(name="Test Workout")
        self.assertEqual(workout.description, "A test workout description")