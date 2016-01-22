commonApp.controller('EventCtrl',
    ['$rootScope', '$http', '$scope', '$window', '$controller', '$timeout', 'CurrentUserService', 'DateFormatService', 'EventService',
    function($rootScope, $http, $scope, $window, $controller, $timeout, CurrentUserService, DateFormatService, EventService) {

        angular.extend(this, $controller('FormCtrl', {$scope: $scope}));

        var emptyProduct = {
                    id: null,
                    name:"",
                    url: "",
                    external: false
        };
        $scope.user = {};
        $scope.loadFailed = false;
        $scope.gatheringData = true;
        $scope.toEdit = false;
        $scope.initData = function(idToEdit){
            if ($scope.info != undefined){
                $scope.toEdit = true;
                EventService.getEvent($scope.info.additionalData.idToEdit).success(function(data){
                    $scope.formData = data;
                    $scope.user.id = $scope.formData.owner;
                    $scope.date = DateFormatService.unformatDate($scope.formData.date);
                    $scope.gatheringData = false;
                }).error(function(error){
                    $scope.loadFailed = true;
                });
            }else{
                CurrentUserService.getCurrentUser().success(function(data){
                    $scope.user = data;
                    $scope.formData.owner = $scope.user.id;
                    $scope.gatheringData = false;
                }).error(function(error){
                    $scope.loadFailed = true;
                });
                $scope.formData = {
                    gifts: [
                        emptyProduct
                    ]
                };
            }
        };


        $scope.setOwner = function (){
            angular.forEach($scope.formData.gifts, function(gift){
                gift.owner = $scope.user.id;
            })
        };

        $scope.submit = function(apiUrl) {
            $('.has-datepicker').trigger('dp.change');
            $scope.isLoading = true;
            $scope.formData.date = DateFormatService.formatDate($scope.date);
            $scope.formSubmitted = true;



            if ($scope.toEdit) {
                $http.put(apiUrl+$scope.formData.id+'/', $scope.formData
                ).success(function (data) {
                        $scope.formData = {};
                        $scope.success = true;
                        $scope.message = data;
                        $rootScope.$broadcast('event-changed');
                        $scope.isLoading = false;
                    }).error(function (err, message) {
                        $scope.isLoading = false;
                        $scope.message = err.detail;
                        $scope.success = false;
                        console.log(err);
                    })
            } else {
            $scope.setOwner();
            $http.post(apiUrl, $scope.formData
            ).success(function (data) {
                    $scope.formData = {};
                    $scope.success = true;
                    $scope.message = data;
                    $rootScope.$broadcast('event-changed');
                    $scope.isLoading = false;
                }).error(function (err, message) {
                    $scope.isLoading = false;
                    $scope.message = err.detail;
                    $scope.success = false;
                    console.log(err);
                })
            }
        };
        $scope.addProduct = function(){
            $scope.formData.gifts.push({
                    id: null,
                    name:"",
                    url: "",
                    external: false
        });

        };

        $scope.removeProduct = function(index){
            $scope.formData.gifts.splice(index, 1);
        };

        $scope.$watch('formData.gifts', function(newValue, oldValue) {
            $scope.initValidation('#eventForm')
        }, true);

    }]);
