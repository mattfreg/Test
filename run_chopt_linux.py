import subprocess
import os

# Define file paths
output_txt = "test/output.txt"
notes_file = "notes.mid"
chopt_executable = "./CHOpt_linux"

# Create test directory if not exists
if not os.path.exists("test"):
    os.makedirs("test")

# Run the CHOpt_linux application with both -f and -o arguments
command = [chopt_executable, "-f", notes_file, "-o", "output.png"]

try:
    # Execute the command and capture stdout and stderr
    result = subprocess.run(command, capture_output=True, text=True)

    # Combine stdout and stderr for debugging purposes
    combined_output = f"STDOUT:\n{result.stdout}\n\nSTDERR:\n{result.stderr}"

    # Print stdout and stderr to the console for logging
    print(combined_output)

    # Write both stdout and stderr to output.txt
    with open(output_txt, "w") as f:
        f.write(combined_output)

except Exception as e:
    print(f"Error running CHOpt_linux: {e}")