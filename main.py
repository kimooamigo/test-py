# control_bot.py
import subprocess
import telebot
from threading import Thread
import time

def run_script(script_name):
  process = subprocess.Popen(["python3", script_name])
  return process


def stop_script(process):
  try:
    process.terminate()
    return True
  except Exception as e:
    print(f"An error occurred: {e}")
    return False


if __name__ == '__name__':
  server()
  
  print('welcome........')
  while True:
    process = run_script("/workspace/test-py/FreeMaxSCGN.py")
    print('Running FreeMaxSCGN.py...')
    time.sleep(700)
    process.terminate()
    print('قد تم إيقاف الاسكربت.')
