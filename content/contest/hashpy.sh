# Usage : cat fichier.py | hashpy.sh

cat - | grep -vE '^\s*(#|$)' | tr -d '[:space:]' | md5sum | cut -c-6