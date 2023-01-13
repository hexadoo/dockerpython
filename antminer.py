
import datetime
import git
import time

repo = git.Repo.init('https://hexadoo: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@github.com/hexadoo/dockerpython.git')

while True:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('time.txt', 'a') as f:
        f.write(current_time + '\n')
    repo.git.add('hello_world.txt')
    repo.git.commit(m='Added current time')
    repo.git.push()
    time.sleep(60)
