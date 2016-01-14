commonApp.controller('ContactCtrl', [
    '$scope', '$window', '$http',
    function($scope, $window, $http) {
        $scope.messageSend = false;
        $scope.isLoading = false;
        $scope.contact = function() {
            if(!$scope.form.$valid){
                angular.forEach($scope.form.$error.required, function(field) {
                    field.$setDirty();
                });
            }
            else{
                $scope.isLoading = true;
                 $http.post("/contact/send/", $scope.formData

                ).success(function(data){
                    $scope.formData = {};
                    $scope.form = {};
                    $scope.messageSend = true;
                    $scope.message = data;
                    $scope.isLoading = false;
                }).error(function(err, message){
                     $scope.isLoading = false;
                     $scope.message = '';
                     angular.forEach(err, function(value,key){
                         angular.forEach(value, function(message){
                            $scope.message += message.message+' ';
                            $scope.form[key].$setValidity('required',false);
                        });

                    });
                 })
            }
        };
    }
]);
