import pydantic

from generated.objects.user import User



class GameHighScore(pydantic.BaseModel):
    """
    This object represents one row of the high scores table for a game.
    :param position: Position in high score table for the game
    :param user: User
    :param score: Score
    """
    
    position: typing.Optional[int] = None
    user: typing.Optional["User"] = None
    score: typing.Optional[int] = None
    
    

