# below conversions are supported currently
 - png -> jpeg (vice-versa)

# How To Install
``` 
git clone https://github.com/git-pixel22/pixelconvert.git
```
```
cd pixelconvert
```
```
sudo pip install .
```

Note: On Linux or MacOS, if you do pip install as a normal user (without sudo), the executable command-line tool should be installed to the $HOME/.local/bin directory. If you haven’t added this directory path to the system $PATH environment variable, the chance is that you cannot find the `pixelconvert` command. (`which pixelconvert` command will also return an empty string.)

# Usage
``` 
pixelconvert <image-path> <format-to-convert-to>
```

# Example
```
pixelconvert imageName.png jpeg
```
``` 
pixelconvert imageName.jpeg png
```
