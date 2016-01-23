commonApp.service('FriendsService', [
    '$http',
    function($http) {
        this.getRequests = function() {
            return $http.get('/api/friendship/?requests=true');
        };

        this.getFriends = function(){
            return $http.get('/api/friendship/?friends=true');
        };

        this.accept = function(id,data) {
            return $http.put('/api/friendship/'+id+'/',data);
        };

        this.decline = function(id) {
            return $http.delete('/api/friendship/'+id+'/');
        };
    }
]);
