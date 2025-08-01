"""
Adaptive learning engine. Determines the next content based on user performance statistics.
"""

def next_content(user: dict) -> dict:
    # Example user schema: {"stats": {"weak_domains": ["storage"], "last_scores": [80, 60, 100]}}
    stats = user.get('stats', {})
    weak_domains = stats.get('weak_domains', [])
    last_scores = stats.get('last_scores', [])
    domain = weak_domains[0] if weak_domains else 'compute'
    avg_score = sum(last_scores) / len(last_scores) if last_scores else 0
    if avg_score > 80:
        return {"content": f"advanced_{domain}", "level": "advanced"}
    else:
        return {"content": f"remedial_{domain}", "level": "remedial"}
