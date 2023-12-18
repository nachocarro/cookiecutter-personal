import subprocess  #llama a la terminal

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

subprocess.call(['git', 'init'])   #inicia el repositorio
subprocess.call(['git', 'add', '*'])   #va a agregar todos los archvios que se encuentren en ese momento
subprocess.call(['git', 'commit', '-m', 'Initial commit']) #hace el primer commit

print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")