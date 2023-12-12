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
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <signal.h>
#include <sys/ioctl.h>

#include "py/runtime.h"
#include "py/mphal.h"

// This is the function which will be called from Python as pydev.open(str, flags).
STATIC mp_obj_t pydev_open(size_t n, const mp_obj_t *obj_list) {
    const char *dev; 
    int fd, flag;
    int permission;

    // Extract the ints from the micropython input objects.
    dev = mp_obj_str_get_str(obj_list[0]);
    flag = mp_obj_get_int(obj_list[1]);
    if(n > 2)
    {
        permission = mp_obj_get_int(obj_list[2]);

        //Convert Dec to Oct
        permission = permission/100*64 + permission/10%10*8 + permission%10;
        fd = open(dev, flag, permission);
        if(fd >= 0)
            printf("device %s open success, fd:%d, permission:%d\n", dev, fd, permission);
    }
    else
    {
        fd = open(dev, flag); 
        if(fd >= 0)
            printf("device %s open success, fd:%d\n", dev, fd);
    }
 
    if(fd < 0)
        printf("device %s open failed!\n", dev);

    // Calculate the addition and convert to MicroPython object.
    return mp_obj_new_int(fd);
}

// Define a Python reference to the function above.
STATIC MP_DEFINE_CONST_FUN_OBJ_VAR_BETWEEN(pydev_open_obj, 2, 3, pydev_open);

void pyb_buf_get_for_send(mp_obj_t o, mp_buffer_info_t *bufinfo, byte *tmp_data) {
    if (mp_obj_is_int(o)) {
        tmp_data[0] = mp_obj_get_int(o);
        bufinfo->buf = tmp_data;
        bufinfo->len = 1;
        bufinfo->typecode = 'B';
    } else {
        mp_get_buffer_raise(o, bufinfo, MP_BUFFER_READ);
    }
}

mp_obj_t pyb_buf_get_for_recv(mp_obj_t o, vstr_t *vstr) {
    if (mp_obj_is_int(o)) {
        // allocate a new bytearray of given length
        vstr_init_len(vstr, mp_obj_get_int(o));
        return MP_OBJ_NULL;
    } else {
        // get the existing buffer
        mp_buffer_info_t bufinfo;
        mp_get_buffer_raise(o, &bufinfo, MP_BUFFER_WRITE);
        vstr->buf = bufinfo.buf;
        vstr->len = bufinfo.len;
        return o;
    }
}

// This is the function which will be called from Python as 
//pydev.write(fd, bytearray).
STATIC mp_obj_t pydev_write(mp_obj_t fd_obj, mp_obj_t buffer_obj) {

    int fd;
    int out_size = 0;
    byte data[1];
    mp_buffer_info_t bufferinfo;

    // Extract the ints from the micropython input objects.
    fd = mp_obj_get_int(fd_obj);
    pyb_buf_get_for_send(buffer_obj, &bufferinfo, data);

    if(fd >= 0 && bufferinfo.len>0)
    {
        printf("fd:%d, write size:%d\n", fd, (int)bufferinfo.len);
        out_size = write(fd, bufferinfo.buf, bufferinfo.len);
    }

    // Calculate the addition and convert to MicroPython object.
    return mp_obj_new_int(out_size);
}
// Define a Python reference to the function above.
STATIC MP_DEFINE_CONST_FUN_OBJ_2(pydev_write_obj, pydev_write);

// This is the function which will be called from Python as 
//pydev.ioctl(fd, cmd, bytearray).
STATIC mp_obj_t pydev_ioctl(mp_obj_t fd_obj, mp_obj_t cmd_obj, mp_obj_t buffer_obj) {

    int fd, cmd;
    int out_size = 0;
    byte data[1];
    mp_buffer_info_t bufferinfo;

    // Extract the ints from the micropython input objects.
    fd = mp_obj_get_int(fd_obj);
    cmd = mp_obj_get_int(cmd_obj);
    pyb_buf_get_for_send(buffer_obj, &bufferinfo, data);

    if(fd >= 0)
    {
        out_size = ioctl(fd, cmd, bufferinfo.buf);
    }

    // Calculate the addition and convert to MicroPython object.
    return mp_obj_new_int(out_size);
}
// Define a Python reference to the function above.
STATIC MP_DEFINE_CONST_FUN_OBJ_3(pydev_ioctl_obj, pydev_ioctl);

// This is the function which will be called from Python as pydev.open(str, flags, ...).
//pydev.read(fd, bytearray, size).
STATIC mp_obj_t pydev_read(mp_obj_t fd_obj, mp_obj_t buffer_obj, mp_obj_t size_obj) {
    // Extract the ints from the micropython input objects.
    int fd;
    int out_size = 0;
    size_t size;
    vstr_t vstr;
    
    fd = mp_obj_get_int(fd_obj);
    size = mp_obj_get_int(size_obj);
    pyb_buf_get_for_recv(buffer_obj, &vstr);
    size = size>vstr.len?vstr.len:size;

    if(fd >= 0 && size > 0)
    {
        out_size = read(fd, vstr.buf, size);  
    }

    // Calculate the addition and convert to MicroPython object.
    return mp_obj_new_int(out_size);
}

// Define a Python reference to the function above.
STATIC MP_DEFINE_CONST_FUN_OBJ_3(pydev_read_obj, pydev_read);

// This is the function which will be called from Python as pydev.open(str, flags).
STATIC mp_obj_t pydev_close(mp_obj_t a_obj) {
    // Extract the ints from the micropython input objects.
    int fd = mp_obj_get_int(a_obj);
    int state;

    state = close(fd);

    // Calculate the addition and convert to MicroPython object.
    return mp_obj_new_int(state);
}
// Define a Python reference to the function above.
STATIC MP_DEFINE_CONST_FUN_OBJ_1(pydev_close_obj, pydev_close);

// Define all attributes of the module.
// Table entries are key/value pairs of the attribute name (a string)
// and the MicroPython object reference.
// All identifiers and strings are written as MP_QSTR_xxx and will be
// optimized to word-sized integers by the build system (interned strings).
STATIC const mp_rom_map_elem_t pydev_module_globals_table[] = {
    { MP_ROM_QSTR(MP_QSTR___name__), MP_ROM_QSTR(MP_QSTR_pydev) },
    { MP_ROM_QSTR(MP_QSTR_open), MP_ROM_PTR(&pydev_open_obj) },
    { MP_ROM_QSTR(MP_QSTR_write), MP_ROM_PTR(&pydev_write_obj) },  
    { MP_ROM_QSTR(MP_QSTR_read), MP_ROM_PTR(&pydev_read_obj) },   
    { MP_ROM_QSTR(MP_QSTR_ioctl), MP_ROM_PTR(&pydev_ioctl_obj) },
    { MP_ROM_QSTR(MP_QSTR_close), MP_ROM_PTR(&pydev_close_obj) },

#define C(name) { MP_ROM_QSTR(MP_QSTR_##name), MP_ROM_INT(name) }
    C(O_RDWR),
    C(O_NONBLOCK),
    C(O_NDELAY),
    C(O_RDONLY),
    C(O_WRONLY),
    C(O_CREAT),
#undef C
};
STATIC MP_DEFINE_CONST_DICT(pydev_module_globals, pydev_module_globals_table);

// Define module object.
const mp_obj_module_t pydev_module = {
    .base = { &mp_type_module },
    .globals = (mp_obj_dict_t *)&pydev_module_globals,
};

// Register the module to make it available in Python.
MP_REGISTER_MODULE(MP_QSTR_pydev, pydev_module);
