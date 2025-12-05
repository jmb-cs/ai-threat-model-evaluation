import os
import json

from argparse import ArgumentParser

from utils.convert_model import convert_STRIDEgpt
from utils.files import load_assets


def extract_STRIDEgpt_models(assets: list[str], application: list[str], result_folder: str, folder_path:str) -> None:
    """
    Extracts threat models from markdown files in the STRIDEgpt_models directory,
    and saves them as a JSON file in the result directory.
    Parameters:
        applications (list[str]): List of application names to process.
        result_folder (str): Path to the directory where the JSON files will be saved.
    """
    application_path = f"{folder_path}/{application}"
    
    threat_model = convert_STRIDEgpt(application_path, assets)
    
    print(f"Threat model for {application} has {len(threat_model)} threats.")
    
    threat_path = f"{result_folder}/{application}/{folder_path}_stridegpt_model.json"
    with open(threat_path, "w") as json_file:
        json.dump(threat_model, json_file, indent=4)
        
if __name__ == "__main__":
    application = "iot"
    models = ["gpt_5_1", "gemini_2_5_pro", "qwen_3_235b_thinking"]
        
    result_folder = "results"
    
    print(f"[INFO] Processing threat models for application: {application}")
    
    for model in models:
        if not os.path.exists(f"{result_folder}/{application}"):
            os.makedirs(f"{result_folder}/{application}")

        assets = load_assets(f"threat_templates/{application}/assets.json")
        print(f"[INFO] System has assets: {assets}")
        
        extract_STRIDEgpt_models(assets, application, result_folder, model)
        print(f"[INFO] Extracted threat model for STRIDEgpt...")