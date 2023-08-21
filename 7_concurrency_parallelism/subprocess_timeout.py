import subprocess

proc = subprocess.Popen(['sleep', '10'])
try:
    proc.communicate(timeout=1)
except subprocess.TimeoutExpired:
    proc.terminate()
    proc.wait()

print('종료 코드', proc.poll())