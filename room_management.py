#!/usr/bin/env python
# encoding:utf-8
#
# Copyright 2015-2017 Yoshihiro Tanaka
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__Author__ =  "Yoshihiro Tanaka"
__date__   =  "2015-01-20"

import time
import cv, cv2
import numpy as np
import Adafruit_BBIO.GPIO as GPIO


def takePicture(folder):
    code = "-".join([str(r) for r in list(time.localtime())])
    capture = cv2.VideoCapture(0)
    capture.set(cv.CV_CAP_PROP_FRAME_WIDTH, 320)
    capture.set(cv.CV_CAP_PROP_FRAME_HEIGHT, 240)
    time.sleep(0.1)
    ret, img = capture.read()
    if ret:
        cv2.imwrite(folder + "/" + code + ".png", img)

def buttonCheck():
    GPIO.setup("P9_15", GPIO.IN)
    GPIO.setup("P9_12", GPIO.IN)

    once = True
    while True:
        try:
            if GPIO.input("P9_12"):
                once = True
            else:
                if once:
                    takePicture("in")
                    once = False

            if GPIO.input("P9_15"):
                once = True
            else:
                if once:
                    takePicture("out")
                    once = False
        except KeyboardInterrupt:
            break
    GPIO.cleanup()

if __name__ == '__main__':
    buttonCheck()
