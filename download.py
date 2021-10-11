import os
import time
import urllib.request
from tqdm import tqdm

import argparse

def main(args):
    output_dir = args.output
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


    file1 = open(args.input, 'r')
    image_urls = file1.read().splitlines()

    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36', 
        'Accept-Language': 'en-US,en;q=0.8'
    }

    for i, url in enumerate(tqdm(image_urls)):
        
        #url = url.replace("?width=300", "")
        name = url.split("/")[-1]
        filename = os.path.join(output_dir, name)


        request_= urllib.request.Request(url,None,headers) #T he assembled request
        response = urllib.request.urlopen(request_) # store the response

        #create a new file and write the image
        image = response.read()
        with open(filename, "wb") as file:
            file.write(image)
        
        # delay to prevent API/download limit
        if ((i+1)%1000) == 0:
            time.sleep(args.delay)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Text files containing urls")
    
    # Adding optional argument
    parser.add_argument("-o", "--output", help="Output directory", default="images")
    parser.add_argument("-d", "--delay", help="Delay every 1000 downloads", default=60)

    
    # Read arguments from command line
    args = parser.parse_args()

    # calling the main function
    main(args)