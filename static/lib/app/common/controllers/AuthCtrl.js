commonApp.controller('authCtrl',
    ['$rootScope', '$http', '$scope', '$window', 'api', '$uibModalInstance',
    function($rootScope, $http, $scope, $window, api,$uibModalInstance) {

        function add_auth_header(data, headersGetter){
            // as per HTTP authentication spec [1], credentials must be
            // encoded in base64. Lets use window.btoa [2]
            var headers = headersGetter();
            headers['Authorization'] = ('Basic ' + btoa(data.email +
                                        ':' + data.password));
        }
        // defining the endpoints. Note we escape url trailing dashes: Angular
        // strips unescaped trailing slashes. Problem as Django redirects urls
        // not ending in slashes to url that ends in slash for SEO reasons, unless
        // we tell Django not to [3]. This is a problem as the POST data cannot
        // be sent with the redirect. So we want Angular to not strip the slashes!

          $scope.close = function () {
            $uibModalInstance.dismiss('cancel');
          };
        $scope.alerts =[];
        $scope.isLoading=false;
        $scope.closeAlert = function(index) {
            $scope.alerts.splice(index, 1);
        };

        $scope.submit = function($event,callback) {
            var form = $scope[angular.element($event.target).attr('name')];
            if(form.$invalid){
                angular.forEach(form.$error.required, function (field) {
                    field.$setDirty();
                });
            }else{
                callback();
            }
        };

        var showErrors = function(form,errors){
            var messages = '';
            angular.forEach(errors.errors,function(value, key){
                messages += value+' ';
                form[key].$setValidity('email',false);
                $scope.alerts.push({type: 'danger', msg: value})
            });
            return messages;
        };

        $scope.accoutCreated = false;
        $scope.formData = {};
        $scope.getCredentials = function(){
            return {
                email: $scope.formData.email,
                password: $scope.formData.password
            };
        };

        $scope.register = function() {
            $scope.message = '';
            $scope.isLoading=true;
            $scope.alerts =[];
             $http.post("/api/users/", $scope.formData

            ).success(function(data){
                $scope.isLoading=false;
                $scope.formData = {};
                $scope.form = {};
                $scope.accoutCreated = true;
                $scope.message = data;
                $scope.alerts.push({type: 'success', msg: data });

            }).error(function(err){
                 $scope.isLoading=false;
                 //console.log(err);
                 $scope.message = showErrors($scope.form,err);
            })

        };


        $scope.login = function(){
            $scope.showMessage = false;
            $scope.alerts = [];
            $scope.isLoading=true;

                api.auth.login($scope.getCredentials()).
                $promise.
                then(function(data){
                    $window.location.href = "/application/";
                }).
                catch(function(data){
                    $scope.isLoading=false;
                    $scope.formData.email = '';
                    $scope.formData.password = '';
                    $scope.message=data.data.detail;
                    $scope.alerts.push({type: 'danger', msg: data.data.detail });
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
