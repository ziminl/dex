import subprocess

adb_command = 'adb shell input text "Hello from Python"'

process = subprocess.Popen(adb_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

print(stdout.decode())
if stderr:
    print(f"Error: {stderr.decode()}")
