import unittest
from runner_and_tournament import Runner, Tournament


def skip_if_frozen(func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            raise unittest.SkipTest('Тесты в этом кейсе заморожены')
        return func(self, *args, **kwargs)
    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_walk(self):
        runner = Runner('TestWalk')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen
    def test_run(self):
        runner = Runner('TestRun')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner('Runner1')
        runner2 = Runner('Runner2')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

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

    @skip_if_frozen
    def test_race_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        self.all_results[1] = tournament.start()
        self.assertTrue(self.all_results[1][max(self.all_results[1])] == self.nick)

    @skip_if_frozen
    def test_race_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        self.all_results[2] = tournament.start()
        self.assertTrue(self.all_results[2][max(self.all_results[2])] == self.nick)

    @skip_if_frozen
    def test_race_usain_and_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        self.all_results[3] = tournament.start()
        self.assertTrue(self.all_results[3][max(self.all_results[3])] == self.nick)


if __name__ == "__main__":
    unittest.main()
