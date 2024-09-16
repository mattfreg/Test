import subprocess
import os
import stat

def run_chopt():
    # Define the path to 'chopt' in the same folder as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    chopt_path = os.path.join(script_dir, 'chopt')
    
    # Make 'chopt' executable
    try:
        # Change the file permission to make it executable
        os.chmod(chopt_path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
    except PermissionError:
        print("Error: Permission denied when trying to change file permissions.")
        return
    except FileNotFoundError:
        print("Error: 'chopt' executable not found at the specified path.")
        return
    except Exception as e:
        print(f"An error occurred while changing permissions: {e}")
        return
    
    # Define the command and argument
    command = [chopt_path, '-f', 'notes.mid']
    
    # Open the output file in write mode
    with open('output.txt', 'w') as file:
        try:
            # Run the command and capture the output
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            # Write the stdout and stderr to the file
            file.write(result.stdout)
            file.write(result.stderr)
            
            print("Output saved to 'output.txt'")
        except FileNotFoundError:
            print("Error: 'chopt' command not found. Please ensure it is installed and in your PATH.")
        except Exception as e:
            print(f"An error occurred while running 'chopt': {e}")

if __name__ == '__main__':
    run_chopt()