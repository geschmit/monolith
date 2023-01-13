# Monolith: because it's now apparently 2077

## What is this?
This is the source code for a Google Glass-like visor goggle, dubbed Monolith. You can think of it as one of those fancy visor things the techy people have in those really hollywood films when they're hacking the thing and doing the thing and, uhh... you get the idea.

## Why is this?
I made this out of boredom, and perhaps because I possibly wish to actually build this piece of hardware someday, if I can fund it!

## How is this?
This project utilizes these things:
- A RPi 4b+
- [A NoIR camera](https://www.adafruit.com/product/3100) to track thing in the visible frame
- One of these [Vufine](https://www.amazon.com/Vufine-006011-Wearable-Display/dp/B01MZ89QXF/) displays connected to said RPi
- A custom-made glove controller running off of an [Adafruit Feather nRF Sense](https://www.adafruit.com/product/4516), plus some other stuff
- A [speaker bonnet](https://www.adafruit.com/product/3346) and [bone transducers](https://www.adafruit.com/product/1674) to enable audio
- A cool hat to hook and install this on
- Some glasses
- someone with a lot bigger income than me to pay for all of this lmao

## When is this?
As of now, my goals are, as followed;

### Basics
- [ ] Basis firmware to interface w/ camera and display video feed
- [ ] Basic inputs from nRF via BLE and accelerometer to enable UI selection, etc
- [ ] Built-in modules to make use of the camera(facial detection, webcam streaming, youtube video lookup)

### Additions
- [ ] Integration with [something like this](https://www.adafruit.com/product/1070) to enable index control
- [ ] External module loading via USB(load on-the-go & hotswap features, etc)
- [ ] I2C module integration(use stuff like an [air quality sensor](https://www.adafruit.com/product/3709) or a [mini esp chip](https://www.adafruit.com/product/5405))

## Can is this?
If you do want to make this project for yourself, please make sure to credit me(@geschmit on GitHub) somewhere on social media. Everything is licensed under GNU GPL v3, unless otherwise noted.
