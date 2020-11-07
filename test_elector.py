import unittest
from elector import Elector
from party import Party
from electionresult import ElectionResult

parties = [
    Party("Cons", 776370, [
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
    Party("Green", 173351, [
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
    Party("Lab", 301398, [
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
    Party("Lib Dems", 338342, [
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
    Party("UKIP", 431111, [
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
    Party("BNP", 64877, [
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
    Party("SCP", 42861, [
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
    Party("EngDem", 29126, [
        "Steven Uncles",
        "Robert Sulley",
        "Courtney Williams",
        "Richard Sutton",
        "Jacqueline Brookman",
        "David Uncles",
        "Louise Uncles"
    ]),
    Party("Respect", 13426, [
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
    Party("Peace", 12572, [
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
    Party("Christian Peoples", 11733, [
        "David John Bamber",
        "David Campanale",
        "Gladstone Macaulay"
    ]),
    Party("Pro Life Alliance", 6579, [
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
    Party("Independent", 5671, [
        "Philip Rhodes"
    ])
]

class TestElector(unittest.TestCase):
    
    def test_run_election(self):
        self.maxDiff = None

        elector = Elector(10)
        actual = elector.run_election(parties)
        expected = [
            ElectionResult("Cons", 4, [
                "Daniel Hannan",
                "Nirj Deva",
                "James Elles",
                "Richard Ashworth"
            ]),
            ElectionResult("Lib Dems", 2, [
                "Chris Huhne",
                "Baroness Nicholson of Winterbourne",
            ]),
            ElectionResult("UKIP", 2, ["Nigel Farage", "Ashley Mote"]),
            ElectionResult("Lab", 1, ["Peter Skinner"]),
            ElectionResult("Green", 1, ["Caroline Lucas"]),
            ElectionResult("BNP", 0, []),
            ElectionResult("SCP", 0, []),
            ElectionResult("EngDem", 0, []),
            ElectionResult("Respect", 0, []),
            ElectionResult("Peace", 0, []),
            ElectionResult("Christian Peoples", 0, []),
            ElectionResult("Pro Life Alliance", 0, []),
            ElectionResult("Independent", 0, [])
        ]

        for idx,val in enumerate(actual):
            self.assertEqual(val.party_name, expected[idx].party_name)
            self.assertEqual(val.seats_won, expected[idx].seats_won)
            self.assertSequenceEqual(val.candidates_elected, expected[idx].candidates_elected)

if __name__ == "__main__":
    unittest.main()