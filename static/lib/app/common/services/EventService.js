commonApp.service('EventService', [
    '$http',
    function($http) {
        this.deleteEvent = function(id) {
            return $http.delete('/api/event/'+id+'/');
        };

        this.getEvent = function(id) {
            return $http.get('/api/event/'+id+'/');
        };

        this.getAllEvents = function() {
            return $http.get('/api/event/');
        };

        this.getEventsForUser = function(id) {
            return $http.get('/api/event/?owner='+id);
        };
    }
]);
