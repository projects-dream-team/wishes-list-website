commonApp.service('DateFormatService',
    function() {
        this.formatDate = function(dateStr) {
            var arr = dateStr.split(" ");
            var dateArr = arr[0].split(".");
            var date = ""+dateArr[2]+"-"+dateArr[1]+"-"+dateArr[0];
            return date+"T"+arr[1];
        };
    }
);