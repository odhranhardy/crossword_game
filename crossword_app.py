from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class CrosswordCell(TextInput):
    def __init__(self, is_active=True, **kwargs):
        super().__init__(**kwargs)
        self.multiline = False
        self.max_length = 1
        self.input_filter = 'alpha'  # Only letters
        self.disabled = not is_active
        self.background_color = (1, 1, 1, 1) if is_active else (0, 0, 0, 1)
        self.foreground_color = (0, 0, 0, 1) if is_active else (1, 1, 1, 1)
        self.size_hint = (None, None)
        self.size = (50, 50)
        self.halign = 'center'
        self.valign = 'middle'
        self.font_size = 20
        self.on_text_validate = self.on_text_change
        self.bind(text=self.on_text_change)

    def on_text_change(self, instance, value):
        if len(value) > 1:
            self.text = value[-1].upper() if value else ""
        else:
            self.text = value.upper() if value else ""

class CrosswordGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 5
        self.spacing = 2
        self.padding = 10
        # Sample grid: 1=active (white), 0=inactive (black)
        self.grid_layout = [
            [1, 1, 0, 1, 1],
            [1, 0, 1, 0, 1],
            [0, 1, 1, 1, 0],
            [1, 0, 1, 0, 1],
            [1, 1, 0, 1, 1]
        ]
        self.cells = {}
        for row in range(5):
            for col in range(5):
                is_active = self.grid_layout[row][col] == 1
                cell = CrosswordCell(is_active=is_active)
                self.add_widget(cell)
                if is_active:
                    self.cells[(row, col)] = cell

    def get_answers(self):
        return {(row, col): cell.text for (row, col), cell in self.cells.items()}

class CrosswordApp(App):
    def build(self):
        Window.size = (400, 500)  # Simulate mobile screen
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Title
        title = Label(text="Crossword Puzzle", font_size=24, size_hint=(1, 0.1))
        layout.add_widget(title)
        
        # Grid
        self.grid = CrosswordGrid(size_hint=(1, 0.7))
        layout.add_widget(self.grid)
        
        # Check button
        check_btn = Button(text="Check Answers", size_hint=(1, 0.1))
        check_btn.bind(on_press=self.check_answers)
        layout.add_widget(check_btn)
        
        return layout

    def check_answers(self, instance):
        answers = self.grid.get_answers()
        # Placeholder: Check against a correct solution