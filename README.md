# <img src="logo.svg" width="48px" height="48px" alt="logo"> vbmeta Patch Script

A Python port of https://github.com/libxzr/vbmeta-disable-verification to patch Android vbmeta image file to disable verification flags

## Why

This script patches the vbmeta.img image file by setting the disable-verity flag and the disable-verification flag in the vbmeta.img file. While the same thing is done by the `fastboot --disable-verity --disable-verification flash vbmeta vbmeta.img` command, it does not produce a local file. Thus, if you wish to flash the vbmeta.img file using other methods (for example, using SP Flash Tool), you'd probably want a local vbmeta.img file.

While the original repo is functional, the prebuilt binary is only available for Linux platforms like GNU/Linux and Android. Therefore, this Python script is created to make it cross-platform. It also serves as a little exercise for me to try writing more Python code.

Other than that, I've created this repository to document how patching out verity/verification on a local vbmeta file works. As all the sources I've found on this topic are only in Chinese, I hope this repo serves as a short documentation/translation/conclusion of existing knowledge.

## Credits

Credits to [@libxzr](https://github.com/libxzr) for creating the [original repo](https://github.com/libxzr/vbmeta-disable-verification) and [the blog post about patching vbmeta.img](https://blog.xzr.moe/archives/226/).
