import sys
import os
from os import listdir, makedirs
from os.path import isfile, join
import hashlib
from PIL import Image
import datetime
from shutil import copyfile

def main():
    if len(sys.argv) == 3:
        firstFolder = getAllImageHashes(sys.argv[1])
        secondFolder = getAllImageHashes(sys.argv[2])
        printDifferences(firstFolder, secondFolder)
    elif len(sys.argv) == 2:
        folder = getAllImageHashes(sys.argv[1])
        printDifferences(folder, None)
    else:
        print("Improper arguments given")
        print("")
        print("Usage:")
        print("main.py <folder1> [folder2]")

def printDifferences(folder1, folder2):
    matchFound = False
    matchCount = 0
    imagesToDelete = []
    # Single folder
    # Only dissalow matching filenames if in the same directory
    if folder2 == None:
        # For reference: f1[0] gives filepath. f1[1] gives the image hash
        for f1 in folder1:
            # We don't want to compare an image after we have decided it is a duplicate
            compare = True
            for image in imagesToDelete:
                if f1[1] == image[1]:
                    compare = False

            if compare:
                for f2 in folder1:
                    if f1[1] == f2[1] and f1[0] != f2[0]:
                        matchCount += 1
                        matchFound = True
                        print("{\nMatch #" + str(matchCount) + " found: ")
                        print("\t" + f1[0])
                        print("\t" + f2[0])
                        print("\nDeleting " + f2[0])
                        print("}")
                        imagesToDelete.append(f2)
                        
    # Two folder compare             
    else:
        for f1 in folder1:
            for f2 in folder2:
                if f1[1] == f2[1]:
                    matchCount += 1
                    matchFound = True
                    processMatchedImages(f1, f2, matchCount)

    # Now delete the images
    for image in imagesToDelete:
        if os.path.exists(image[0]):
            os.remove(image[0])
        else:
            print("The file does not exist")


    if not matchFound:
        print("No matches found!")

def processMatchedImages(img1, img2, matchCount):
    print("{\nMatch #" + str(matchCount) + " found: ")
    print("  " + img1[0])
    print("  " + img2[0])
    print("}")

def getOnlyFilename(fullpath):
    return fullpath.split("\\")[-1]

def getAllImageHashes(folder):
    onlyfiles = [join(folder, f) for f in listdir(folder) if isfile(join(folder, f)) and not f.endswith(".ini") and not f.endswith(".db")]
    hashedFiles = []
    fileLength = len(onlyfiles)
    for f in onlyfiles:
        hashedFiles.append((f, dhash(Image.open(f))))
    print("Hashed all files from folder: "+ folder)
    return hashedFiles

def dhash(image, hash_size = 8):
    # Grayscale and shrink the image in one step.
    image = image.convert('L').resize(
        (hash_size + 1, hash_size),
        Image.ANTIALIAS,
    )

    pixels = list(image.getdata())

    # Compare adjacent pixels.
    difference = []
    for row in range(hash_size):
        for col in range(hash_size):
            pixel_left = image.getpixel((col, row))
            pixel_right = image.getpixel((col + 1, row))
            difference.append(pixel_left > pixel_right)

    # Convert the binary array to a hexadecimal string.
    decimal_value = 0
    hex_string = []
    for index, value in enumerate(difference):
        if value:
            decimal_value += 2**(index % 8)
        if (index % 8) == 7:
            hex_string.append(hex(decimal_value)[2:].rjust(2, '0'))
            decimal_value = 0

    return ''.join(hex_string)

if __name__ == '__main__':
    main()
