commonApp.service('EventService', [
    '$http',
    function($http) {
        this.deleteEvent = function(id) {
            return $http.delete('/api/event/'+id+'/');
        };

        this.getNextPage = function(url) {
            return $http.get(url);
        };
    }
]);
