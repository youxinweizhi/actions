/*
 * This file is part of the MicroPython project, http://micropython.org/
 *
 * Development of the code in this file was sponsored by Microbric Pty Ltd
 *
 * The MIT License (MIT)
 *
 * Copyright (c) 2013-2016 Damien P. George
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

#include "py/builtin.h"

const char esp32_help_text[] =
    "Welcome to MicroPython on the ESP32!\n"
    "\n"
    "Basic smartconfig configuration\n"
    "\n"
    "None\n"
    "\n"
    "Basic Espnow configuration:\n"
    "\n"
    "from espnow import ESPNOW\n"
    "from machine import Pin\n"
    "\n"
    "#key callback\n"
    "def button_callback(pin_instance:Pin):\n"
    "    simple.send_message(simple.BROADCAST_MAC, b'toggle_led')\n"
    "\n"
    "#espnow callback\n"
    "def espnow_callback(mac,message):\n"
    "    if message == b'toggle_led':\n"
    "        led.value(not led.value())\n"
    "\n"
    "#key\n" 
    "button = Pin(9, Pin.IN, Pin.PULL_UP)\n"
    "button.irq(button_callback, Pin.IRQ_RISING)\n"
    "\n"
    "#LED\n"
    "led = Pin(3, Pin.OUT, value=0)\n"
    "\n"
    "#espnow\n"
    "simple = ESPNOW(callback=espnow_callback\n"
    "\n"
    "Control commands:\n"
    "  CTRL-A        -- on a blank line, enter raw REPL mode\n"
    "  CTRL-B        -- on a blank line, enter normal REPL mode\n"
    "  CTRL-C        -- interrupt a running program\n"
    "  CTRL-D        -- on a blank line, do a soft reset of the board\n"
    "  CTRL-E        -- on a blank line, enter paste mode\n"
    "\n"
    "For further help on a specific object, type help(obj)\n"
    "For a list of available modules, type help('modules')\n"
;
