commonApp.controller('DeleteEventCtrl', ['$scope', '$rootScope', 'EventService', '$uibModalInstance',
    function ($scope, $rootScope, EventService, $uibModalInstance) {

        console.log($uibModalInstance.extData);
        $scope.additionalData = $uibModalInstance.extData;

        $scope.loadFailed = false;
        $scope.gatheringData = false;

        $scope.ok = function () {
            EventService.deleteEvent($scope.additionalData.idToEdit).success(function (data) {
                $rootScope.$broadcast('eventDelete',{name:$scope.additionalData});
                $rootScope.$broadcast('event-changed');
                $uibModalInstance.close();
            }).error(function (error) {
                $scope.loadFailed = true;
            });

        };

        $scope.close = function () {
            $uibModalInstance.dismiss('cancel');
        };

    }]);
