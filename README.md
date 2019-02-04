# Shellcode Cleaner
I got sick of having to remove junk from my shellcode so I made a script to just clean it all for me.

## Usage

(If installed): shellcode-cleaner [-hnqrxs]

(If standalone script): python shellcode-cleaner.py [-hnqrxs]

Running the tool with no arguments will prompt you to paste your shellcode in and will strip it completely of newlines, quotation marks (single AND double), semicolons, and the "\r" as well as "\x" escape character.

## Flags
-h: Display the help

-n: Strip newline "\n" characters

-q: Strip quoation marks- single and double

-r: Strip "\r" characters

-x: Strip "\x" escape characters

-s: Strip semicolons ";"

Multiple flags can be set allowing you to customize the output however you like.

## Example
Shellcode taken from: https://packetstormsecurity.com/files/102847/All-Windows-Null-Free-CreateProcessA-Calc-Shellcode.html for demo purposes.

Remove newlines, "\r", quotations, and semicolons but keep the "\x":

shellcode-cleaner -nrqs

Tool will prompt you to paste your shellcode. Do so, then hit Control + D.

### It will turn THIS:
  "\x31\xdb\x64\x8b\x7b\x30\x8b\x7f"
        "\x0c\x8b\x7f\x1c\x8b\x47\x08\x8b"
        "\x77\x20\x8b\x3f\x80\x7e\x0c\x33"
        "\x75\xf2\x89\xc7\x03\x78\x3c\x8b"
        "\x57\x78\x01\xc2\x8b\x7a\x20\x01"
        "\xc7\x89\xdd\x8b\x34\xaf\x01\xc6"
        "\x45\x81\x3e\x43\x72\x65\x61\x75"
        "\xf2\x81\x7e\x08\x6f\x63\x65\x73"
        "\x75\xe9\x8b\x7a\x24\x01\xc7\x66"
        "\x8b\x2c\x6f\x8b\x7a\x1c\x01\xc7"
        "\x8b\x7c\xaf\xfc\x01\xc7\x89\xd9"
        "\xb1\xff\x53\xe2\xfd\x68\x63\x61"
        "\x6c\x63\x89\xe2\x52\x52\x53\x53"
        "\x53\x53\x53\x53\x52\x53\xff\xd7";
        
### INTO THIS:
 
\x31\xdb\x64\x8b\x7b\x30\x8b\x7f\x0c\x8b\x7f\x1c\x8b\x47\x08\x8b\x77\x20\x8b\x3f\x80\x7e\x0c\x33\x75\xf2\x89\xc7\x03\x78\x3c\x8b\x57\x78\x01\xc2\x8b\x7a\x20\x01\xc7\x89\xdd\x8b\x34\xaf\x01\xc6\x45\x81\x3e\x43\x72\x65\x61\x75\xf2\x81\x7e\x08\x6f\x63\x65\x73\x75\xe9\x8b\x7a\x24\x01\xc7\x66\x8b\x2c\x6f\x8b\x7a\x1c\x01\xc7\x8b\x7c\xaf\xfc\x01\xc7\x89\xd9\xb1\xff\x53\xe2\xfd\x68\x63\x61\x6c\x63\x89\xe2\x52\x52\x53\x53\x53\x53\x53\x53\x52\x53\xff\xd7

Now you can paste it into your exploit without needing to organize it further.
Please report any issues and I'll do my best to fix.

## License

It's under GNU/GPL v3, so have at it. 
