import unittest
from bowling_game import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def roll_many(self, game, n, pins):
        for _ in range(n):
            game.roll(pins)

    def roll_spare(self, game):
        game.roll(5)
        game.roll(5)

    def roll_strike(self, game):
        game.roll(10)

    def test_empty_game_scores_zero(self):
        game = BowlingGame()
        self.assertEqual(game.score(), 0)

    def test_open_frames_sum_points(self):
        game = BowlingGame()
        game.roll(3)
        game.roll(4)
        self.assertEqual(game.score(), 7)

    def test_single_spare_adds_next_roll(self):
        game = BowlingGame()
        self.roll_spare(game)  # 10
        game.roll(3)           # +3 (bonus)
        self.assertEqual(game.score(), 16)

    def test_single_strike_adds_next_two(self):
        game = BowlingGame()
        self.roll_strike(game)  # 10
        game.roll(3)            # +3
        game.roll(4)            # +4
        self.assertEqual(game.score(), 24)

    def test_score_accumulates_all_frames(self):
        game = BowlingGame()
        game.roll(3)
        game.roll(4)          # 7
        self.roll_spare(game)  # 10 + 3
        game.roll(3)          # 3
        game.roll(2)          # 2
        self.assertEqual(game.score(), 25)

    def test_tenth_frame_with_bonus_rolls(self):
        game = BowlingGame()
        self.roll_many(game, 18, 0)
        self.roll_spare(game)
        game.roll(7)
        self.assertEqual(game.score(), 17)

    def test_tenth_frame_without_bonus(self):
        game = BowlingGame()
        self.roll_many(game, 18, 0)
        game.roll(3)
        game.roll(4)
        self.assertEqual(game.score(), 7)

    def test_perfect_game_scores_300(self):
        game = BowlingGame()
        self.roll_many(game, 12, 10)
        self.assertEqual(game.score(), 300)

if __name__ == '__main__':
    unittest.main()