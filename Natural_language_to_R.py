import os
import replicate
import pyperclip
import re  # Cette importation est conservée au cas où vous souhaiteriez utiliser des regex pour d'autres traitements
import subprocess


#If API-KEY problem, just paste yours below
#os.environ['REPLICATE_API_TOKEN'] = ''

# Assurez-vous que la variable d'environnement est définie
REPLICATE_API_TOKEN = os.getenv('REPLICATE_API_TOKEN')
if REPLICATE_API_TOKEN is None:
    raise EnvironmentError("REPLICATE_API_TOKEN is not set in the environment")

# Configuration initiale de Replicate
replicate.api_token = REPLICATE_API_TOKEN

def get_clipboard():
    # Retrieve the current clipboard content using `xclip`
    result = subprocess.run(['xclip', '-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')


def translate_to_r_with_replicate(text):
    """Envoie le texte à l'API Replicate pour traduction en code R."""
    input = {
        "prompt": f"Le texte suivant contient une demande en langage naturel pour générer du code R. La demande est encadrée par ###. Traduire la demande en code R et fournir le code et les commentaires nécessaires :\n\n{text}",
        "prompt_template": "system\n\nTu es un Assistant très efficace pour générer du code R à partir de demandes en langage naturel et tu dois suivre les instructions suivantes :\n\n{prompt}\n\n"
    }
    try:
        output = replicate.run("meta/meta-llama-3-70b-instruct", input=input)
        response_text = "".join(output)  # Joindre les parties de la réponse
        return response_text
    except Exception as e:
        print(f"Erreur lors de l'envoi de la demande à Replicate: {e}")
        return None

def copy_to_clipboard(text: str):
    # Copy text to clipboard using `xclip`
    process = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
    process.communicate(input=text.encode('utf-8'))
    
def main():
    text_from_clipboard = get_clipboard()
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