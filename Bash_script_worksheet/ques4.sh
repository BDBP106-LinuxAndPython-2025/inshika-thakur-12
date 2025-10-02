#!/bin/bash

#List the contents of the current directory and also the name and size of the largest file.

ls -lS | grep "^-" | head -n 1
