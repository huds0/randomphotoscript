# Random Photo Script

This script is made in Python and will display any random photo from a specified directory. At the moment it uses
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
  
