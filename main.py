# Zip file contains some folders with images. You should convert all images from each folder to pdf and save it
# in the same folder with the same name as folder. For example, if you have folder "images" with images "1.jpg", "2.jpg"
# and "3.jpg", you should convert them to pdf and save it as "images.pdf". You should do this for all folders in zip file.

import os
import sys
import zipfile
from PIL import Image


def convert_to_pdf(image_list, pdf_name):
    # image_list.sort()
    im_list = []
    for image in image_list:
        im_list.append(Image.open(image))
    im_list[0].save(pdf_name, "PDF", resolution=100.0, save_all=True, append_images=im_list[1:])


def convert_images_in_folder_to_pdf(folder, filename: str):
    print(folder)
    image_list = []
    for file in os.listdir(folder):
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
            image_list.append(os.path.join(folder, file))
    if not filename.endswith(".pdf"):
        filename += ".pdf"
    convert_to_pdf(image_list, filename)


def main():
    # filename isfirst argument from command line
    filename = sys.argv[1]
    if filename.endswith(".zip"):
        filename = filename[:-4]
    zip_file = zipfile.ZipFile(filename + ".zip")
    zip_file.extractall(f"{filename}_images/")
    zip_file.close()
    for folder in os.listdir(f"{filename}_images/"):
        if os.path.isdir(f"{filename}_images/{folder}"):
            convert_images_in_folder_to_pdf(os.path.join(f"{filename}_images/", folder), f"{filename}_{folder}")


if __name__ == "__main__":
    main()
