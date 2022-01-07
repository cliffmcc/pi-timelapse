## Copyright (c) 2022 Cliff McCollum

from time import gmtime, strftime, sleep
import os
import click

from picamera import PiCamera

camera = PiCamera()

def start_camera():
    camera.resolution = (1280, 720)
    camera.vflip = True

def end_camera():
    camera.close()

def get_camera_image(file_object):
    camera.capture(file_object, format='jpeg')

def get_file_name(base):
    return "{}{}".format(base, strftime("%d-%m-%Y -- %H-%M-%S", gmtime()))

@click.command()
@click.option('--delay', default=300, help='Number of seconds between images. Default: 300.')
@click.option('--prefix', default='pics-', help='folder name prefix. Default: pics-')
def start(delay, prefix):
    new_folder_name = get_file_name(base=prefix)
    os.mkdir(new_folder_name)

    start_camera()
    while True:
        picture_name = "{}.jpg".format(get_file_name("{}/".format(new_folder_name)))
        with open(picture_name, 'wb') as outfile:
            get_camera_image(outfile)
        sleep(delay)


if __name__ == '__main__':
    start()
