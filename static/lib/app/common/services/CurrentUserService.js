commonApp.service('CurrentUserService', [
    '$http',
    function($http) {
        this.getCurrentUser = function() {
            return $http.get('/api/current_user/1/');
        };
    }
]);

