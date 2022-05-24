#!/usr/bin/env python
# coding: utf-8
'''
@File   :espnow.py
@Author :youxinweizhi
@Date   :2021/12/23
@Github :https://github.com/youxinweizhi
'''
"""
https://github.com/glenn20/micropython/blob/espnow-g20/docs/library/espnow.rst
https://micropython-glenn20.readthedocs.io/en/latest/library/espnow.html
"""
import network
from machine import Pin
from utime import sleep_ms
from esp import espnow

def help():
	print("""
	from espnow import ESPNOW
	from machine import Pin

	#按键回调函数
	def button_callback(pin_instance:Pin):
		simple.send_message(simple.BROADCAST_MAC, b'toggle_led')

	#espnow回调函数
	def espnow_callback(mac,message):
		if message == b'toggle_led':
			led.value(not led.value())
	
	#注册按键
	button = Pin(9, Pin.IN, Pin.PULL_UP)
	button.irq(button_callback, Pin.IRQ_RISING)
	
	#初始化LED
	led = Pin(3, Pin.OUT, value=0)
	
	#实例化espnow对象
	simple = ESPNOW(callback=espnow_callback)
""")


class ESPNOW(object):
	IF_INDEX_STA = network.STA_IF                   #ap模式
	IF_INDEX_AP = network.AP_IF                     #sta模式
	BROADCAST_MAC = b'\xff\xff\xff\xff\xff\xff'     #广播地址

	#初始化实例参数
	def __init__(self,callback):
		w0=network.WLAN(network.AP_IF) # Or network.STA_IF
		w0.active(True)
		w0.config(channel=6)    #信道
		w0.config(hidden=True)
		self.callback=callback
		self.__espnow = espnow.ESPNow()
		self.__espnow.deinit()
		self.config_callback(self.__espnow_callback)
		self.__espnow.init()
		self.register_peer(self.BROADCAST_MAC, ifidx=self.IF_INDEX_AP)
		print('espnow is running...')

	#注册设备
	def register_peer(self,mac_peer,ifidx,encrypt=False):
		self.__espnow.add_peer(mac_peer, ifidx=ifidx, encrypt=encrypt)

	#解析mac地址
	def __decode_mac_address(self, mac_address):
		if isinstance(mac_address, (bytes, bytearray)) and len(mac_address) == 6:
			return ":".join(['{:02x}'.format(byte) for byte in mac_address])
		else:
			return mac_address
	
	#espnow接收回调函数
	def __espnow_callback(self, espnow_instance):
		while espnow_instance.poll():
			mac, message = espnow_instance.irecv(0)
			mac=self.__decode_mac_address(mac)
			print(f'received from [mac] {mac}, [message] {message}')
			#下面是判断逻辑
			self.callback(mac,message)
	
	#配置接收回调
	def config_callback(self,callback):
		self.__espnow.config(on_recv=callback)
	
	#发送消息
	def send_message(self,mac_peer,msg):
		try:
			res=self.__espnow.send(mac_peer, msg)
			print(f'send to [mac] {self.__decode_mac_address(mac_peer)} [message] {msg} [status] {res}')
		except OSError as err:
			if len(err.args) < 2:
				raise err
			if err.args[1] == 'ESP_ERR_ESPNOW_NOT_INIT':
				print("espnow is not init")
			elif err.args[1] == 'ESP_ERR_ESPNOW_NOT_FOUND':
				print("not register peer(mac)")
			elif err.args[1] == 'ESP_ERR_ESPNOW_IF':
				network.WLAN(network.STA_IF).active(True)
				print("not active network")
			else:
				raise err
	
	#销毁
	def deinit(self):
		self.__espnow.deinit()

