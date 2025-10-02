Hi! This repository consists of a Python project I was working on, which works with linked lists that represent low-level memory blocks, with features like allocating certain
sizes of data into the blocks, freeing the blocks, merging freed blocks, and looking at some of their statistics.

To run this project load the main.py file and type in how much data you would like to free or alocate, along with whether or not you would like to see some of the statistics or
a display of each block's information.

Some examples of the output you should see are as following:

Enter command allocate 256
Allocated 256 bytes at address 0

Enter command allocate 128
Allocated 128 bytes at address 256

Enter command display
[Start: 0, Size: 256, Free: False]
[Start: 256, Size: 128, Free: False]
[Start: 384, Size: 640, Free: True]
[ALLOCATED: 384] [FREE: 640]

Enter command free 256
Freed memory at address 256

Enter command display
[Start: 0, Size: 256, Free: False]
[Start: 256, Size: 128, Free: True]
[Start: 384, Size: 640, Free: True]
[ALLOCATED: 256] [FREE: 768]

Enter command free 0
Freed memory at address 0

Enter command display
[Start: 0, Size: 1024, Free: True]
[ALLOCATED: 0] [FREE: 1024]

Enter command statistics
Percent Allocated: 0.00%, Percent Free: 100.00%

Enter command exit
Exiting memory manager.
