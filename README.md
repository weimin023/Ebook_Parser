# Ebook_Parser (doc88.com)
### Ebook downloader v1_2023.08.14
```
usage: main.py [-h] [-link LINK] [-begin BEGIN] [-end END]
-h, --help    show this help message and exit
-link LINK    Link to the book (doc88.com)
-begin BEGIN  Starting page number
-end END      Ending page number
```
```
terminal> python main.py -link <BOOK_LINK> -begin 1 -end 10
```
> Page 1~10 will be dowloaded.
### Save2PDF with Pixel Restoration v1_2023.08.14
```
usage: sr_script.py [-h] [-path PATH] [-sr SR] [-compress COMPRESS]
-h, --help          show this help message and exit
-path PATH          Path to the images
-sr SR              Image super resolution
-compress COMPRESS  Image size compression
```
```
terminal> python sr_script.py -path <IMG_PATH> -sr 1 -compress 1
```
> result.pdf will be placed at ./processed
