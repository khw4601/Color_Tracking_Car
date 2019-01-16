#! /usr/bin/python

#################################################################################
# Copyright 2018 NTREX CO.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#################################################################################

# Authors: HeungSi #
# Date   : 16/03/2019
# Usage  : python follower_car.py

import cv2
import dc_motor as motor
import time

t = 0.1

Color_Lower = (36,130,46)
Color_Upper = (113, 255, 255)
Frame_Width  = 320
Frame_Height = 240

camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH,  Frame_Width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, Frame_Height)

try:
    while True:
        (_, frame) = camera.read()

        # Do gaussian blur if needed
        frame = cv2.GaussianBlur(frame, (11, 11),1)

        # Convert to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Convert to binary with given color
        mask = cv2.inRange(hsv, Color_Lower, Color_Upper)

        # Do erode if needed
        #mask = cv2.erode(mask, None, iterations=2)

        # Do dilate if needed
        #mask = cv2.dilate(mask, None, iterations=2)

        # Find the contours
        _, contours,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        #(contours, _) = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        # Define mass center
        center = None
	
	
        if len(contours) > 0:
	    
            # Find the max length of contours
            c = max(contours, key=cv2.contourArea)
            
            # Find the x, y, radius of given contours        
            ((x, y), radius) = cv2.minEnclosingCircle(c)

            # Find the moments
            M = cv2.moments(c)
            

            try:
                # mass center
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

                # process every frame
                cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)
		#print (radius)	
                # Forward and backward rule # 
                if radius < 25 and radius > 5 :
                    if center[0] > Frame_Width/2 + 55 :
                        motor.turnRight()
                        
                    elif center[0] < Frame_Width/2 -55 :
                        motor.turnLeft()
                        
                    else:
                        motor.forward_2()
               
		elif radius < 45 and radius > 25 :
                    if center[0] > Frame_Width/2 + 55 :
                        motor.turnRight()
                        
                    elif center[0] < Frame_Width/2 -55 :
                        motor.turnLeft()
                        
                    else:
                        motor.forward_1()
         
                elif radius > 65:
                    motor.backward()
                                  
                else:
                    motor.brake()
        
	        

                # turn right and turn left rule
               # if center[0] > Frame_Width/2 + 10:
               #     motor.turnRight()
               # elif center[0] < Frame_Width/2 - 10:
               #     motor.turnLeft()
               # else:
               #     motor.stop()

            # if not find mass center
            except:
                pass

	else:
	    motor.stop()
        # mark these lines below if you don't need to display and the car will get faster
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break
        # mark these lines above if you don't need to display and the car will get faster

finally:
        motor.cleanup()
        camera.release()
        cv2.destroyAllWindows()


