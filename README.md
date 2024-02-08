# Random Photo Script

This script is made in Python and will display any random photo from a specified directory from your terminal. At the moment it uses
nsxiv as the image viewer but this can be easily changed to suit your preferences.

## Steps to install:
Clone this repository:
`git clone https://github.com/huds0/randomphotoscript.git`

Open the randomphotoscript.py file in an editor:

1. Change the `photo_directory = os.path.abspath("path/to/your/directory")` to the directory of the photos you want to display.
2. Specify your image viewer program you want to use: `subprocess.run(["NAME", photo_path])`
3. If required, change the file extensions that you want to display
4. Give the script an alias in your terminal config file ie.
   If you're using bash, in .bashrc file add:
   `alias alias_name="python path/to/randomphotoscript.py"`

## Dependencies
   - Python
   - Image viewer program (default config uses nsxiv)
  
## License
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
