from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from src.crossword.game.puzzle import Puzzle, Cell

class CrosswordGrid(GridLayout):
    def __init__(self, puzzle: Puzzle, **kwargs):
        super().__init__(**kwargs)
        self.cols = puzzle.cols
        self.rows = puzzle.rows
        self.cell_size = (60, 60)  # Increased cell size
        self.size = (self.cols * self.cell_size[0], self.rows * self.cell_size[1])
        self.padding = 10
        self.spacing = 2

        for row in range(puzzle.rows):
            for col in range(puzzle.cols):
                cell = puzzle.get_cell(row, col)
                cell_widget = self.create_cell_widget(cell)
                self.add_widget(cell_widget)

    def create_cell_widget(self, cell: Cell):
        cell_layout = FloatLayout(size=self.cell_size, size_hint=(None, None))
        
        if cell.is_active:
            # Active cell: TextInput for letter entry
            text_input = TextInput(
                size_hint=(None, None),
                size=self.cell_size,
                multiline=False,
                font_size=24,
                halign='center',
                background_color=(1, 1, 1, 1),  # White background
                foreground_color=(0, 0, 0, 1),  # Black text
                padding=[10, (self.cell_size[1] - 24) / 2 - 4, 10, (self.cell_size[1] - 24) / 2 - 4],  # Center vertically
            )
            text_input.bind(text=self.on_text_input)
            cell_layout.add_widget(text_input)
        else:
            # Inactive cell: Black square
            with cell_layout.canvas:
                Color(0, 0, 0, 1)  # Black color
                rect = Rectangle(pos=cell_layout.pos, size=cell_layout.size)
            # Bind to update rectangle when layout changes
            cell_layout.bind(pos=lambda instance, value: setattr(rect, 'pos', value))
            cell_layout.bind(size=lambda instance, value: setattr(rect, 'size', value))
        
        if cell.number is not None:
            # Add clue number in top-left corner
            number_label = Label(
                text=str(cell.number),
                size_hint=(None, None),
                size=(15, 15),
                pos_hint={'x': 0.05, 'y': 0.75},  # Top-left corner
                font_size=10,
                color=(0, 0, 0, 1)
            )
            cell_layout.add_widget(number_label)
        
        return cell_layout

    def on_text_input(self, instance, value):
        # Ensure only one uppercase letter is entered
        if len(value) > 1:
            instance.text = value[-1].upper()
        else:
            instance.text = value.upper()