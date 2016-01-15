commonApp.controller('authCtrl',
    ['$rootScope', '$http', '$scope', '$window', 'api', '$controller',
    function($rootScope, $http, $scope, $window, api, $controller) {

        angular.extend(this, $controller('FormCtrl', {$scope: $scope}));

        $scope.submit = function(apiUrl) {
            $scope.formSubmitted = true;
            $scope.isLoading = true;
            api.auth.login($scope.getCredentials()).
            $promise.
            then(function(data){
                $window.location.href = "/";
            }).catch(function (err, message) {
                $scope.isLoading = false;
                $scope.message=err.data.detail;
                $scope.success = false;
                console.log(err.data.detail);
            })
        };

        $scope.getCredentials = function(){
            return {
                email: $scope.formData.email,
                password: $scope.formData.password
            };
        };

        $scope.login = function(){
            $scope.showMessage = false;
            $scope.alerts = [];
            $scope.isLoading=true;

                api.auth.login($scope.getCredentials()).
                $promise.
                then(function(data){
                    $window.location.href = "/";
                }).
                catch(function(data){
                    $scope.isLoading=false;
                    $scope.formData.email = '';
                    $scope.formData.password = '';
                    $scope.message=data.data.detail;
                });
        };


        //logout user
        $scope.logout = function(){
            api.auth.logout(function(){
                $scope.user = undefined;
                $window.location.href="/";
            });
        };

        //restore user password
        $scope.restore_password = function(){
            $scope.alerts = [];

            $scope.isLoading = true;
            //var data = $scope.getCredentials();
            var data = {email:"", "csrfmiddlewaretoken": $scope.formData.csrfmiddlewaretoken};
            var email = $scope.formData.email;
            data.email = email;
            $http.post(
                '/users/password/reset/',
                data

            ).success(function(data){
                $scope.isLoading = false;
                $scope.message = data;
                $scope.alerts.push({type: 'success', msg: data});
            }).error(function(err){
                $scope.isLoading = false;
                $scope.message = err;
                $scope.form.email.$setValidity('email',false);
                if(err.email != undefined){
                    angular.forEach(err.email, function(error){
                        $scope.alerts.push({type: 'danger', msg: error.message });
                    });
                }else{
                     $scope.alerts.push({type: 'danger', msg: err });
                }

            });

        };
        //


        ////$scope.delete_account = function(){
        ////    $scope.showMessage = false;
        ////    $http({
        ////        url: url_delete_account,
        ////        data: $scope.formData,
        ////        method: 'POST',
        ////        headers : {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
        ////
        ////    }).success(function(data){
        ////        $window.location.href = "/"
        ////    }).error(function(err){
        ////    })
        ////};


    }]);
