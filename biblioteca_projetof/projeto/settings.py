import json

ARQUIVO = "settings.json"

def carregar_settings():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "genero_favorito": None,
            "limite_leituras_simultaneas": None,
            "meta_anual_leituras": None
        }
