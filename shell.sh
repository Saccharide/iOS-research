
key_word=$1
test -z $key_word && echo "Key word require." 1>&2 && exit 1
grep -rl "KEYWORD"  --exclude=shell.sh .  | while read -r line; do
    file_name="${line:2}" 
    grep -l $key_word $file_name 
done
