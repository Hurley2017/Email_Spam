import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("Command output:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running the command: {e}")
        print("Command output (if available):")
        print(e.output)

if __name__ == "__main__":
    command_to_run = ["Flask", "scikit-learn", "pandas"]
    for command in command_to_run:
        ping = "pip install " + command
        run_command(ping)
