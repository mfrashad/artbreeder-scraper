# Artbreeder Scraper
A script to scrape and download images from artbreeder.com

## Usage
### 1. Scrape URLs
To get the image urls, run `scrape.py`
```
python scrape.py -o urls.txt --iterations 100 --type anime_portraits
```
This will collect the anime portraits image urls by scrolling the site for 100 times.


Available image types are:
- general
- portraits_sg2
- landscapes_sg2_concept
- buildings
- paintings
- sci_bio_art
- characters
- albums
- furries
- anime_portraits


For more command line options, run `--help`
```
python scrape.py --help
```

### 2. Download Images
To download the images using the scraped url, run `download.py`
```
python download.py urls.txt --output images --delay 60
```
This will download urls in `urls.txt` and save it into `images` directory. It will also wait for 60 s every 1000 images to prevent API limit.

### 3. Expand Image to Square (Optional)
Some images are portrait or landscape. As the purpose of this script is to collect image for GAN training. You can run the following script to expand the image into a square.
```
python preprocess.py input_dir -o output_dir
```

## License
This project is under license from MIT. For more details, see the LICENSE file.


