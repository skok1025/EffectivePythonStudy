import subprocess

result = subprocess.run(['echo', '자식 프로세스에서 보내는 인사'], capture_output=True, encoding='utf-8')
result.check_returncode()

print(result.stdout)

proc = subprocess.Popen(['sleep', '1'])
while proc.poll() is None:
    print('작업중...')
print('종료 코드', proc.poll())