import time
from datetime import datetime
import os

current_path = os.getcwd()


while True:
    # Get the current date and time
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # # Append the current date and time and the word "test" to the file
    # with open("/local_output/hello_world.txt", "a") as file:
    #     file.write(f"{now} test\n")
        
    with open(current_path + "\hello_world.txt", "a") as file:
        file.write(f"{now} test\n")
    
    print(now)
    print(current_path)
    # Sleep for 1 minute
    time.sleep(60)
