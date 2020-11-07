from party import Party
from electionresult import ElectionResult

class Elector:
    def __init__(self, available_seats):
        self.available_seats = available_seats

    def run_election(self, parties):
        for i in range(self.available_seats):
            parties.sort(key=lambda x: x.quotient, reverse=True)
            parties[0].allocate_seat()

        results = []
        for x in parties:
            results.append(ElectionResult(x.name, x.seats_won, x.candidates_elected))

        results.sort(key=lambda x: x.seats_won, reverse=True)
        return results