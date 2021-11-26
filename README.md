# Fight Lights Pico
Fight Lights Pico is a LED-Driver for the Raspberry Pi Pico that gives Arcade Stick modders the neccessary software to implement beautiful RGB LEDs for their projects

# What does it do?

This project is aimed for Arcade stick modders to add custom RGB LEDs to Arcade sticks. The LEDs react to button presses and display custom colors and animations.
The code is easily customizable to help you build the Arcade stick of your dreams.
This code is not limited to Arcade stick projects though, it can be used for any project that needs to light up LEDs when pressing something.


# How does it look?

I have made a short video showcasing some of the features to give you an idea on how it may look in the end:
https://www.youtube.com/watch?v=nG0_0xVvnjk

Reddit user u/mad_max206 has also build this project for his Qanba Obsidian, you can see his result here: https://www.reddit.com/r/fightsticks/comments/qhtwi9/qanba_obsidian_led_mod/

# Requirement

If you want to use this you will need a Raspberry Pi Pico and a RGB LED-Strip with individually adressable LEDs known as Neopixel or WS2812/WS2812b/WS2812e

# Guide

I have written a complete guide for assembly and installation here: https://docs.google.com/document/d/1qY4HESYdRyFT8OaB5leyHsWm4kfqoA74zqSLAdihuvo/edit?usp=sharing

The guide may make the impression that you can only build this with a Brook fighting board, but this is not the case. This code runs standalone on the pico and only
uses the brook fighting board as a means to get the signals from the buttons to the pico and to power the Pico together with the LEDs. I have chosen to write the guide
with a brook fighting board in mind, since it is a very common fighting board, with great compatability and all the neccessary pins for this project, and thus makes it
very easy for begginers to follow and realize.
So as long as you can send the signals of your buttons to the pico, by whatever means you like, directly or through a different pcb,
and have a way to power the Pico and the LEDs, a brook board is not required.

# Contact

There is a Discord Server for all your questions: https://discord.gg/AyYfbYQt

# License

MIT License

Copyright 2021 Daora

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
