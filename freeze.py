"""
Frozen-Flask static build — generates dist/ for Capacitor wrapping.
Resolves redirects and produces complete HTML for offline use.
"""
import os
import shutil

from app import app

DIST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")


def render_route(client, route, file_path):
    """Render a route, following any redirects to get actual content."""
    resp = client.get(route)

    # Follow redirects — render the target page content, not a meta-refresh
    if resp.status_code == 302:
        location = resp.headers.get("Location", "/")
        # Follow the redirect internally to get actual content
        resp = client.get(location)

    if resp.status_code == 200:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as f:
            f.write(resp.data)
        print(f"  OK  {route} -> {file_path} ({len(resp.data)}B)")
        return True
    else:
        print(f"  {resp.status_code} {route}")
        return False


def freeze():
    """Generate static HTML for all routes."""
    if os.path.exists(DIST):
        shutil.rmtree(DIST)

    os.makedirs(DIST, exist_ok=True)

    # Copy static assets
    static_src = os.path.join(os.path.dirname(__file__), "static")
    static_dst = os.path.join(DIST, "static")
    if os.path.exists(static_src):
        shutil.copytree(static_src, static_dst, dirs_exist_ok=True)

    client = app.test_client()

    # Core pages
    core_routes = [
        ("/", "index.html"),
        ("/daily", "daily/index.html"),
        ("/weekly", "weekly/index.html"),
        ("/practice", "practice/index.html"),
        ("/progress", "progress/index.html"),
        ("/badges", "badges/index.html"),
        ("/onboarding", "onboarding/index.html"),
        ("/privacy", "privacy/index.html"),
        ("/terms", "terms/index.html"),
    ]
    for route, filename in core_routes:
        file_path = os.path.join(DIST, filename)
        render_route(client, route, file_path)

    # API endpoints as JSON
    api_routes = [
        ("/api/progress", "api/progress/index.html"),
        ("/api/platforms", "api/platforms/index.html"),
        ("/api/lessons", "api/lessons/index.html"),
    ]
    for route, filename in api_routes:
        file_path = os.path.join(DIST, filename)
        render_route(client, route, file_path)

    # All lesson and quiz pages
    from app import get_lessons

    lessons = get_lessons()
    for l in lessons:
        lid = l["id"]
        for route in [f"/lesson/{lid}", f"/quiz/{lid}"]:
            # Create directory index (served when URL ends with /)
            file_path = os.path.join(DIST, route.lstrip("/"), "index.html")
            render_route(client, route, file_path)
            # Also create .html sibling (Capacitor needs this for no-slash URLs)
            sibling = os.path.join(DIST, route.lstrip("/") + ".html")
            if os.path.exists(file_path):
                shutil.copy(file_path, sibling)

    # Copy progress.example.json as initial state
    example = os.path.join(os.path.dirname(__file__), "progress.example.json")
    if os.path.exists(example):
        shutil.copy(example, os.path.join(DIST, "progress.json"))

    print(f"\nStatic build complete -> {DIST}")
    print(f"Lessons frozen: {len(lessons)}")


if __name__ == "__main__":
    freeze()
