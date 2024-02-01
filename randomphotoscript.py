import os
import random
import subprocess

photo_directory = os.path.abspath("/home/hud/Pictures/Cats")

def display_random_photo(directory):
    photos = [f for f in os.listdir(directory) if f.endswith(('.jpg', '.jpeg', '.png', '.gif', '.heic', '.JPEG', ".JPG"))]
    if photos:
        random_photo = random.choice(photos)
        photo_path = os.path.join(directory, random_photo)
        subprocess.run(["nsxiv", photo_path])
    else:
        print("No photos found in the specified directory.")


if __name__ == "__main__":
    display_random_photo(photo_directory)


