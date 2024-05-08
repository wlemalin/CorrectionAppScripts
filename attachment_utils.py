"""
attachment_utils.py

This module provides utility functions for managing file attachments,
particularly for handling CSV files.

Functions:
    - initialise_file_pj(): Sets the path to the directory for sending attachments.
    - prepare_csv(): Prepares and combines CSV tables for analysis and 
      returns them in Markdown format.
"""

import os
import re
import pandas as pd

def initialise_file_pj():
    """
    Défini le chemin d'accès vers le dossier qui servira à envoyer les pièces-jointes.
    """
    if not os.path.isfile('path_to_csv.txt'):
        attach_path = input("Path to file for attachments : /home/user/filepath/ \n\n")
        csv_path = f'path="{attach_path}"'
        with open('path_to_csv.txt', 'w', encoding='utf-8') as f:
            f.write(csv_path)

def prepare_csv():
    """
    Prépare et combine les tableaux CSV pour l'analyse.

    Returns:
        str: Une chaîne Markdown représentant les tableaux combinés.
    """
    input_table = []
    with open('path_to_csv.txt', "r", encoding='utf-8') as f:
        lines = f.readlines()
    csv_filepath = re.findall(r'"(.*?)"', lines[0])[0]
    file_names = os.listdir(csv_filepath)
    csv_files = [file for file in file_names if re.search(r'\.csv$', file)]
    if csv_files:
        combined_table = ''
        for csv in csv_files:
            t = pd.read_csv(csv_filepath + csv, nrows=200)
            merged_df = pd.concat([t.head(5), t.tail(5)], ignore_index=True)
            input_table = merged_df.to_markdown(tablefmt="grid")
            combined_table += 2 * "\n" + 98 * "#" + 2 * "\n" + input_table.strip()
        return combined_table
    return ""
