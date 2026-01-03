import json
import os
import subprocess
import glob
from typing import List, Dict, Optional

SCENARIO_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'scenarios')

def get_scenarios() -> List[str]:
    """Returns a list of available scenario names defined inside the JSON files."""
    names = []
    for path in glob.glob(os.path.join(SCENARIO_DIR, "*.json")):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, dict) and "name" in data:
                    names.append(data["name"])
        except (json.JSONDecodeError, OSError):
            continue
    return names


def load_scenario(name: str) -> Optional[Dict]:
    """Loads a scenario by its internal name."""
    for path in glob.glob(os.path.join(SCENARIO_DIR, "*.json")):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, dict) and data.get("name") == name:
                    return data
        except (json.JSONDecodeError, OSError):
            continue
    return None

def execute_scenario(name: str) -> str:
    """Executes a scenario."""
    scenario = load_scenario(name)
    if not scenario:
        return f"Scenario '{name}' not found or invalid."
    
    results = []
    steps = scenario.get("steps", [])
    
    for step in steps:
        action = step.get("action")
        command = step.get("command")
        
        if action == "run" and command:
            try:
                # Use Popen to execute without blocking effectively, or blocking if needed.
                # Use subprocess to run the command
                subprocess.Popen(command, shell=True)
                results.append(f"Generic run: {command}")
            except Exception as e:
                results.append(f"Failed to run: {command} ({e})")
        else:
            results.append(f"Unknown action or missing command in step: {step}")
            
    return "\n".join(results)
