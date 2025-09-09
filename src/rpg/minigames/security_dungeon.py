"""
A simple Security Dungeon minigame. Users must supply a JSON string representing an IAM
policy. The evaluator checks if the policy follows least‑privilege best practices (only
allows specific actions on specific resources).
"""
import json

def evaluate_security_dungeon(policy_str: str) -> dict:
    try:
        policy = json.loads(policy_str)
    except json.JSONDecodeError:
        return {"success": False, "message": "Invalid JSON"}

    # Check for overly permissive actions or resources
    statements = policy.get('Statement', [])
    too_permissive = []
    for stmt in statements:
        if stmt.get('Effect') != 'Allow':
            continue
        actions = stmt.get('Action')
        resources = stmt.get('Resource')
        if actions == '*' or actions == ['*']:
            too_permissive.append('Action *')
        if resources == '*' or resources == ['*']:
            too_permissive.append('Resource *')
    if too_permissive:
        return {
            "success": False,
            "message": "Your policy is too permissive: {}. Refine the actions and resources.".format(', '.join(too_permissive))
        }
    return {"success": True, "message": "Great job! Your policy follows least‑privilege principles."}
