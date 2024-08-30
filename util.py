import yaml 
import os

def getConfig(file_path):
    # Define the path to the YAML file
    yaml_file_path = file_path

    # Read the YAML file
    with open(yaml_file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def getCharacter(subject):
    config = getConfig('character.yaml')
    return config[subject]

def getPrompts(prompts_file):
    # Check if the file exists
    if not os.path.exists(prompts_file):
        print(f"Error: {prompts_file} not found.")
    else:
        with open(prompts_file, 'r') as file:
            prompts = file.read().split('#')
    return prompts

