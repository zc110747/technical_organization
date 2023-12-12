/*
 * This file is part of the MicroPython project, http://micropython.org/
 *
 * The MIT License (MIT)
 *
 * Copyright (c) Jason
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
#include <stdio.h>

#if SUPPORT_WIRINGPI_H
#include <wiringPi.h>
#endif
#include "py/runtime.h"
#include "py/mphal.h"

#define LED 33
static uint8_t led_open_state = 0;

// This is the function which will be called from Python as pydev.open(str, flags).
STATIC mp_obj_t pyled_open(void) {

    int fd = 0;

    if(led_open_state == 0)
    {
        led_open_state = 1;
        printf("led open success!\n");
    }
    else
    {
        fd = -1;
        printf("led already open!\n");
    }

#if SUPPORT_WIRINGPI_H
    wiringPiSetup ();
    digitalWrite (LED, LOW);    //点亮，LOW熄灭。
    pinMode (LED, OUTPUT);
#endif

    // Calculate the addition and convert to MicroPython object.
    return mp_obj_new_int(fd);
}
// Define a Python reference to the function above.
STATIC MP_DEFINE_CONST_FUN_OBJ_0(pyled_open_obj, pyled_open);

// This is the function which will be called from Python as pydev.open(str, flags).
STATIC mp_obj_t pyled_on(void) {
    // Extract the ints from the micropython input objects.
    
    if(led_open_state == 1)
    {
#if SUPPORT_WIRINGPI_H
        digitalWrite (LED, HIGH);
#endif
        printf("led on!\n");
    }
    else
    {
        printf("led set failed, need open!\n"); 
    }

    // Calculate the addition and convert to MicroPython object.
    return mp_obj_new_int(led_open_state);
}
// Define a Python reference to the function above.
STATIC MP_DEFINE_CONST_FUN_OBJ_0(pyled_on_obj, pyled_on);

// This is the function which will be called from Python as pydev.open(str, flags).
STATIC mp_obj_t pyled_off(void) {
    // Extract the ints from the micropython input objects.
    
    if(led_open_state == 1)
    {
#if SUPPORT_WIRINGPI_H
        digitalWrite (LED, LOW);
#endif
        printf("led off!\n");
    }
    else
    {
        printf("led set failed, need open!\n"); 
    }

    // Calculate the addition and convert to MicroPython object.
    return mp_obj_new_int(led_open_state);
}
// Define a Python reference to the function above.
STATIC MP_DEFINE_CONST_FUN_OBJ_0(pyled_off_obj, pyled_off);

// This is the function which will be called from Python as pydev.open(str, flags).
STATIC mp_obj_t pyled_close(void) {
    // Extract the ints from the micropython input objects.
    led_open_state = 0;

    printf("led close!\n");

    // Calculate the addition and convert to MicroPython object.
    return mp_obj_new_int(led_open_state);
}
// Define a Python reference to the function above.
STATIC MP_DEFINE_CONST_FUN_OBJ_0(pyled_close_obj, pyled_close);

// Define all attributes of the module.
// Table entries are key/value pairs of the attribute name (a string)
// and the MicroPython object reference.
// All identifiers and strings are written as MP_QSTR_xxx and will be
// optimized to word-sized integers by the build system (interned strings).
STATIC const mp_rom_map_elem_t pyled_module_globals_table[] = {
    { MP_ROM_QSTR(MP_QSTR___name__), MP_ROM_QSTR(MP_QSTR_pyled) },
    { MP_ROM_QSTR(MP_QSTR_open), MP_ROM_PTR(&pyled_open_obj) },
    { MP_ROM_QSTR(MP_QSTR_on), MP_ROM_PTR(&pyled_on_obj) },  
    { MP_ROM_QSTR(MP_QSTR_off), MP_ROM_PTR(&pyled_off_obj) },   
    { MP_ROM_QSTR(MP_QSTR_close), MP_ROM_PTR(&pyled_close_obj) },
};
STATIC MP_DEFINE_CONST_DICT(pyled_module_globals, pyled_module_globals_table);

// Define module object.
const mp_obj_module_t pyled_module = {
    .base = { &mp_type_module },
    .globals = (mp_obj_dict_t *)&pyled_module_globals,
};

// Register the module to make it available in Python.
MP_REGISTER_MODULE(MP_QSTR_pyled, pyled_module);
