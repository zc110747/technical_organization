(function(me) {
    var dirty = [];
    var original = [];
    var ngModels = [];
    var getObjValue = function(objStr) {
        return eval("(window.$scope." + objStr + ")");
    }
    var setObjValue = function(objStr, value) {
        eval("window.$scope." + objStr + " = \"" + value + "\"");
    }
    me.angularjs = function(initFn) {
        me.$scope = {};
        initFn(me.$scope);
        if (me.$scope) {
            ngModels = document.querySelectorAll("*[ng-model]");
            if (ngModels.length != 0) {
                var len = ngModels.length
                for (var i = 0; i < len; i++) {
                    var ngModelValue = ngModels[i].getAttribute("ng-model");
                    var objArr = ngModelValue.split('.');
                    var tempStr = "";
                    for (var j = 0; j < objArr.length; j++) {
                        tempStr = (j == objArr.length - 1) ? tempStr + "$" + objArr[j] : tempStr + objArr[j] + ".";
                    }

                    original[i] = ngModelValue;
                    dirty[i] = tempStr;
                    setObjValue(tempStr, "");
                }
                check();
            }
        }
    }
    var check = function() {
        setInterval(function() {
            //赋值绑定
            for (var i = 0; i < ngModels.length; i++) {
                var originalValue = getObjValue(original[i]);
                var dirtyValue = getObjValue(dirty[i]);
                if (originalValue == ngModels[i].value) setObjValue(dirty[i], originalValue);
                if (originalValue != dirtyValue) ngModels[i].value = originalValue;
                if (ngModels[i].value != dirtyValue) setObjValue(original[i], ngModels[i].value);
            }
        },  1);
    }
})(window);