import os
from PIL import Image
from tqdm import tqdm
import argparse

def expand2square(pil_img, background_color):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result

def main(args):
    input_dir = args.input
    output_dir = args.output
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filenames = os.listdir(input_dir)
    for filename in tqdm(filenames):
        im = Image.open(os.path.join(input_dir, filename))
        im_new = expand2square(im, (255, 255, 255))
        im_new.save(os.path.join(output_dir, filename))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    # Adding optional argument
    parser.add_argument("input", help="input directory")
    parser.add_argument("-o", "--output", help="output directory", default="preprocessed")

    
    # Read arguments from command line
    args = parser.parse_args()
    # calling the main function
    main(args)
