"""
Flat-file static build for Capacitor APK.
Uses relative paths and flat .html files (lesson-1.html, quiz-1.html)
so navigation works with file:// protocol in Android WebView.
"""

import os
import re
import shutil

from app import app

DIST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")


def render_route(client, route, filename):
    """Render a route, following any redirects."""
    resp = client.get(route)
    if resp.status_code == 302:
        location = resp.headers.get("Location", "/")
        resp = client.get(location)
    if resp.status_code == 200:
        filepath = os.path.join(DIST, filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        content = resp.data.decode("utf-8", errors="replace")

        # Convert absolute paths to relative paths for file:// compatibility
        # /static/... -> static/...
        # /lesson/X -> lesson-X.html
        # /quiz/X -> quiz-X.html
        # / -> index.html
        content = content.replace('href="/static/', 'href="static/')
        content = content.replace('src="/static/', 'src="static/')
        content = content.replace('href="/"', 'href="index.html"')
        content = content.replace("href='/'", "href='index.html'")
        content = re.sub(r'href="/lesson/(\d+)/?"', r'href="lesson-\1.html"', content)
        content = re.sub(r'href="/quiz/(\d+)/?"', r'href="quiz-\1.html"', content)
        content = re.sub(r"href='/lesson/(\d+)/?'", r"href='lesson-\1.html'", content)
        content = re.sub(r"href='/quiz/(\d+)/?'", r"href='quiz-\1.html'", content)
        # Core pages
        for page in [
            "daily",
            "weekly",
            "practice",
            "progress",
            "badges",
            "onboarding",
            "privacy",
            "terms",
        ]:
            content = content.replace(f'href="/{page}"', f'href="{page}.html"')
            content = content.replace(f"href='/{page}'", f"href='{page}.html'")
        # Redirect URLs in JS (window.location.href)
        content = re.sub(
            r"window\.location\.href\s*=\s*'/lesson/(\d+)/?'",
            r"window.location.href='lesson-\1.html'",
            content,
        )
        content = re.sub(
            r"window\.location\.href\s*=\s*'/'",
            r"window.location.href='index.html'",
            content,
        )
        content = re.sub(
            r'window\.location\.href\s*=\s*"/lesson/(\d+)/?"',
            r'window.location.href="lesson-\1.html"',
            content,
        )

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False


def freeze():
    """Generate flat-file static HTML for Capacitor."""
    if os.path.exists(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST, exist_ok=True)

    # Copy static assets
    static_src = os.path.join(os.path.dirname(__file__), "static")
    static_dst = os.path.join(DIST, "static")
    if os.path.exists(static_src):
        shutil.copytree(static_src, static_dst, dirs_exist_ok=True)

    client = app.test_client()

    # Reset progress so home redirects to onboarding for APK entry point
    example = os.path.join(os.path.dirname(__file__), "progress.example.json")
    if os.path.exists(example):
        import json

        with open(example) as f:
            default_progress = json.load(f)
        # Temporarily write default progress so home redirects to onboarding
        progress_path = os.path.join(os.path.dirname(__file__), "progress.json")
        backup = None
        if os.path.exists(progress_path):
            with open(progress_path) as f:
                backup = f.read()
        with open(progress_path, "w") as f:
            json.dump(default_progress, f)

    # index.html — render the onboarding page (APK entry point)
    render_route(client, "/", "index.html")

    # Restore progress if we backed it up
    if backup:
        with open(progress_path, "w") as f:
            f.write(backup)

    # Core pages
    for page in [
        "daily",
        "weekly",
        "practice",
        "progress",
        "badges",
        "onboarding",
        "privacy",
        "terms",
    ]:
        render_route(client, f"/{page}", f"{page}.html")

    # API endpoints as flat JSON files
    for api in ["progress", "platforms", "lessons"]:
        resp = client.get(f"/api/{api}")
        if resp.status_code == 200:
            with open(os.path.join(DIST, f"api-{api}.json"), "wb") as f:
                f.write(resp.data)

    # All lesson and quiz pages as flat files
    from app import get_lessons

    lessons = get_lessons()
    for l in lessons:
        lid = l["id"]
        render_route(client, f"/lesson/{lid}", f"lesson-{lid}.html")
        render_route(client, f"/quiz/{lid}", f"quiz-{lid}.html")

    # Copy progress.example.json
    example = os.path.join(os.path.dirname(__file__), "progress.example.json")
    if os.path.exists(example):
        shutil.copy(example, os.path.join(DIST, "progress.json"))

    print(f"Flat build complete -> {DIST}")
    print(f"Files: index.html + {len(lessons)} lessons + {len(lessons)} quizzes")


if __name__ == "__main__":
    freeze()
