# Matthew Davis
# Task: Create script that reads from stdin and writes to a file
import sys

with open('stdin_log.txt', 'w') as log:
    while 1:
        try:
            line = sys.stdin.read(1048576)  # Reads stdin up to 1 MB
            if not line:  # Stops reading if line is empty
                break
            log.write(line)  # writes stdin line to the file
            log.flush()
        except KeyboardInterrupt:  # Stops reading when Ctrl-C is pressed
            break
