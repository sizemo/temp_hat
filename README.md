# temp_hat
Temp Hat: A portable temperature measurement device using the Adafruit ESP32-S2 Feather with BME280

## Why tho?

Official weather measurements are supposed to be taken in the shade. When your weather person on the news tells you the temperature, it's not the temperature that you're going to feel in direct sun on a concrete sidewalk. You're going to be in higher temperatures than that. I wanted to know what kind of temperatures I'm actually running in by measuring with a portable temperature sensor that I can clip on to my hat while I'm out there.

## Hardware
* [Adafruit ESP32-S2 Feather with BME280](https://www.adafruit.com/product/5303)
* Some kind of Adafruit-compatible LiPo battery (ex: https://www.microcenter.com/product/503621/adafruit-industries-lithium-ion-battery-37v-2000mah)

## Steps
1. [Follow these steps to flash the board with the bootloader](https://learn.adafruit.com/adafruit-esp32-s2-feather/install-uf2-bootloader)
2. [You should probably download the Mu editor if you don't already have it](https://learn.adafruit.com/adafruit-esp32-s2-feather/installing-mu-editor)
3. [You could also read this if you want to understand the basics of how to update the files on the board](https://learn.adafruit.com/adafruit-esp32-s2-feather/the-circuitpy-drive)
4. Make sure the board is plugged in and showing up as CIRCUITPY in your computer. Copy `boot.py` over from this repo and then either replace the `code.py` file with the one from here or copy and paste the code from that file in this repo into the existing `code.py` file on the board.

## Start logging data

