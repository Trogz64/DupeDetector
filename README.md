# DupeDetector
Finds any duplicate images in 1 or 2 directories

- Deletes duplicate images (keeping first image) when input is 1 directory

- Displays duplicate image filenames when input is 2 directories

### Usage

```bash
    python main.py "dir1"
```

Or

```bash
    python main.py "dir1" "dir2"
```

**dir1 is always required**

If dir2 isn't specified, the directory will be compared against itself.

Program currently works for the following file extensions:

- .jpg
- .jpeg
- .png
- .gif

### Tip:

If you only want to display matches, and not delete them, compare the directory to itself using the two directory method
