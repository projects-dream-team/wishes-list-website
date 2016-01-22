commonApp.controller('ReservationCtrl', ['$scope', '$rootScope', 'EventService', 'DateFormatService', '$controller',
    function ($scope, $rootScope, EventService, DateFormatService, $controller) {
        angular.extend(this, $controller('FormCtrl', {$scope: $scope}));
        //$scope.additionalData = $uibModalInstance.extData;

        $scope.loadFailed = false;
        $scope.isLoading = true;
        $scope.formSubmitted = false;
        $scope.initData = function(){
            EventService.getGift($scope.additionalData.idToEdit).success(function (data) {
                $scope.formData = data;

                if ($scope.additionalData.user != 'None') {
                    $scope.formData.reserved_by = $scope.additionalData.user
                } else {
                    $scope.formData.reserved_by = null;
                }

                $scope.isLoading = false;
            }).error(function (error) {
                $scope.loadFailed = true;
            });

        };

        $scope.submit = function(apiUrl){
            $scope.isLoading = true;

            $scope.formData.reservation_date = DateFormatService.fromJsDate(Date.now());
            EventService.editGift($scope.formData.id,$scope.formData).success(function (data) {
                $rootScope.$broadcast('gift-reserved');
                $scope.formSubmitted = true;
                $scope.success = true;
                $scope.isLoading = false;
            }).error(function (error) {
                $scope.loadFailed = true;
            });

        };
        $scope.cancelReservation = function(){
            $scope.isLoading = true;

            $scope.formData.reservation_date = null;
            $scope.formData.reserved_by = null;
            EventService.editGift($scope.formData.id,$scope.formData).success(function (data) {
                $rootScope.$broadcast('gift-reserved');
                $scope.formSubmitted = true;
                $scope.success = true;
                $scope.isLoading = false;
            }).error(function (error) {
                $scope.loadFailed = true;
            });

        };
        $rootScope.$on('gift-reserved',function(data){
            location.reload();
        })
    }]);
