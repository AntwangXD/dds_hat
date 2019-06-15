#
# Makefile for the Analog devices ad9834 device driver
#

obj-m += ad9834.o

all:
	make -C /usr/lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
	make -C /usr/lib/modules/$(shell uname -r)/build M=$(PWD) clean 

