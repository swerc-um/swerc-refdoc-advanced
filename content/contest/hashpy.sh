#!/bin/bash

# Read from standard input (e.g., piped content)
cat - | grep -vE '^\s*(#|$)' | tr -d '[:space:]' | md5sum | cut -c-6