

class ModuleProcess
{
    constructor(){
        this.buf = require("./Buffer.js");
    }
    Buffer_process(){
        this.buf.Buffer_new();
        this.buf.Buffer_old();
    }
}

const mp = new ModuleProcess();
mp.Buffer_process();