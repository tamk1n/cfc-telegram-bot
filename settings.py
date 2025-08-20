import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHELSEA_API_URL = os.getenv('CHELSEA_API_URL')
LEAGUE_TABLE_API_URL = os.getenv('LEAGUE_TABLE_API_URL')
RESULTS_API_URL = os.getenv('RESULTS_API_URL')
PLAYER_STATS_API_URL = os.getenv('PLAYER_STATS_API_URL')

FIXTURES_CACHE_HOURS = float(os.getenv('FIXTURES_CACHE_HOURS', 2))
RESULTS_CACHE_HOURS = float(os.getenv('RESULTS_CACHE_HOURS', 0.5))
PLAYER_STATS_CACHE_HOURS = float(os.getenv('PLAYER_STATS_CACHE_HOURS', 24))
LEAGUE_TABLE_CACHE_HOURS = float(os.getenv('LEAGUE_TABLE_CACHE_HOURS', 2))

WEEKDAYS = {
    "Sun": "Sunday",
    "Mon": "Monday",
    "Tue": "Tuesday",
    "Wed": "Wednesday",
    "Thu": "Thursday",
    "Fri": "Friday",
    "Sat": "Saturday"
}

MONTHS = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sept": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

PLAYERS = [
            {"id": "7AJQtOXBgmRphJJCp2NvNR", "full_name": "Robert Sanchez", "number": 1},
            {"id": "3os8PwL1mJ2TJmGkhBDeDv", "full_name": "Filip Jorgensen", "number": 12},
            {"id": "4H1GhgvG1ldTNe8pgOUpol", "full_name": "Gaga Slonina", "number": 44},
            {"id": "78u6wchuqyJTlk2E0N4Skf", "full_name": "Marc Cucurella", "number": 3},
            {"id": "5nsrSil1MgDMLJn7APQgbD", "full_name": "Tosin Adarabioyo", "number": 4},
            {"id": "2JKytx9yLSwjXyOuW1jtQe", "full_name": "Benoit Badiashile", "number": 5},
            {"id": "5LOgdi9SSvd8dwRDyazmoZ", "full_name": "Levi Colwill", "number": 6},
            {"id": "2Be2AsOE5UnUayhdzMlVnF", "full_name": "Jorrel Hato", "number": 21},
            {"id": "jiKIenze7hskkncPNrA6B", "full_name": "Trevoh Chalobah", "number": 23},
            {"id": "4pu8Vnba43JYreI7ytlXGR", "full_name": "Reece James", "number": 24},
            {"id": "4AJxNxFWWKTy1xzuPeHMUL", "full_name": "Malo Gusto", "number": 27},
            {"id": "4CJuicRu1cGbhb22n7MNJh", "full_name": "Wesley Fofana", "number": 29},
            {"id": "5rRjJlyKtF87uvdKfy48F", "full_name": "Aaron Anselmino", "number": 30},
            {"id": "5QYkzwOGVPMISpU1HFtLUZ", "full_name": "Josh Acheampong", "number": 34},
            {"id": "6pEHcNajH2J2pTPneUXmXV", "full_name": "Enzo Fernandez", "number": 8},
            {"id": "3IjuqjelbhncAlTPIGE35R", "full_name": "Dario Essugo", "number": 14},
            {"id": "7qeAlzwWGlEyXKh6eHXcJY", "full_name": "Andrey Santos", "number": 17},
            {"id": "43oUZ5vRX4B6m61Pue0jWB", "full_name": "Moises Caicedo", "number": 25},
            {"id": "2fd36y1tclXGYu6pIMjOIL", "full_name": "Romeo Lavia", "number": 45},
            {"id": "2OCQIwCKdHMJNhImUsBRzw", "full_name": "Pedro Neto", "number": 7},
            {"id": "591Ncctlm9o6wWCTFrxfo0", "full_name": "Liam Delap", "number": 9},
            {"id": "2srYA1QS1OhCE45rzou1ZR", "full_name": "Cole Palmer", "number": 10},
            {"id": "5IobErY2OMIyoMUYzkJwmB", "full_name": "Jamie Gittens", "number": 11},
            {"id": "5UBDLH28hHkBfZ4sCiAFnA", "full_name": "Nicolas Jackson", "number": 15},
            {"id": "qbrH5sUyPH8swXEC2twTp", "full_name": "Christopher Nkunku", "number": 18},
            {"id": "2FwzGE2WMOHAnR0puVMisc", "full_name": "Joao Pedro", "number": 20},
            {"id": "5Y1CrHFGRhBLOjHMUNmkk5", "full_name": "Tyrique George", "number": 32},
            {"id": "7pQf4EbJjYGXqcniuC0I0t", "full_name": "Estevao", "number": 41},
            {"id": "3Fu6jUWvWDGabzNapGjtlz", "full_name": "Mykhailo Mudryk", "number": None}
        ]