#!/usr/bin/env python3
from wand.image import Image

def create_text(text, text_color='#fff'):
    '''Creates an image using a spritefont from a string.'''
    text = text.replace(' ', '_').lower()

    textImage = Image()
    for c in text:
        # For every character in the string, append the right spritefont to the sequence of frames
        textImage.sequence.append(Image(filename='font/font-{0}.png'.format(c)))

    # Draw out every frame in the sequence side by side
    textImage.concat()

    # Apply the specified color to the whole text sprite, with no transparency
    textImage.colorize(color=text_color, alpha='#fff')
    return textImage

def generate_image(english_name, latin_name, bee_color, scale=1):
    '''Creates the final bee image using the specified strings and colors by compositing everything onto the background image.'''
    sd_bee = Image(filename='sp_bee_{0}.png'.format(english_name))
    hd_bee = Image(filename='sp_bee_{0}_hd.png'.format(english_name))

    with Image(filename='background.png') as background:
        background.composite(sd_bee, left=40, top=67)
        background.composite(hd_bee, left=27, top=20)

        latin = create_text(latin_name, '#a8a6a5')
        background.composite(latin, left=4, top=4)
        
        english = create_text(english_name + ' bee', bee_color)
        background.composite(english, left=4, top=9)

        background.resize(background.width * scale, background.height * scale, filter='point')
        background.save(filename=english_name + '.png')

def main():
    # Generate an image for the common bee using scale 4
    generate_image('common', 'apis communia', 'rgb(216, 171, 65)', 4)

main()