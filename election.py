class Party:

    def __init__(self, name, num_votes, candidates):
        self.name = name
        self.votes_won = num_votes
        self.candidates = candidates
        self.quotient = num_votes
        self.candidates_elected = []
        self.seats_won = 0
    
    def allocate_seat(self):
        self.candidates_elected.append(self.candidates[self.seats_won])
        self.seats_won += 1
        self.quotient = self.votes_won / (self.seats_won + 1)

num_seats = 10
parties = [
    Party('Cons', 776370, [
        "Daniel Hannan",
		"Nirj Deva",
        "James Elles",
        "Richard Ashworth",
        "Roy Perry",
        "Therese Coffey",
        "David Logan",
        "Ferris Cowper",
        "Richard Robinson"
    ]),
    Party('Green', 173351, [
        "Caroline Lucas",
        "Mike Woodin",
        "Miriam Kennet",
        "Keith Taylor",
        "Alan Francis",
        "Xanthe Bevis",
        "Hazel Dawe",
        "Derek Wall",
        "nthony Cooper",
        "Michael Stimson"
    ]),
    Party('Lab', 301398, [
        "Peter Skinner",
        "Mark Watts",
        "Ann Davison",
        "Simon Burgess",
        "Janet Sully",
        "Mark Muller",
        "Josephine Wood",
        "Raj Chandarana",
        "Gillian Roles",
        "David Menon"
    ]),
    Party('Lib Dems', 338342, [
        "Chris Huhne",
        "Baroness Nicholson of Winterbourne",
        "Sharon Bowles",
        "Catherine Bearder",
        "James Walsh",
        "Ann Lee",
        "John Vincent",
        "John Ford",
        "Charles Fraser-Fleming",
        "James Barnard"
    ]),
    Party('UKIP', 431111, [
        "Nigel Farage",
        "Ashley Mote",
        "David Lott",
        "Craig Mackinlay",
        "Timothy Cross",
        "Petrina Holdsworth",
        "David Abbott",
        "Stephen Harris",
        "Michael Wigley",
        "Lisa Hawkins"
    ]),
    Party('BNP', 64877, [
        "Brian Galloway",
        "Julie Russell",
        "Timothy Rait",
        "Peter Lane",
        "Roger Robertson",
        "Julian Crewe",
        "Adam Champneys",
        "Ian Johnson",
        "Dennis Whiting",
        "Vernon Atkinson"
    ]),
    Party('SCP', 42861, [
        "Grahame Leon-Smith",
        "David Gray",
        "Patrick Eston",
        "Rona Brown",
        "Paresh Kotecha",
        "Larry Kreeger",
        "Michael Devine",
        "Terry Patinson",
        "Ian Murdoch",
        "Alfred Egleton"
    ]),
    Party('EngDem', 29126, [
        "Steven Uncles",
        "Robert Sulley",
        "Courtney Williams",
        "Richard Sutton",
        "Jacqueline Brookman",
        "David Uncles",
        "Louise Uncles"
    ]),
    Party('Respect', 13426, [
        "Patrick O'Keeffe",
        "Ingrid Dodd",
        "Muriel Hirsch",
        "Ajaz Khan",
        "Sally Watkins",
        "Jonathan Molyneux",
        "Norman Thomas",
        "Ella Noyes",
        "Bunny La Roche",
        "Angelina Rai"
    ]),
    Party('Peace', 12572, [
        "John Morris",
        "Caroline O'Reilly",
        "Geoffrey Pay",
        "Rachel Hancock",
        "James Duggan",
        "Kate Hebden",
        "Cyril Bolam",
        "Carol Morris",
        "Anne Brewer"
    ]),
    Party('Christian Peoples', 11733, [
        "David John Bamber",
        "David Campanale",
        "Gladstone Macaulay"
    ]),
    Party('Pro Life Alliance', 6579, [
        "Dominica Roberts",
        "Gillian Duval",
        "Josephine Quintavalle",
        "Penelope Orford",
        "Mark Carroll",
        "Rebecca Ng",
        "John Dixon",
        "Francis O'Brien",
        "Yvonne Windsor",
        "Carl St John"
    ]),
    Party('Independent', 5671, [
        "Philip Rhodes"
    ]),
]

for i in range(num_seats):
    parties.sort(key=lambda x: x.quotient, reverse=True)
    parties[0].allocate_seat()

for x in parties:
    print(x.name)
    print(x.seats_won)
    print(x.candidates_elected)
    print(x.quotient)