import subprocess
import os
import shutil

# Define file paths
output_txt = "test/output.txt"
notes_file = "notes.mid"
output_png = "output.png"
chopt_executable = "./CHOpt_linux"

# Create test directory if not exists
if not os.path.exists("test"):
    os.makedirs("test")

# Run the CHOpt_linux application
command = [chopt_executable, "-f", notes_file]

try:
    # Execute command and capture output
    result = subprocess.run(command, capture_output=True, text=True)

    # Save terminal output to .txt file
    with open(output_txt, "w") as f:
        f.write(result.stdout)

    # Move the generated .png file (assumed to be output.png)
    if os.path.exists(output_png):
        shutil.move(output_png, "test/output.png")

except Exception as e:
    print(f"Error running CHOpt_linux: {e}")