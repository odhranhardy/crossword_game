from src.crossword.game.logic import validate_answer

def test_validate_answer():
    assert validate_answer("TEST", "TEST") == True
    assert validate_answer("TEST", "WRONG") == False