# Matthew Davis
# Task: Create script that reads from stdin and writes to a file
import sys
import os
import unittest
import filecmp

def recorder(fd):
    with open('stdin_log.txt', 'w') as log:
        while 1:
            try:
                line = os.read(fd, 1)  # Reads up to 4KB at a time
                print('\nRead line: '+line) # Printing to see 'line' value each iteration
                if not line:  # Stops reading if line is empty
                    break
                log.write(line)  # writes line to the file
            except KeyboardInterrupt:  # Stops reading when Ctrl-C is pressed
                print('\nEntered except') # Printing to show entering 'except' section
                break

def main():
    fn=sys.stdin.fileno()
    recorder(fn)


class Test(unittest.TestCase):

    def check_equivalence(self, test, log): # Reads files and checks for equality 
        while 1:
            in_line = os.read(test, 1024*4)
            log_line = os.read(log, 1024*4)
            if not in_line or not log_line:
                break
            self.assertEqual(in_line, log_line)

    def test_written_file(self):    # Uses english text test file
        test_file = os.open('moby.txt', os.O_RDONLY)
        recorder(test_file)
        same = filecmp.cmp('moby.txt','stdin_log.txt', False)
        self.assertTrue(same)

    def test_empty_file(self):      # Uses empty .txt test file
        test_file = os.open('empty.txt', os.O_RDONLY)
        recorder(test_file)
        same = filecmp.cmp('empty.txt','stdin_log.txt', False)
        self.assertTrue(same)

    def test_numeric_file(self):    # Uses 1 GB .txt file with only 0's
        test_file = os.open('zeros.txt', os.O_RDONLY)
        recorder(test_file)
        same = filecmp.cmp('zeros.txt','stdin_log.txt', False)
        self.assertTrue(same)

    def test_binary_file(self):     # Uses .txt file generated by "dd if=/dev/urandom bs=1024k count=1 > binary.txt"
        test_file = os.open('binary.txt', os.O_RDONLY)
        recorder(test_file)
        same = filecmp.cmp('binary.txt','stdin_log.txt', False)
        self.assertTrue(same)

#if __name__ == '__main__':          # Runs Test
#    unittest.main()

main()
