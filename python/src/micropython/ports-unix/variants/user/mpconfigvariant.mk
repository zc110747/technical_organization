# This is the default variant when you `make` the Unix port.

FROZEN_MANIFEST ?= $(VARIANT_DIR)/manifest.py

##############################################################
# Start of User define region
###############################################################
# Support User Build Config
BOARD ?= x86
ifeq ($(BOARD), Walnutpi)
CFLAGS += -DSUPPORT_WIRINGPI_H=1
LDFLAGS += -lwiringPi
endif
ifeq ($(BOARD), imx6ull)
CROSS_COMPILE = arm-linux-gnueabihf-
endif

MICROPY_STANDALONE = 1

MICROPY_PY_FFI = 0

V = 1

#update
SRC_C += modpydev.c \
		modpyled.c 

##############################################################
# End of User define region
###############################################################
