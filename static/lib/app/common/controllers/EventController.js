commonApp.controller('EventCtrl',
    ['$rootScope', '$http', '$scope', '$window', '$controller', 'CurrentUserService', 'DateFormatService',
    function($rootScope, $http, $scope, $window, $controller, CurrentUserService, DateFormatService) {

        angular.extend(this, $controller('FormCtrl', {$scope: $scope}));

        var emptyProduct = {
                    id: null,
                    name:"",
                    url: "",
                    external: false
        };
        $scope.loadFailed = false;
        $scope.gatheringData = true;
        $scope.initData = function(){

            CurrentUserService.getCurrentUser().success(function(data){
                $scope.user = data;
                $scope.formData.owner = $scope.user.id;
                $scope.gatheringData = false;
            }).error(function(error){
                $scope.loadFailed = true;
            });
        };
        $scope.formData = {
            gifts: [
                emptyProduct
            ]
        };


        $scope.submit = function(apiUrl) {
            $scope.initForm('#eventForm','/api/event/');
            return false;
            $('.has-datepicker').trigger('dp.change');
            $scope.formData.date = DateFormatService.formatDate($scope.date);
            console.log($scope.formData);
            $scope.formSubmitted = true;
            $scope.isLoading = true;
            $http.post(apiUrl, $scope.formData
            ).success(function (data) {
                    $scope.formData = {};
                    $scope.success = true;
                    $scope.message = data;
                    $scope.isLoading = false;
                }).error(function (err, message) {
                    $scope.isLoading = false;
                    $scope.message = err.detail;
                    $scope.success = false;
                    console.log(err);
                })
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

        $scope.$watch('formData.gifts.length', function(newValue, oldValue) {
            console.log("gifts changed");
            $scope.initForm('#eventForm','/api/event/');
        }, true);

        $scope.showFormData = function(){
            console.log($scope.formData);
        }

    }]);
