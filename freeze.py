"""
Frozen-Flask static build — generates dist/ for Capacitor wrapping.
All routes pre-rendered as static HTML + JSON API endpoints.
"""

import os
import shutil

from app import app

DIST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")

# Routes to freeze (no dynamic parameters)
ROUTES = [
    "/",
    "/daily",
    "/weekly",
    "/practice",
    "/progress",
    "/badges",
    "/onboarding",
    "/privacy",
    "/terms",
    "/api/progress",
    "/api/platforms",
    "/api/lessons",
    # Lesson + quiz pages for all platforms (sampled to keep build fast)
    # Full freeze would iterate all 78 lesson IDs
]


def freeze():
    """Generate static HTML for all routes."""
    if os.path.exists(DIST):
        shutil.rmtree(DIST)

    os.makedirs(DIST, exist_ok=True)
    os.makedirs(os.path.join(DIST, "static"), exist_ok=True)

    # Copy static assets
    static_src = os.path.join(os.path.dirname(__file__), "static")
    static_dst = os.path.join(DIST, "static")
    if os.path.exists(static_src):
        shutil.copytree(static_src, static_dst, dirs_exist_ok=True)

    # Copy templates for reference (not strictly needed for static)
    templates_src = os.path.join(os.path.dirname(__file__), "templates")
    templates_dst = os.path.join(DIST, "templates")
    if not os.path.exists(templates_dst):
        shutil.copytree(templates_src, templates_dst)

    client = app.test_client()

    for route in ROUTES:
        file_path = os.path.join(DIST, route.lstrip("/"), "index.html")
        if route == "/":
            file_path = os.path.join(DIST, "index.html")

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        resp = client.get(route)
        if resp.status_code == 200:
            with open(file_path, "wb") as f:
                f.write(resp.data)
            print(f"  OK  {route} -> {file_path}")
        elif resp.status_code == 302:
            # Redirect — copy the target
            location = resp.headers.get("Location", "/")
            print(f"  302 {route} -> {location}")
            # Write a meta-refresh page
            html = (
                f'<html><meta http-equiv="refresh" content="0;url={location}">'
                f"</html>"
            )
            with open(file_path, "w") as f:
                f.write(html)
        else:
            print(f"  {resp.status_code} {route}")

    # Freeze lesson pages for all 78 lessons
    from app import get_lessons

    lessons = get_lessons()
    for l in lessons:
        lid = l["id"]
        for route in [f"/lesson/{lid}", f"/quiz/{lid}"]:
            resp = client.get(route)
            if resp.status_code == 200:
                file_path = os.path.join(DIST, route.lstrip("/"), "index.html")
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                with open(file_path, "wb") as f:
                    f.write(resp.data)
        print(f"  OK  lesson/{lid} + quiz/{lid}")

    # Copy progress.example.json as initial state
    example = os.path.join(os.path.dirname(__file__), "progress.example.json")
    if os.path.exists(example):
        shutil.copy(example, os.path.join(DIST, "progress.json"))

    print(f"\nStatic build complete -> {DIST}")
    print(f"Lessons frozen: {len(lessons)}")


if __name__ == "__main__":
    freeze()
