import subprocess

proc = subprocess.Popen(['sleep', '10'])

while proc.poll() is None:
    print('작업중...')
    print(proc.poll())
    # 시간이 걸리는 작업을 수행한다.
