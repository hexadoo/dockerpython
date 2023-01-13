
import datetime
import git
import time

repo = git.Repo('https://github.com/hexadoo/dockerpython.git')

while True:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('time.txt', 'a') as f:
        f.write(current_time + '\n')
    repo.git.add('hello_world.txt')
    repo.git.commit(m='Added current time')
    repo.git.push()
    time.sleep(60)
