import os
import replicate
import pyperclip
import re


# Assurez-vous que la variable d'environnement est définie
REPLICATE_API_TOKEN = os.getenv('REPLICATE_API_TOKEN')

if REPLICATE_API_TOKEN is None:
    raise EnvironmentError("REPLICATE_API_TOKEN is not set in the environment")

# Configuration initiale de Replicate
replicate.api_token = REPLICATE_API_TOKEN


def get_clipboard():
    """Récupère le texte du presse-papiers."""
    return pyperclip.paste()

def correct_text_with_replicate(text):
    """Envoie le texte à l'API Replicate pour correction et extrait uniquement le texte corrigé."""
    input = {
        "prompt": f"Corrige les fautes d'orthographe, de grammaire, de syntaxe, de conjugaison, etc., dans le texte suivant et retourne uniquement le texte corrigé dans la langue originale, placé entre guillemets : \"{text}\"",
        "prompt_template": "system\n\nTu es un Assistant très efficace en traduction et tu dois suivre les instructions suivantes :\n\n{prompt}\n\n"
    }
    try:
        output = replicate.run("meta/meta-llama-3-70b-instruct", input=input)
        response_text = "".join(output)
        
        # Extraire le texte corrigé entre guillemets
        corrected_text = re.findall(r'\"(.*?)\"', response_text)
        if corrected_text:
            return corrected_text[0]
        else:
            return "Aucun texte corrigé trouvé."
    except Exception as e:
        print(f"Erreur lors de l'envoi de la demande à Replicate: {e}")
        return None

def main():
    text_from_clipboard = get_clipboard()
    print(f"Texte récupéré du presse-papiers : {text_from_clipboard}")
    
    corrected_text = correct_text_with_replicate(text_from_clipboard)
    if corrected_text:
        print("Texte corrigé de Replicate:")
        print(corrected_text)
        pyperclip.copy(corrected_text)
        print("Réponse corrigée copiée de nouveau dans le presse-papiers.")
    else:
        print("Aucune réponse reçue ou erreur lors de la récupération de la réponse.")

if __name__ == "__main__":
    main()

