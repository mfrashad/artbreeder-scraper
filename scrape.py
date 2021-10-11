import time
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from webdriver_manager.chrome import ChromeDriverManager
from tqdm import tqdm

import argparse

def main(args):
    # Change to the path in your file
    # Eg. PATH_TO_CHROMEDRIVER_EXE = "D:\Downloads\Compressed\chromedriver_win32\chromedriver.exe"

    ##### Web scrapper for infinite scrolling page #####
    if args.driver:
        driver = webdriver.Chrome(executable_path=args.driver)
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get("https://www.artbreeder.com/browse")
    time.sleep(2)  # Allow 2 seconds for the web page to open

    driver.find_element_by_css_selector(f"div[data-name={args.type}]").click()
    time.sleep(1)

    scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
    screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
    i = 1

    pbar = tqdm(total = args.iterations)
    pbar.update(1)
    while i < args.iterations:
        # scroll one screen height each time
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
        i += 1
        if (i % 100) == 0:
            print(i)
        time.sleep(scroll_pause_time)
        pbar.update(1)
        # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
        scroll_height = driver.execute_script("return document.body.scrollHeight;")
        
        # Break the loop when the height we need to scroll to is larger than the total scroll height
        if (screen_height) * i > scroll_height:
            # time.sleep(5)
            break
    pbar.close()
    elements = driver.find_elements_by_css_selector(".main_image")
    image_urls = []
    for e in elements:
        image_url = e.get_attribute('style').split('"')[1].replace("_small", "")
        image_urls.append(image_url)

    with open(args.output, "w") as output:
        for row in image_urls:
            output.write(str(row) + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    # Adding optional argument
    parser.add_argument("-o", "--output", help="Output filename", default="urls.txt")
    parser.add_argument("-t", "--type", help="Image type", required=True, choices=["general", "portraits_sg2", "landscapes_sg2_concept", "buildings", "paintings", "sci_bio_art", "characters", "albums", "furries", "anime_portraits"])
    parser.add_argument("-i", "--iterations", help="Scrolls iterations", type=int, default=1000)
    parser.add_argument("-d", "--driver", help="Chrome driver path", default=None)

    
    # Read arguments from command line
    args = parser.parse_args()
    # calling the main function
    main(args)