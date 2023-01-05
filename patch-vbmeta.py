import os
import sys

# Magic for the vbmeta image header
AVB_MAGIC = b"AVB0"
AVB_MAGIC_LEN = 4

# Information about the verification flags
FLAGS_OFFSET = 123
FLAGS_TO_SET = b'\x03'


### main program

# if an argument is not provided
if len(sys.argv) != 2:
    sys.exit("Usage: python ./" + os.path.basename(__file__) + " <vbmeta-image>")

# try reading the file with read/write to make sure it exists
FILE = sys.argv[1]

try:
    fd = os.open(FILE, os.O_RDWR)
except OSError:
    sys.exit("Error reading file: " + FILE + ". File not modified. Exiting...")

# making sure it's a vbmeta image by reading the magic bytes at the start of the file
magic = os.read(fd, AVB_MAGIC_LEN)

if (magic != AVB_MAGIC):
    fd.close()
    sys.exit("Error: The provided image is not a valid vbmeta image. File not modified. Exiting...")

# set the disable-verity and disable-verification flags at offset 123
try:
    os.lseek(fd, FLAGS_OFFSET, os.SEEK_SET)
    os.write(fd, FLAGS_TO_SET)
except OSError:
    fd.close()
    sys.exit("Error: Failed when patching the vbmeta image. Exiting...")

# end of program
os.close(fd)
print("Patching successful.")