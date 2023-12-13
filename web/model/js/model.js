
var json_data = {
    page: "1",
    records: "3",
    data: [{
        title: "title1",
        content: "content1"
    },{
        title: "title2",
        content: "content2"
    },{
        title: "title3",
        content: "content3"
    },{
        title: "title4",
        content: "content4"
    },{
        title: "title5",
        content: "content5"
    },]
};

String.prototype.tmp = function(obj) {
    return this.replace(/\$\w+\$/g, function(matchs) {
        var returns = obj[matchs.replace(/\$/g, "")];
        return (returns + "") == "undefined"? "": returns;
    });
};