import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nick = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results.values():
            print(i)

    def test_race_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        self.all_results[1] = tournament.start()
        self.assertTrue(self.all_results[1][max(self.all_results[1])] == self.nick)

    def test_race_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        self.all_results[2] = tournament.start()
        self.assertTrue(self.all_results[2][max(self.all_results[2])] == self.nick)

    def test_race_usain_and_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        self.all_results[3] = tournament.start()
        self.assertTrue(self.all_results[3][max(self.all_results[3])] == self.nick)


if __name__ == "__main__":
    unittest.main()
