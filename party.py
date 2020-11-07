class Party:

    def __init__(self, name, votes_won, candidates):
        self.name = name
        self.votes_won = votes_won
        self.candidates = candidates
        
        self.quotient = votes_won
        self.seats_won = 0
        self.candidates_elected = []
    
    def allocate_seat(self):
        self.candidates_elected.append(self.candidates[self.seats_won])
        self.seats_won += 1
        self.quotient = self.votes_won / (self.seats_won + 1)