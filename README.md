# BLEper
BLEper is a small python script that takes a BLE (Bluetooth Low Energy) device and plays a .wav file until in range of your dongle. 
I used the default wav file included by default in many Linux distros. Users can change it to whatever. 

## Requirements
- pygatt lib (https://github.com/peplin/pygatt)
- *nix flavour os 

## How to run it
```sh
sudo python BLEper.py 'bd_addr'
```
### Click on the image to see it in action:

[![BLEper working on a BLE device - Click to Watch!](https://i.imgur.com/OVPgz2l.png)](https://www.youtube.com/watch?v=C9u31OazI20 "BLEper working on a BLE device - Click to Watch!")

![Example device](https://i.imgur.com/eFIxjqy.jpg)

- Raspberry PI2
- Raspbian
- BLE dongle
- Powerbank
- Cheap output speaker (the pirate thing)

## License
Copyright (c) 2018 David Sopas

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
