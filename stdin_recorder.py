# Matthew Davis
# Task: Create script that reads from stdin and writes to a file
import sys
log = open('stdin_log.txt','w')		# Creates file for writing
while 1:
	try:
		line = sys.stdin.readline()	# Reads stdin
	except KeyboardInterrupt:		# Stops reading when Ctrl-C is pressed
		break

	if not line:					# Stops reading if line is empty
		break

	log.write(line)					# writes stdin line to the file
log.close()