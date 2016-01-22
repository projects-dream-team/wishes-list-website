commonApp.service('DateFormatService',
    function($filter) {
        this.formatDate = function(dateStr) {
            console.log(dateStr);
            var arr = dateStr.split(" ");
            var dateArr = arr[0].split(".");
            var date = ""+dateArr[2]+"-"+dateArr[1]+"-"+dateArr[0];
            return date+"T"+arr[1];
        };

        this.unformatDate = function(date){
            return $filter('date')(date, 'dd.MM.yyyy HH:mm')
        };

        this.fromJsDate = function(date){
            return $filter('date')(date, 'yyyy-MM-ddTHH:mm')
        }
    }
);