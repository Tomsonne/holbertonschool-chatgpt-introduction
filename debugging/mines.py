#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        print('   ' + ' '.join(f"{i:2}" for i in range(self.width)))
        for y in range(self.height):
            print(f"{y:2}", end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print(" *", end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(f" {count}" if count > 0 else "  ", end=' ')
                else:
                    print(" .", end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if (y * self.width + x) in self.mines:
            return False
        self.revealed[y][x] = True
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def all_safe_cells_revealed(self):
        """Vérifie si toutes les cases sans mine ont été révélées."""
        for y in range(self.height):
            for x in range(self.width):
                # Vérifie si la cellule est non-mine et non révélée
                if (y * self.width + x) not in self.mines and not self.revealed[y][x]:
                    return False
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Entrez la coordonnée x : "))
                y = int(input("Entrez la coordonnée y : "))
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Coordonnées hors limites. Réessayez.")
                    input("Appuyez sur Entrée pour continuer...")
                    continue
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("💥 GAME OVER ! Vous avez déclenché une mine.")
                    break
                if self.all_safe_cells_revealed():
                    self.print_board(reveal=True)
                    print("🎉 Félicitations ! Vous avez gagné !")
                    break
            except ValueError:
                print("Entrée invalide. Veuillez entrer uniquement des nombres.")
                input("Appuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
