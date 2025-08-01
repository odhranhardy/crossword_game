from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from src.crossword.game.puzzle import Puzzle
from src.crossword.ui.crossword_grid import CrosswordGrid
import os

class CrosswordApp(App):
    def build(self):
        # Load the puzzle from JSON
        puzzle = Puzzle()
        puzzle_file = os.path.join(os.path.dirname(__file__), 'data', 'puzzle.json')
        puzzle.load_from_file(puzzle_file)
        
        # Create the crossword grid with size based on puzzle dimensions
        cell_size = 60  # Increased cell size for better visibility
        grid = CrosswordGrid(
            puzzle,
            size_hint=(None, None),
            size=(puzzle.cols * cell_size, puzzle.rows * cell_size),
            padding=10,
            spacing=2
        )
        
        # Center the grid using AnchorLayout
        layout = AnchorLayout(anchor_x='center', anchor_y='center')
        layout.add_widget(grid)
        return layout