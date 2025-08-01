def handle_answer(player, question, user_answer):
    if not question:
        return {"success": False, "message": "No question defined."}
    correct = user_answer == question['answer']
    if correct:
        player.gain_xp(10)
        return {"success": True, "message": "Correct! You gain XP."}
    else:
        player.lose_hp(10)
        return {"success": False, "message": "Incorrect. You lose HP."}
