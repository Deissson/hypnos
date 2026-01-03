import sys
import os

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

try:
    print("Testing imports...")
    from core import system
    from core import runner
    from bot import handlers
    from bot import keyboards
    from bot import main as bot_main
    print("Imports successful.")
except ImportError as e:
    print(f"Import failed: {e}")
    sys.exit(1)

print("Testing scenario loader...")
scenarios = runner.get_scenarios()
print(f"Found scenarios: {scenarios}")

if "example_scenario" in scenarios:
    data = runner.load_scenario("example_scenario")
    print(f"Loaded example_scenario: {data}")
else:
    print("example_scenario not found.")

print("Verification complete.")
