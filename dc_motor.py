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
# Usage  : dc_motor.py

import RPi.GPIO as GPIO
import time
#Set Used GPIO 

Motor_R1_Pin = 21
Motor_R2_Pin = 20
Motor_L1_Pin = 27
Motor_L2_Pin = 17
Enable_1 = 23
Enable_2 = 24

t = 0.01

GPIO.setmode(GPIO.BCM)
GPIO.setup(Motor_R1_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Motor_R2_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Motor_L1_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Motor_L2_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Enable_1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Enable_2, GPIO.OUT, initial=GPIO.LOW)

pwm_e1 = GPIO.PWM(Enable_1, 500)
pwm_e2 = GPIO.PWM(Enable_2, 500)
pwm_e1.start(0)
pwm_e2.start(0)

def brake():
    pwm_e1.ChangeDutyCycle(10)
    pwm_e2.ChangeDutyCycle(10)
    GPIO.output(Motor_R1_Pin, False)
    GPIO.output(Motor_R2_Pin, True)
    GPIO.output(Motor_L1_Pin, False)
    GPIO.output(Motor_L2_Pin, True)
    time.sleep(t)
    GPIO.output(Motor_R1_Pin, False)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, False)
    GPIO.output(Motor_L2_Pin, False)
    print("BR")
    #time.sleep(t)


def stop():
    pwm_e1.ChangeDutyCycle(100)
    pwm_e2.ChangeDutyCycle(100)
    GPIO.output(Motor_R1_Pin, False)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, False)
    GPIO.output(Motor_L2_Pin, False)
    print("s")
    #time.sleep(t)

def forward_1():
    pwm_e1.ChangeDutyCycle(40)
    pwm_e2.ChangeDutyCycle(40)
    GPIO.output(Motor_R1_Pin, True)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, True)
    GPIO.output(Motor_L2_Pin, False)
    print("F_L")
    time.sleep(t)
    #stop()

def forward_2():
    pwm_e1.ChangeDutyCycle(65)
    pwm_e2.ChangeDutyCycle(65)
    GPIO.output(Motor_R1_Pin, True)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, True)
    GPIO.output(Motor_L2_Pin, False)
    print("F_F")
    time.sleep(t)
    #stop()


def backward():
    pwm_e1.ChangeDutyCycle(45)
    pwm_e2.ChangeDutyCycle(45)

    GPIO.output(Motor_R1_Pin, False)
    GPIO.output(Motor_R2_Pin, True)
    GPIO.output(Motor_L1_Pin, False)
    GPIO.output(Motor_L2_Pin, True)
    print("B")
    time.sleep(t)
    #stop()

def turnRight():
    pwm_e1.ChangeDutyCycle(100)
    pwm_e2.ChangeDutyCycle(100)
    GPIO.output(Motor_R1_Pin, True)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, False)
    GPIO.output(Motor_L2_Pin, True)
    print ("R")
    time.sleep(t)
    #stop()

def turnLeft():
    pwm_e1.ChangeDutyCycle(100)
    pwm_e2.ChangeDutyCycle(100)
    GPIO.output(Motor_R1_Pin, False)
    GPIO.output(Motor_R2_Pin, True)
    GPIO.output(Motor_L1_Pin, True)
    GPIO.output(Motor_L2_Pin, False)
    print("L")
    time.sleep(t)
    #stop() 

#while True:
#    a = input("")
#    a = int(a)
#    if a == 1:
#        turnRight()
#    elif a == 2:
#        turnLeft()
#    elif a ==3:
#        forward()
def cleanup():
    stop()
    GPIO.cleanup()

