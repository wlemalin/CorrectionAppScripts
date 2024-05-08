"""
main_script.py

This is the main script that orchestrates the translation of natural language 
requests to R code using Replicate's API.
It handles clipboard input and output, prepares attachment files, and interacts 
with the Replicate API.

Functions:
    - translate_to_r_with_replicate(text): Sends the text to Replicate's API 
      for translation into R code.
    - main(): The main function orchestrating the translation process.
"""

import os
import replicate
from replicate.exceptions import ReplicateError
from clipboard_utils import get_clipboard, copy_to_clipboard
from attachment_utils import initialise_file_pj, prepare_csv

# If API-KEY problem, just paste yours below
os.environ['REPLICATE_API_TOKEN'] = 'r8_O4277pIV92WO3V9VhewlbxS23KGOWW64Q4fJP'

# Assurez-vous que la variable d'environnement est définie
REPLICATE_API_TOKEN = os.getenv('REPLICATE_API_TOKEN')
if REPLICATE_API_TOKEN is None:
    raise EnvironmentError("REPLICATE_API_TOKEN is not set in the environment")

# Configuration initiale de Replicate
replicate.api_token = REPLICATE_API_TOKEN

def translate_to_r_with_replicate(text):
    """Envoie le texte à l'API Replicate pour traduction en code R."""
    input_data = {
        "prompt": (
            "Le texte suivant contient une demande en langage naturel pour "
            "générer du code R. "
            "La demande est encadrée par ***. Elle peut etre suivit par des "
            "tableaux de données qui sont précédés par une ligne de 98 #, "
            "ces tableaux te serviront à comprendre la structure "
            "des données utilisées, tu ne dois pas écrire dans ta réponse "
            "la partie data loading. "
            "Traduire la demande en code R et fournir le code et les commentaires "
            "nécessaires :\n\n"
            f"{text}\n\n"
        ),
        "prompt_template": (
            "system\n\nTu es un Assistant très efficace pour générer du code R "
            "à partir de demandes en langage naturel et tu dois suivre les "
            "instructions suivantes :\n\n{prompt}\n\n"
        )
    }
    try:
        output = replicate.run("meta/meta-llama-3-70b-instruct", input=input_data)
        response_text = "".join(output)  # Joindre les parties de la réponse
        return response_text
    except ReplicateError as e:
        print(f"Erreur liée à Replicate lors de l'envoi de la demande: {e}")
    except FileNotFoundError as e:
        print(f"Erreur : Le fichier spécifié n'a pas été trouvé: {e}")
    except OSError as e:
        print(f"Erreur système : {e}")
    except ValueError as e:
        print(f"Erreur de valeur : {e}")
    return None

def main():
    """Launches the whole process"""
    initialise_file_pj()
    text_from_clipboard = get_clipboard() + prepare_csv()
    print(f"Texte récupéré du presse-papiers : {text_from_clipboard}")
    translated_code = translate_to_r_with_replicate(text_from_clipboard)
    if translated_code:
        print("Code R généré par Replicate:")
        print(translated_code)
        copy_to_clipboard(translated_code)
        print("Code R copié de nouveau dans le presse-papiers.")
    else:
        print("Aucune réponse reçue ou erreur lors de la récupération de la réponse.")

if __name__ == "__main__":
    main()
