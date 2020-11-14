# DupeDetector
Finds any duplicate images in 1 or 2 folders

- Deletes duplicate images (keeping first image) when input is 1 folder

- Displays duplicate image filenames when input is 2 folders

### Usage

```bash
    python main.py <folder1> [folder2]
```

**folder1 is always required**

If folder2 isn't specified, the folder will be compared against itself.

Currently only works if images are in the folder; no video files.

### Tip:

If you only want to display matches, and not delete them, compare the folder to itself using the two input folder method
