#!/usr/bin/python
#coding: utf8
#引入gpio的模块
import time

#设置in1到in4接口
IN1 = 11
IN2 = 12
IN3 = 13
IN4 = 15

#初始化接口
def init():
    pass


## 左
def left(functionType,sleep_time1,sleep_time2):
    if functionType == 1:
        leftFront(sleep_time1,sleep_time2)
    elif functionType == -1:
        leftAfter(sleep_time1,sleep_time2)
## 右
def right(functionType,sleep_time1,sleep_time2):
    if functionType == 1:
        rightFront(sleep_time1,sleep_time2)
    elif functionType == -1:
        rightAfter(sleep_time2,sleep_time2)


## 左前进
def leftFront(sleep_time1,sleep_time2):
    print("IN3 1")
    print("IN4 -1")
    print(sleep_time1)
    time.sleep(sleep_time1)
    leftCleanup(sleep_time2)

## 左后退
def leftAfter(sleep_time1,sleep_time2):
    print("IN3 -1")
    print("IN4 1")
    print(sleep_time1)
    time.sleep(sleep_time1)
    leftCleanup(sleep_time2)

## 右前进
def rightFront(sleep_time1,sleep_time2):
    print("IN1 1")
    print("IN2 -1")
    print(sleep_time1)
    time.sleep(sleep_time1)
    leftCleanup(sleep_time2)

## 右后退
def rightAfter(sleep_time1,sleep_time2):
    print("IN1 -1")
    print("IN2 1")
    print(sleep_time1)
    time.sleep(sleep_time1)
    rightCleanup(sleep_time2)


## 左清理
def leftCleanup(sleep_time):
    print("IN3 0")
    print("IN4 0")
    print(sleep_time)
    time.sleep(sleep_time)


## 右清理
def rightCleanup(sleep_time):
    print("IN1 0")
    print("IN2 0")
    print(sleep_time)
    time.sleep(sleep_time)
