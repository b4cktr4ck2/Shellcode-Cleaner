#!/bin/bash
if [[ $EUID -ne 0 ]]; then
   printf "Need to be root- Try Harder ;)"
   exit 1
fi
cp shellcode-cleaner.py /usr/share/
printf "#!/bin/bash \n" > /usr/bin/shellcode-cleaner
echo "cd /usr/share/shellcode-cleaner/ && ./shellcode-cleaner.py" >> /usr/bin/shellcode-cleaner
cp /usr/bin/shellcode-cleaner /usr/local/bin
chmod 744 /usr/local/bin/shellcode-cleaner
