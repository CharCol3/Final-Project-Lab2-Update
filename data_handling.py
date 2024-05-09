import csv
from typing import List
from student import Student

def save_scores(filename: str, students: List['Student']) -> None:
    """
    Saves student scores to a CSV file.

    Parameters:
        filename (str): The path to the file where scores will be saved.
        students (list of Student): A list of Student objects whose scores will be saved.
    """
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Score 1', 'Score 2', 'Score 3', 'Score 4', 'Final Score'])
        
        for student in students:
            scores = student.scores + [0] * (4 - len(student.scores))
            final_score = max(scores)
            writer.writerow([student.name] + scores + [final_score])

def load_scores(filename: str) -> List[int]:
    """
    Loads scores from a CSV file.

    Parameters:
        filename (str): The path to the file from which scores will be loaded.

    Returns:
        List[int]: A list of scores loaded from the file.
    """
    try:
        with open(filename, 'r') as file:
            scores = [int(line.strip()) for line in file.readlines()]
        # Validate scores
        if any(score < 0 or score > 100 for score in scores):
            raise ValueError("All scores must be between 0 and 100")
        return scores
    except FileNotFoundError:
        return []
    except ValueError as e:
        print(f"Error reading scores: {e}")
        return []
