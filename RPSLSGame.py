import random
import os
import sys
import time
from collections import defaultdict

# --- Game Constants ---
COMPUTER_NAMES = ['Sheldon', 'Amy', 'Leonard', 'Penny', 'Howard', 'Bernadette', 'Raj']
DEFAULT_CHOICES = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['spock', 'paper'],
    'spock': ['scissors', 'rock']
}
DEFAULT_SHORTCUTS = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors',
    'l': 'lizard',
    'k': 'spock'
}
ASCII_ART = {
    'rock': """
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣄⣀⣀⡀
⠀⠀⠀⠀⠀⠀⢠⣶⠟⠉⠁⠀⣠⠉⠉⠛⠳⣦⣄⡀
⠀⠀⠀⠀⠀⢰⡿⠁⠀⣀⣠⠞⠁⠀⠀⠀⠀⠀⠉⠻⣶⡶⠶⣦⡀
⠀⣠⡶⠟⠛⠛⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣄⠈⢿⡄
⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣤⣤⣶⠈⣿⡀⠘⣷
⠸⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⢀⣀⡀⠹⣧⠀⢻⡄
⠀⣼⡿⠶⠦⠤⠤⠤⠀⠀⠀⠀⠀⠀⢠⣤⡶⠶⠞⠛⢋⡁⠀⣿⠀⢸⡧
⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡶⠟⠃⢀⣿⢀⣾⠁
⢸⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⢀⣿⡛⠛⠁
⠈⠻⣶⣄⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠁
⠀⠀⠀⢹⣯⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠟⠋⠀
⠀⠀⠀⠀⠙⠿⣶⣤⣤⣀⣀⣠⣤⣴⡶⠾⠛⠉
""",
    'paper': """
     ⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⢀⣀⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⢠⣾⠟⠉⠀⠈⠙⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀
                      ⣴⠟⠁⠀⠀⠀⠀⢀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀
  ⢠⣴⠶⠶⠶⣦⣄⠀ ⠀⠀⠀⠀⠀⠀⣠⣾⠋ ⠀⠀⠀⠀⠀⣰⠟⠁⠀⠀⣀⣀⣀⡀⠀⠀⠀
 ⢸⡇⠀⠀⠀⠀ ⠹⣧⠀⠀⠀⠀⢀⣴⠟⠁⠀ ⠀⠀⠀⢀⣼⠏⢀⣠⡶⠟⠋⠉⠉⠛⢷⣄⠀
 ⠸⣧⠀⠀⠀⠀⠀⢻⡇⠀ ⣠⡿ ⠃⠀⠀⠀⠀⠀⢠⣾⣧⠾⠛⠉⠀ ⠀⠀⠀⠀⠀ ⢈⣿⠀
  ⢻⣇⠀⠀⠀⠀⠘⣇⣴⡾⠋⠀⠀⠀⠀⠀⠀⣰⡿⠛⠁⠀⠀⠀⠀⠀ ⠀⠀⣀⣴⠟⠋⠀
   ⣿⡇⠀⠀⠀⠀⠟⠁⠀⠀⠀⠀⠀⠀⠀⣸⠋⠀⠀⠀⠀⠀⠀ ⠀⣀⣴⠿⠋⠁⠀⠀⠀
   ⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠁⠀⠀⠀⠀ ⠀⢀⣤⠾⠋ ⣀⣠⣤⣤⣤⣄⡀
  ⠂⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠿⠛⠛⠛⠉⠉⠁  ⠀⠀⠙⣿
 ⢀⣼⡇⠀⠀⠀⢀⣴⡄⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠁⠀⠀ ⠀⠀⠀⠀ ⠀⣀⣤⡾⠏
 ⡿⠉⣷⠀⢀⣴⡿⠋⠀⢀⣴⠿⠁⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀ ⠀⢀⣠⣴⠾⠛⠉⠁⠀⠀
 ⣷ ⠀⢻⣧⠈⠁⢀⣤⡾⠋⠁⢀⡀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠾⠛⠉⠀⠀⠀⠀⠀⠀⠀
 ⠹⣇ ⠀⠹⣷⡀⠉⠁⣤⣴⠶⠛⠋⠀⠀⠀⠀⠀⣀⣴⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  ⠹⣧⡀ ⠈⢿⣦⡀⠁⠀⠀⠀⠀⠀⠀⣀⣴⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
   ⠈⠻⣦⣄⣈⣻⡷⠶⣶⣶⡶⠶⠾⠛⠋⠁
""",
    'scissors': """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣠⣀⣀⣀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣤⠶⠿⣶⣤⡶⠟⠛⠉⠉⠉⢉⡉⠙⠛⢷⣦⡀
⠀⠀⠀⠀⣰⡟⠁⢠⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠹⣄⠀⠀  ⠙⢿⡄
⠀⠀⠀⣰⡏⠀⣰⡟⠀⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣦⣄ ⣸⣇
⠀⠀⢠⡟⠀⣰⡟⠀⣄⠈⠉⠛⠻⠆⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠳⠶⠶⠶⠶⣤⣭⣭⣋⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⡇⢀⣿⠁⢠⠛⠿⢶⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀⠀⠈⠙⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⣷⣼⣇⠀⠘⢷⣄⡀⠈⠙⠿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠉⢿⡆⠀⠀⠙⠻⠆⠀⠀⠀⠀⠀⠀⠀⠀⠘⠒⠒⠒⠶⢶⣶⣶⣤⣤⣤⣤⣤⣀⣀⣀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⢿⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠷⣦⣀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠉⠛⠲⢶⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠶⣦⣤⣄⣠⣤⣤⠶⠟⠋⠉⠛⠳⢶⣤⣀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠉⠛⠷⣦⣄⡀⣀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      ⠈⠉⠉⠉⠁⠀⠀⠀
""",
    'lizard': """
⠀⢀⣀⣤⡶⠟⠛⠛⠷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣼⡟⠉⢀⡀⠀⢀⣤⣶⣬⠻⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠻⣷⢦⣀⠀⠀⠘⠿⡿⠿⢦⡄⠙⠿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣤⣤⣶⣶⣶⣦⣤⣤⣤⣤⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠙⢧⡈⠳⣄⠀⠀⠀⠀⠀⠙⠷⣄⠘⣷⡄⠀⠀⠀⠀⠀⣤⠶⣛⣯⣿⠿⠛⠋⠉⠁⢀⣠⠤⠒⠋⠉⠁⠀⠀⠀⠈⠉⠉⠉⠙⠛⠛⠶⢶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⢻⣦⠈⠓⢤⣀⠀⠀⠰⣶⣯⠙⠾⣿⣦⣀⣠⣤⠴⠿⠛⠉⠁⠀⢀⣀⡤⠴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⠶⣤⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⣷⡀⠀⠈⠙⠲⠶⣽⡅⠀⢀⣈⣃⣭⡉⠓⠒⠒⠒⠋⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢶⣤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠻⢶⣤⣀⡀⢀⣤⣇⣀⣩⣿⣹⣿⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡅⠀⠙⢿⡉⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣦⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣾⣿⣾⣿⣿⣿⣿⢣⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠸⡟⠉⠉⠀⠀⠀⠀⠈⠉⠉⠙⠛⠳⢶⣤⣀⠀⠀⠀⠀⠘⣷⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠙⣿⡿⠿⢿⠋⠁⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠷⣄⠀⠀⠙⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣦⡄⠀⠀⡿⣷
⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠈⠉⡟⢧⣴⠋⡥⠒⠒⠲⣄⠙⠿⢶⢴⣶⣤⣤⣀⣀⣀⣀⣀⣤⡾⢋⡾⠃⠀⠈⢧⡄⢀⣿⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡆⢀⠇⢸
⠀⠀⠀⠀⠀⠀⠀⢰⠏⠀⠀⣸⠇⠀⠉⠛⠳⢤⣀⠀⠈⠳⣤⡀⠀⠀⠀⠉⠉⠉⠉⠉⠉⣩⣴⠟⠁⠀⠀⠀⡾⢻⡟⠉⠶⣾⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣧⠋⢠⡿
⠀⠀⠀⣀⣠⣤⣀⡟⠀⠀⣼⠋⠀⠀⠀⠀⠀⠀⠙⢷⡄⠀⠈⠻⣷⠿⠶⠦⣤⣤⣤⡶⠞⠋⠁⠀⠀⠀⠀⠀⠻⣬⣿⣦⡻⣦⣝⣷⡄⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⠾⠋⢀⣴⠟⠁
⠀⠀⣾⣿⣯⣭⡿⠃⠀⢘⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣀⣀⡘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠛⣿⡟⣿⡏⢻⣿⠀⢀⣠⣤⡶⠶⠛⠋⣉⣠⡴⠞⠛⠁⠀⠀
⠀⢠⣧⢾⣶⡚⣚⣀⣠⣟⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⠘⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠁⠘⠃⢀⣵⣾⣿⣭⠴⠶⠒⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠃⣿⠟⠉⠉⢹⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄⠀⠈⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⠿⢾⣇⡀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣾⣿⠖⠒⢃⣥⠐⢚⠙⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣵⠛⠉⡿⣯⡵⠶⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⣿⡏⠀⠀⢙⣟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    'spock': """
                            .ss$$$$$$$$$$$$$$$ss.
                       .s$$$$$$$$$$$$$$$$$$$$$$$$$$ss.
                   .s$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$s
                 .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
               .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$s
             .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$s.
            $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
          .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
          $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$                                  $$
        $$$$$$$$$$$$$$$$$$     .
       s$$$$$$$$$$$$$$$$$     sssss.                           s
      ss $$$$$$$$$$$$$$$          ssss                      ss$s
     sss   $$$$$$$$$$$            ssss$$$$ss              $$$$s.
    sssss   $$$$$$$$   s.      .sss$$$$$$$$sss      sss$$$$$$s
    ss$ssss  $$$$$$$  sss.  .ss$$$$$$ss$ss     .         s$$$$s.
    ss$s   s  $$$$$$ ss.ss           ..        ss           .sss
     ss   s $s $$$$$ ss..s.                   ss
      s ss$$$$s $$$$ ssssss.                 .ss
    ss     s$$$s $$$ ssssssssss..           ssss.              .
    ss      $$  s $$ ss..ss$$$$sss        .sssss              ..
     s      s$$ss  $ ssss.sss$$$sss       .sssss.     ss..
      s.     $     $ .sss . .ss$sss        .  sssssss...   ss$
        ss   sssss$$ ..ss   ...sssss            .sss.       s
          ss    $$ $ .ss..s .sssssss
            ss$$  $$  .ssssss .sssss              ..       $
                $$$$  .ss$$ssss...s.s        ..sss$$ssss.
               $$.$$$  .ss$$sss.. sss.    .ssss$$s..s$ss. s
               ss ssss  .sssssss...sss.      .ssss$$ss..  .
               ss  ssss   .ssssssss.sss.        .sss.
               ss    .ssss    .sssssssss.               s
               ss      .sssss.  .sssssss.s .. ..ss$s. .s
              ss         sssssss.  .sssssssssssss$$s. .ss
            $ss           ssssssss.   ..sssssssssss  .ss.
          $$$$.            .sssssssss.     ssssss ssss.$s
      s$$$$$$$$s.             ..ssssssssss......ssss. s$$$s
    .s$$$$$$$$$$$s.              .ssssssssssssssss. s$$$$$ss.
       s$$$$$$$$$$$$$$ss..          .ssssssssss. .s$$$$$$$$s
         s$$$$$$$$$$$$$$$$$$$ssss...   ...ss.. s$$$$$$$$$s
           s$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$s
              .s$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$s
                    .s$$$$$$$$$$$$$$$$$$$$$$$$$$$$$s
                          .s$$$$$$$$$$$$$$$$$$$$s
                                ..s$$$$$$$$$$s
"""
}
PAUSE_SHORT = 0.5

class RPSLSGame:
    def __init__(self):
        self.choices = DEFAULT_CHOICES
        self.shortcuts = DEFAULT_SHORTCUTS
        self.player1_score = 0
        self.player2_score = 0
        self.player_tie = 0
        self.rounds_played = 0
        self.player_history = []
        self.difficulty = 'easy'
        self.mode = 'single'
        self.player1_name = 'Player 1'
        self.player2_name = 'Computer'

    def _clear_screen(self):
        """Clears the console screen with a safe fallback."""
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
        except Exception:
            print("\n" * 10)

    def _get_raw_input(self, prompt, preserve_case=False):
        """Safely collects raw input."""
        try:
            user_input = input(prompt).strip()
            return user_input if preserve_case else user_input.lower()
        except EOFError:
            print("Error: Input stream ended unexpectedly.")
            return None
        except KeyboardInterrupt:
            print("\nInput interrupted. Assuming quit.")
            return "quit"
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def _setup_game(self):
        """Sets up game mode (single or multi player), difficulty mode, and custom choices."""
        self._clear_screen()
        print("--- Rock, Paper, Scissors, Lizard, Spock Setup ---")
        self.player1_name = self._get_raw_input("Player 1 enter your name or just press enter: ", preserve_case=True) or 'Player 1'
        time.sleep(PAUSE_SHORT)
        print(f"Are you ready to play {self.player1_name}?")
        
        # Choose single or multi user mode
        while True:
            mode = self._get_raw_input("Please choose a mode (single/multi): ")
            if mode in ['single', 'multi']:
                self.mode = mode
                #self.player2_name = 'Player 2' if mode == 'multi' else 'Computer'
                self.player2_name = 'Player 2' if mode == 'multi' else random.choice(COMPUTER_NAMES)
                print(f"Your opponent for this game is {self.player2_name}!")
                time.sleep(PAUSE_SHORT)
                break
            print("Invalid mode. Enter 'single' or 'multi'.")

        # Set names for multiplayer
        if self.mode == 'multi':
            self.player1_name = self._get_raw_input("Player 1 enter your name or just press enter: ", preserve_case=True) or 'Player 1'
            time.sleep(PAUSE_SHORT)
            print(f"Are you ready to play {self.player1_name}?")
            self.player2_name = self._get_raw_input("Player 2 enter your name or just press enter: ", preserve_case=True) or 'Player 2'
            time.sleep(PAUSE_SHORT)
            print(f"Are you ready to play {self.player2_name}?")

        # Choose difficulty for single-player
        if self.mode == 'single':
            while True:
                diff = self._get_raw_input("Please choose a difficulty level easy/medium/hard): ")
                if diff in ['easy', 'medium', 'hard']:
                    self.difficulty = diff
                    break
                print("Invalid difficulty. Enter 'easy', 'medium', or 'hard'.")

        # Custom choices
        use_custom = self._get_raw_input("Would you like to use custom choices? (yes/no): ")
        if use_custom in ['yes', 'y']:
            self._setup_custom_choices()

    def _setup_custom_choices(self):
        """Sets up custom choices and win conditions."""
        self.choices = {}
        self.shortcuts = {}
        print("Enter at least 3 choices ( an odd number is recommended).")
        print("For each choice, specify its name and the two choices it beats.")
        print("For example: 'fire' beats 'ice,grass'")

        while True:
            num_choices = self._get_raw_input("How many choices (3 or more)? ")
            try:
                num_choices = int(num_choices)
                if num_choices >= 3:
                    break
                print("Must have at least 3 choices.")
            except ValueError:
                print("Enter a valid number.")

        for i in range(num_choices):
            while True:
                name = self._get_raw_input(f"Enter choice {i+1} name: ")
                if not name or name in self.choices:
                    print("Name cannot be empty or duplicate.")
                    continue
                beats = self._get_raw_input(f"What does '{name}' beat? (comma-separated, two choices): ")
                beats = [b.strip() for b in beats.split(',') if b.strip()]
                if len(beats) != 2:
                    print("You must specify exactly two choices to beat.")
                    continue
                self.choices[name] = beats
                self.shortcuts[name[0]] = name
                break

        # Validate custom choices
        for choice, beats in self.choices.items():
            for b in beats:
                if b not in self.choices:
                    print(f"Error: '{b}' is not a valid choice. Resetting to default.")
                    self.choices = DEFAULT_CHOICES
                    self.shortcuts = DEFAULT_SHORTCUTS
                    return

    def _get_player_choice(self, player_name):
        """Gets player's choice and validates it."""
        max_attempts = 5
        attempts = 0
        prompt = f"{player_name}, enter choice ({', '.join(f'{k}/{v}' for k, v in self.shortcuts.items())} or q/quit): "

        while attempts < max_attempts:
            choice_input = self._get_raw_input(prompt)
            if choice_input in ['quit', 'q'] or choice_input is None:
                return None

            choice = self.shortcuts.get(choice_input, choice_input)
            if choice in self.choices:
                if player_name == self.player1_name:
                    self.player_history.append(choice)
                    if len(self.player_history) > 10:
                        self.player_history.pop(0)
                return choice
            else:
                print(f"Invalid choice. Use {', '.join(f'{k}/{v}' for k, v in self.shortcuts.items())} or q/quit: ")
                attempts += 1
                if attempts < max_attempts:
                    print(f"Attempts remaining: {max_attempts - attempts}")
                time.sleep(PAUSE_SHORT)

        print(f"Too many invalid inputs ({max_attempts}). Would you like to retry? (yes/no): ")
        retry = self._get_raw_input("Enter 'yes' or 'no': ")
        if retry in ['yes', 'y']:
            return self._get_player_choice(player_name)
        return None

    def _get_computer_choice(self):
        """Returns computer choice based on difficulty."""
        if self.difficulty == 'easy': # easy difficulty
            return random.choice(list(self.choices.keys()))
        elif self.difficulty == 'medium': # medium difficulty
            if len(self.player_history) >= 3:
                last_choices = self.player_history[-3:]
                counters = [c for choice in last_choices for c in self.choices if choice in self.choices[c]]
                return random.choice(counters) if counters else random.choice(list(self.choices.keys()))
            return random.choice(list(self.choices.keys()))
        else:  # hard difficulty
            if len(self.player_history) < 2:
                return random.choice(list(self.choices.keys()))
            transitions = defaultdict(lambda: defaultdict(int))
            for i in range(len(self.player_history)-1):
                current, next_choice = self.player_history[i], self.player_history[i+1]
                transitions[current][next_choice] += 1
            last_choice = self.player_history[-1]
            next_likely = max(transitions[last_choice], key=transitions[last_choice].get, default=None)
            if next_likely:
                counters = [c for c in self.choices if next_likely in self.choices[c]]
                return random.choice(counters) if counters else random.choice(list(self.choices.keys()))
            return random.choice(list(self.choices.keys()))

    def _determine_winner(self, player1_choice, player2_choice):
        """Determines the round winner."""
        if player1_choice == player2_choice:
            self.player_tie += 1
            return f"It's a tie! You both chose {player1_choice.capitalize()}.", None
        if player2_choice in self.choices[player1_choice]:
            self.player1_score += 1
            return f"{self.player1_name} wins! {player1_choice.capitalize()} beats {player2_choice.capitalize()}.", True
        else:
            self.player2_score += 1
            return f"{self.player2_name} wins! {player2_choice.capitalize()} beats {player1_choice.capitalize()}.", False

    def _print_status(self):
        """Prints the current game status."""
        self._clear_screen()
        print("\n--- Rock, Paper, Scissors, Lizard, Spock ---")
        print(f"Mode: {'Single-Player' if self.mode == 'single' else 'Multiplayer'}")
        if self.mode == 'single':
            print(f"Difficulty: {self.difficulty.capitalize()}")
        print(f"Round: {self.rounds_played}")
        print(f"Score: {self.player1_name} {self.player1_score} | {self.player2_name} {self.player2_score}")
        print()

    def play(self):
        """Main game loop."""
        self._setup_game()
        print("\nRules:")
        for choice, beats in self.choices.items():
            print(f"  {choice.capitalize()} beats {beats[0].capitalize()} and {beats[1].capitalize()}")
        print("Enter full names or shortcuts. Type 'quit' or 'q' to exit.")
        
        while True:
            self._print_status()
            player1_choice = self._get_player_choice(self.player1_name)
            if player1_choice is None:
                print(f"\nFinal Score: {self.player1_name} {self.player1_score} | {self.player2_name} {self.player2_score}")
                print("Thanks for playing Rock, Paper, Scissors, Lizard, Spock!")
                break
            
            if self.mode == 'multi':
                print("\n" * 10)
                print(f"{self.player2_name}'s turn. {self.player1_name}, look away!")
                player2_choice = self._get_player_choice(self.player2_name)
                if player2_choice is None:
                    print(f"\nFinal Score: {self.player1_name} {self.player1_score} | {self.player2_name} {self.player2_score} | Ties: {self.player_tie}")
                    print("Thanks for playing Rock, Paper, Scissors, Lizard, Spock!")
                    break
            else:
                player2_choice = self._get_computer_choice()
            
            self.rounds_played += 1
            
            print(f"\n{self.player1_name} chose: {player1_choice.capitalize()}")
            print(ASCII_ART.get(player1_choice, "No ASCII art available"))
            print(f"{self.player2_name} chose: {player2_choice.capitalize()}")
            print(ASCII_ART.get(player2_choice, "No ASCII art available"))
            result, _ = self._determine_winner(player1_choice, player2_choice)
            print(result)
            time.sleep(PAUSE_SHORT * 2)
            
            print("\nWould you like to play another round? (yes/no): ")
            play_again = self._get_raw_input("")
            if play_again not in ['yes', 'y']:
                print(f"\nFinal Score: {self.player1_name} {self.player1_score} | {self.player2_name} {self.player2_score} | Ties: {self.player_tie}")
                print("Thanks for playing Rock, Paper, Scissors, Lizard, Spock!")
                break

def main():
    """Main function to start the game."""
    try:
        game = RPSLSGame()
        game.play()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Game will exit.")

if __name__ == "__main__":
    main()