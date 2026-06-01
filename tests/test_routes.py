"""Route smoke tests — shift-left testing protocol.

Tests every route without needing a live server (uses Flask test client).
Run: python -m pytest tests/test_routes.py -v
"""

import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# ── Core Pages ──────────────────────────────────────────────────────────────

class TestCoreRoutes:
    def test_home_returns_200(self, client):
        resp = client.get("/")
        assert resp.status_code == 200
        assert b"Cloud Orbit" in resp.data or b"lesson-circle" in resp.data

    def test_aws_lesson_returns_200(self, client):
        resp = client.get("/lesson/1")
        assert resp.status_code == 200

    def test_k8s_lesson_returns_200(self, client):
        resp = client.get("/lesson/101")
        assert resp.status_code == 200

    def test_docker_lesson_returns_200(self, client):
        resp = client.get("/lesson/201")
        assert resp.status_code == 200

    def test_invalid_lesson_returns_404(self, client):
        resp = client.get("/lesson/999")
        assert resp.status_code == 404

    def test_quiz_get_returns_200(self, client):
        resp = client.get("/quiz/1")
        assert resp.status_code == 200
        assert b"shield" in resp.data or b"option" in resp.data.lower()

    def test_quiz_post_returns_200_or_302(self, client):
        resp = client.post("/quiz/1", data={"answer": "0"})
        # 200 = normal result, 302 = milestone reward redirect (every 15 questions)
        assert resp.status_code in (200, 302)

    def test_progress_dashboard_returns_200(self, client):
        resp = client.get("/progress")
        assert resp.status_code == 200

    def test_badges_returns_200(self, client):
        resp = client.get("/badges")
        assert resp.status_code == 200

    def test_reward_screen_returns_200(self, client):
        resp = client.get("/reward/15")
        assert resp.status_code == 200


# ── API Endpoints ───────────────────────────────────────────────────────────

class TestAPIEndpoints:
    def test_api_progress_returns_200(self, client):
        resp = client.get("/api/progress")
        assert resp.status_code == 200

    def test_api_progress_returns_json(self, client):
        resp = client.get("/api/progress")
        assert resp.is_json
        data = resp.get_json()
        assert "energy" in data or "xp" in data

    def test_api_platforms_returns_200(self, client):
        resp = client.get("/api/platforms")
        assert resp.status_code == 200
        assert resp.is_json

    def test_api_lessons_returns_200(self, client):
        resp = client.get("/api/lessons")
        assert resp.status_code == 200
        assert resp.is_json

    def test_api_lesson_by_id(self, client):
        resp = client.get("/api/lesson/1")
        assert resp.status_code == 200
        assert resp.is_json

    def test_api_use_potion(self, client):
        resp = client.post("/api/use-potion")
        assert resp.status_code in (200, 401, 415)  # 415 if no JSON content-type

    def test_api_reward(self, client):
        resp = client.post("/api/reward/15")
        assert resp.status_code in (200, 302)


# ── Error Pages ─────────────────────────────────────────────────────────────

class TestErrorHandlers:
    def test_404_page_renders_custom_template(self, client):
        resp = client.get("/nonexistent-route-for-testing")
        assert resp.status_code == 404
        assert b"Zap" in resp.data or b"404" in resp.data

    def test_404_lesson_not_found(self, client):
        resp = client.get("/lesson/999")
        assert resp.status_code == 404


# ── Platform Coverage ───────────────────────────────────────────────────────

class TestPlatformCoverage:
    """Every active platform has at least one lesson rendering."""

    def test_aws_lessons_get(self, client):
        for lid in [1, 5, 10, 15, 20]:
            assert client.get("/lesson/%d" % lid).status_code == 200

    def test_k8s_lessons_get(self, client):
        for lid in [101, 105, 110, 115, 120]:
            assert client.get("/lesson/%d" % lid).status_code == 200

    def test_docker_lessons_get(self, client):
        for lid in [201, 205, 210]:
            assert client.get("/lesson/%d" % lid).status_code == 200


# ── Content Quality ─────────────────────────────────────────────────────────

class TestContentQuality:
    """Every active lesson has required fields."""

    def _get_all_lessons(self):
        from app import get_lessons
        return get_lessons()

    def test_all_lessons_have_titles(self):
        for lesson in self._get_all_lessons():
            assert "title" in lesson, "Lesson %s missing title" % lesson.get("id")
            assert len(lesson["title"]) > 0, "Lesson %s has empty title" % lesson.get("id")

    def test_all_lessons_have_questions(self):
        for lesson in self._get_all_lessons():
            assert "question" in lesson, "Lesson %s missing question" % lesson.get("id")
            assert len(lesson["question"]) > 10, "Lesson %s question too short" % lesson.get("id")

    def test_all_lessons_have_options(self):
        for lesson in self._get_all_lessons():
            assert "options" in lesson, "Lesson %s missing options" % lesson.get("id")
            assert len(lesson["options"]) >= 4, "Lesson %s needs 4+ options" % lesson.get("id")

    def test_all_lessons_have_answer(self):
        for lesson in self._get_all_lessons():
            assert "answer" in lesson, "Lesson %s missing answer" % lesson.get("id")
            assert lesson["answer"] in lesson["options"], (
                "Lesson %s answer not in options" % lesson.get("id")
            )

    def test_all_lessons_have_explanation(self):
        for lesson in self._get_all_lessons():
            assert "explanation" in lesson, "Lesson %s missing explanation" % lesson.get("id")
            assert len(lesson["explanation"]) > 10, (
                "Lesson %s explanation too short" % lesson.get("id")
            )
