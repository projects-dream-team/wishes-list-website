commonApp.service('LoadBlogsService', [
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