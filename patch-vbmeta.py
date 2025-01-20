#!/usr/bin/env python

import os
import sys
import argparse

# Magic for the vbmeta image header
AVB_MAGIC = b"AVB0"
AVB_MAGIC_LEN = 4

# Information about the verification flags
FLAGS_OFFSET = 123
FLAGS_TO_SET = b"\x03"


def patch_vbmeta(file):
    # try reading the file with read/write to make sure it exists
    try:
        fd = os.open(file, os.O_RDWR)
    except OSError:
        sys.exit(f"Error reading file: {file}\nFile not modified. Exiting...")

    # making sure it's a vbmeta image by reading the magic bytes at the start of the file
    magic = os.read(fd, AVB_MAGIC_LEN)

    if magic != AVB_MAGIC:
        fd.close()
        sys.exit(
            "Error: The provided image is not a valid vbmeta image.\nFile not modified. Exiting..."
        )

    # set the disable-verity and disable-verification flags at offset 123
    try:
        os.lseek(fd, FLAGS_OFFSET, os.SEEK_SET)
        os.write(fd, FLAGS_TO_SET)
    except OSError:
        fd.close()
        sys.exit("Error: Failed when patching the vbmeta image.\nExiting...")

    # end of program
    os.close(fd)
    print("Patching successful.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Python script to patch Android vbmeta image file to disable verification flags"
    )
    parser.add_argument("filename", help="vbmeta image file to patch")

    args = parser.parse_args()

    patch_vbmeta(args.filename)
