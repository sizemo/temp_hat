# The Temp Hat
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
Our `boot.py` is set up to be writable by the computer if you just plug it in via the USB-C port on the board. However, when the computer can write to the board, CircuitPython can't write data to the onboard flash memory. Because this Feather doesn't have extra buttons that you can use to switch modes, you have to ground the A0 pin while it's plugged into power and then press the Reset button to switch modes. 

Since it took me way too long for me to figure this out, if you don't have the male headers soldered in already, you can just take one end of a M/M jumper wire and put it through the GND pin hole and put the other end in the A0 hole and that's how you ground the A0 pin.

You should see the LED by the battery port go red for one second and then turn off. That means the data is logging. That LED should flash for one second every 60 seconds just to let you know it's still going.

I've got it set to record the temperature every 60 seconds because I'm planning on using it for about an hour at a time and I don't think I need to have data too much more granular than that, but you can change that by changing `time.sleep(60)` to whatever you want. Just also change `time_from_start += 60` to the correct interval as well.

## Stop logging data
Press the reset button again without grounding the A0 pin, or remove the power source.

## Checking the data
Plug it back in after getting out of the data logging mode. All of the data should be recorded in `temperature.txt`. I have it set up to just log temperature in Fahrenheit, humidity percentage, and time since the start of the recording. I have pressure in the code but decided not to log it.

You should be able to use that file as a csv for analysis.

# Outstanding issues

### Temperature is precise but not accurate
Because the temperature sensor is right next to the CPU, when the CPU heats up, the sensor reads incorrectly high temperatures. I got this particular board because I thought it would be easier to not use an external module, but that does not seem like it's going to be something I can rely on without modifications.

I see two possible paths:
  1. Use a static correction variable in the code to reduce the temperature that gets written to `temperature.txt` is more correct.
  2. Connect an external BME280 to the Feather via the JST port and pull the readings from there.

I'd prefer to use an external sensor because it's probably more correct in different environments and that's the point of this whole project.

### It's supposed to clip to a hat and there's nothing about that in here yet
Okay yeah, still working on that. I want to get the code working before I strap this thing to a tie clip or binder clip or something.

# Thank Yous

A couple of resources I pulled heavily from in putting this together:
1. [@crwilcox](https://github.com/crwilcox)'s writeup of his [similar project](https://chriswilcox.dev/blog/2020/11/17/Collecting-temperature-data-with-CircuitPython.html) with a different board
2. [The official Adafruit product guide](https://learn.adafruit.com/adafruit-esp32-s2-feather/storage)
3. I'm not really sure who's responsible, but whoever [created](https://github.com/tuupola/circuitpython/blob/master/examples/SDdatalogger/boot.py) nearly the only `boot.py` on the internet that doesn't use grounding a pin as a mode switcher, which helped me understand how the whole thing worked. I might try a variation of this in a later version and I never would have understood how to do it without this.
