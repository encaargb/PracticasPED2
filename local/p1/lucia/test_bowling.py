import unittest                     # Importamos el framework de testing de Python
from bowling import BowlingGame    # Queremos usar la clase que aún no existe (esto provocará el error)

class BowlingGameTest(unittest.TestCase):  # Creamos una clase de test que hereda de unittest.TestCase
    def test_score_all_zeros(self):        # Este es nuestro primer test: partida con 0 bolos
        game = BowlingGame()               # Creamos una partida de bolos
        rolls = [0] * 20                   # Simulamos 20 tiros, todos 0 (una partida entera)
        self.assertEqual(game.score(rolls), 0)  # Esperamos que el resultado sea 0

    def test_score_all_ones(self):
        game = BowlingGame()
        rolls = [1] * 20 # Simulamos 20 tiros, todos 1
        self.assertEqual(game.score(rolls), 20) # Esperamos que el resultado sea 20 (1 por tiro, 20 tiros)

    def test_one_spare(self): # Test de spare
        game = BowlingGame()
        # Simulamos una partida con:
        # Ronda 1: 5 + 5 → spare → bonus = siguiente tiro (3)
        # Ronda 2: 3 + 0
        # Total esperado: 10 + 3 (bonus) + 3 = 16
        rolls = [5, 5, 3] + [0] * 17  # 20 tiros en total
        self.assertEqual(game.score(rolls), 16)
        
    def test_one_strike(self):
        game = BowlingGame()
        # Strike: primer tiro es 10 → bonus = 3 + 4
        rolls = [10, 3, 4] + [0] * 17
        self.assertEqual(game.score(rolls), 24) 
        '''Ronda 1: strike → 10 + 3 + 4 = 17
        Ronda 2: 3 + 4 = 7
        Total: 17 + 7 = 24'''

    def test_perfect_game(self):
        game = BowlingGame()
        # 12 strikes: 10 normales + 2 bonus en la última ronda
        rolls = [10] * 12
        self.assertEqual(game.score(rolls), 300)
        '''Ronda 1: strike → 10 + 10 + 10 = 30
        Ronda 2: strike → 10 + 10 + 10 = 30
        Ronda 3: strike → 10 + 10 + 10 = 30
        Ronda 4: strike → 10 + 10 + 10 = 30
        Ronda 5: strike → 10 + 10 + 10 = 30
        Ronda 6: strike → 10 + 10 + 10 = 30
        Ronda 7: strike → 10 + 10 + 10 = 30
        Ronda 8: strike → 10 + 10 + 10 = 30
        Ronda 9: strike → 10 + 10 + 10 = 30
        Ronda 10: strike → 10 + 10 + 10 = 30
        Total: 30 * 10 = 300'''
    
    def test_spare_followed_by_strike(self): # Test de spare seguido de strike
        game = BowlingGame()
        rolls = [5, 5, 10, 3, 4] + [0] * 14
        self.assertEqual(game.score(rolls), 44)
        '''Ronda 1: spare → 5 + 5 = 10 + 10 (strike) + 3 (bonus) = 23
        Ronda 2: strike → 10 + 3 + 4 = 17
        Ronda 3: 3 + 4 = 7
        Total: 23 + 17 + 7 = 47'''

    def test_strike_followed_by_spare(self): # Test de strike seguido de spare
        game = BowlingGame()
        rolls = [10, 5, 5, 3] + [0] * 16
        self.assertEqual(game.score(rolls), 36)
        '''Ronda 1: strike → 10 + 5 + 5 = 20
        Ronda 2: spare → 5 + 5 = 10 + 3 (bonus) = 13
        Ronda 3: 3 + 0 = 3
        Total: 20 + 13 + 3 = 36'''

    def test_spare_in_last_frame(self):
        game = BowlingGame()
        rolls = [0] * 18 + [5, 5, 7]
        self.assertEqual(game.score(rolls), 17)
        '''Ronda 1: 0 + 0 = 0
        Ronda 2: 0 + 0 = 0
        Ronda 3: 0 + 0 = 0
        Ronda 4: 0 + 0 = 0
        Ronda 5: 0 + 0 = 0
        Ronda 6: 0 + 0 = 0
        Ronda 7: 0 + 0 = 0  
        Ronda 8: 0 + 0 = 0
        Ronda 9: 0 + 0 = 0
        Ronda 10: spare → 5 + 5 = 10 + 7 (bonus) = 17
        Total: 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 17 = 17'''


# Esto permite ejecutar el test si lanzamos este archivo directamente
if __name__ == '__main__':
    unittest.main()
