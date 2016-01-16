commonApp.service('EventService', [
    '$http',
    function($http) {
        this.getItems = function() {
            return $http.get('');
        };

        this.getNextPage = function(url) {
            return $http.get(url);
        };
    }
]);
