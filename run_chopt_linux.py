import subprocess
import os

# Define file paths
output_txt = "test/output.txt"
notes_file = "notes.mid"
chopt_executable = "./CHOpt_linux"

# Create test directory if not exists
if not os.path.exists("test"):
    os.makedirs("test")

# Run the CHOpt_linux application with the '-f notes.mid' argument only
command = [chopt_executable, "-f", notes_file]

try:
    # Execute command and capture output
    result = subprocess.run(command, capture_output=True, text=True)

    # Print stdout and stderr for debugging
    print("CHOpt_linux stdout:", result.stdout)
    print("CHOpt_linux stderr:", result.stderr)

    # Save terminal output to .txt file
    with open(output_txt, "w") as f:
        f.write(result.stdout)

except Exception as e:
    print(f"Error running CHOpt_linux: {e}")