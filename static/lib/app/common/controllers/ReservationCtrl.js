commonApp.controller('ReservationCtrl', ['$scope', '$rootScope', 'EventService', '$controller', '$uibModalInstance',
    function ($scope, $rootScope, EventService, $controller, $uibModalInstance) {

        $scope.additionalData = $uibModalInstance.extData;

        $scope.loadFailed = false;
        $scope.isLoading = true;
        console.log($scope.additionalData);
        $scope.initForm = function(formID){
            console.log(formID+' input,'+formID+' textarea');
            //console.log($(formID+' input,'+formID+' textarea'));
            $(formID+' input,'+formID+' textarea').jqBootstrapValidation({
                preventSubmit: true,
                submitError: function($form, event, errors) {
                    // additional error messages or events
                    console.log(errors);
                },
                submitSuccess: function($form, event) {
                    event.preventDefault(); // prevent default submit behaviour
                    // get values from FORM
                    $scope.submit();
                },
                filter: function() {
                    return $(this).is(":visible");
                },
            });
        };
        $scope.initData = function(){
            EventService.getGift($scope.additionalData.idToEdit).success(function (data) {
                $scope.formData = data;

                if ($scope.additionalData.user != 'None'){
                    $scope.formData.reserved_by = $scope.additionalData.user
                }else{
                    $scope.formData.reserved_by = null;
                }

                $scope.isLoading = false;
            }).error(function (error) {
                $scope.loadFailed = true;
            });

        };

        $scope.submit = function(){
            $scope.isLoading = true;
            $scope.formData.reservation_date = Date.now();
            EventService.editGift($scope.formData).success(function (data) {
                $rootScope.$broadcast('eventDelete',{name:$scope.additionalData});
                $rootScope.$broadcast('event-changed');
                $uibModalInstance.close();
                $scope.success = true;
                $scope.isLoading = false;
            }).error(function (error) {
                $scope.loadFailed = true;
            });

        };

        $scope.close = function () {

            $uibModalInstance.dismiss('cancel');
        };

    }]);
