import os
import subprocess


def run_encypt(data):
    env = os.environ.copy()
    env['password'] = 'zf7ShyBhZ0raQDdE/2Q1Qg=='
    proc = subprocess.Popen(
        ['openssl', 'enc', '-des3', '-pass', 'env:password'],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )

    proc.stdin.write(data)
    proc.stdin.flush()
    return proc