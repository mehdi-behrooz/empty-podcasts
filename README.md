## Introduction
There are many different ways to arrange your podcasts based on topics, languages, etc. Using blank logos as separators to create spaces between your podcasts in 
[Pocket Casts](https://play.google.com/store/apps/details?id=au.com.shiftyjelly.pocketcasts)'s grid layout is by far
the dumbest way. The goal of this script is to generate fake empty podcasts with blank logos.

## Usage
For the white and black themes, there are already two predefined logos. You are free to use other logos based on your preferences. 

```
python3 generate.py --number 20 --logo white --output-directory dist/
python3 generate.py --number 20 --logo black --output-directory dist/
python3 generate.py --number 20 --logo https://my.custom.logo/url dist/ 
python3 generate.py --help
```


