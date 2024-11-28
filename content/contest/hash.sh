# Hashes a file, ignoring all whitespace and comments. Use for
# verifying that C++ code was correctly typed.
cpp -dD -P -fpreprocessed | tr -d '[:space:]'| md5sum |cut -c-6
