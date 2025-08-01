import json
from typing import List, Dict, Optional

class Cell:
    """
    Represents a cell in the crossword grid.
    
    Attributes:
        is_active (bool): Indicates if the cell is part of the puzzle.
        correct_letter (Optional[str]): The correct letter for active cells, uppercase.
        number (Optional[int]): The clue number if the cell is the start of a word.
    """
    def __init__(self, is_active: bool, correct_letter: Optional[str] = None, number: Optional[int] = None):
        self.is_active = is_active
        if is_active:
            if correct_letter is None or not isinstance(correct_letter, str) or len(correct_letter) != 1 or not correct_letter.isalpha():
                raise ValueError("correct_letter must be a single alphabetic character")
            self.correct_letter = correct_letter.upper()
        else:
            self.correct_letter = None
        self.number = number

class Puzzle:
    """
    Represents the crossword puzzle, including the grid and clues.
    
    Attributes:
        grid (List[List[Cell]]): 2D list representing the grid of cells.
        across_clues (Dict[int, str]): Dictionary of across clues with clue numbers as keys.
        down_clues (Dict[int, str]): Dictionary of down clues with clue numbers as keys.
    """
    def __init__(self):
        self.grid: List[List[Cell]] = []
        self.across_clues: Dict[int, str] = {}
        self.down_clues: Dict[int, str] = {}

    def load_from_file(self, file_path: str) -> None:
        """
        Loads the puzzle data from a JSON file.
        
        The JSON should have the following structure:
        {
            "grid": [
                [{"letter": "A", "number": 1}, {"letter": "B", "number": null}, ...],
                ...
            ],
            "across_clues": {
                "1": "Clue text",
                ...
            },
            "down_clues": {
                "1": "Clue text",
                ...
            }
        }
        Where "letter" is the correct letter (string) or null for inactive cells,
        and "number" is the clue number (integer) or null.
        
        Raises:
            ValueError: If the grid rows have inconsistent numbers of columns.
        """
        with open(file_path, 'r') as f:
            data = json.load(f)
        grid_data = data['grid']
        self.grid = []
        for row in grid_data:
            row_cells = []
            for cell_data in row:
                letter = cell_data['letter']
                number = cell_data['number']
                if letter is None:
                    cell = Cell(is_active=False, number=number)
                else:
                    cell = Cell(is_active=True, correct_letter=letter, number=number)
                row_cells.append(cell)
            self.grid.append(row_cells)
        # Validate that all rows have the same number of columns
        if self.grid:
            num_cols = len(self.grid[0])
            for row in self.grid:
                if len(row) != num_cols:
                    raise ValueError("Grid rows have inconsistent number of columns")
        # Convert clue keys to integers
        self.across_clues = {int(k): v for k, v in data['across_clues'].items()}
        self.down_clues = {int(k): v for k, v in data['down_clues'].items()}

    def get_cell(self, row: int, col: int) -> Cell:
        """
        Retrieves the cell at the specified row and column.
        
        Args:
            row (int): The row index.
            col (int): The column index.
        
        Returns:
            Cell: The cell at the specified position.
        """
        return self.grid[row][col]

    def get_clue(self, number: int, direction: str) -> Optional[str]:
        """
        Retrieves the clue text for the specified clue number and direction.
        
        Args:
            number (int): The clue number.
            direction (str): The direction, either 'across' or 'down'.
        
        Returns:
            Optional[str]: The clue text if found, otherwise None.
        """
        if direction == 'across':
            return self.across_clues.get(number)
        elif direction == 'down':
            return self.down_clues.get(number)
        else:
            return None

    @property
    def rows(self) -> int:
        """
        Returns the number of rows in the grid.
        
        Returns:
            int: The number of rows.
        """
        return len(self.grid)

    @property
    def cols(self) -> int:
        """
        Returns the number of columns in the grid.
        
        Returns:
            int: The number of columns, or 0 if the grid is empty.
        """
        if self.grid:
            return len(self.grid[0])
        else:
            return 0