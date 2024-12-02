class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1
    
    def __score_to_string(self, score: int) -> str:
        match score:
            case 0: return "Love"
            case 1: return "Fifteen"
            case 2: return "Thirty"
            case 3: return "Forty"
            case _: return "Deuce"
        
                

    def get_score(self) -> str:
        score: str = ""
        player1str: str = self.__score_to_string(self.player1_score)
        player2str: str = self.__score_to_string(self.player2_score)
        delta: int = abs(self.player1_score - self.player2_score)

        lowestScore: int = min(self.player1_score, self.player2_score)
        highestScore: int = max(self.player1_score, self.player2_score)

        if(self.player1_score == self.player2_score):
            if(player1str == "Deuce" or player1str == "Forty"):
                score = "Deuce"
            else:
                score = f"{player1str}-All"
            
        elif(highestScore < 4):
            score = f"{player1str}-{player2str}"

        elif(lowestScore > 2 and delta < 2):
            if(highestScore == self.player1_score):
                score = "Advantage player1"
            else:
                score = "Advantage player2"
        
        elif(lowestScore < 3 and highestScore > 3):
            if(highestScore == self.player1_score):
                score = "Win for player1"
            else:
                score = "Win for player2"
        
        
                
        elif(lowestScore > 2 and delta >= 2):
            if(highestScore == self.player1_score):
                score = "Win for player1"
            else:
                score = "Win for player2"


    
        return score