commonApp.controller('FormCtrl', [
    '$scope', '$window', '$http', '$controller', 'DateFormatService',
    function($scope, $window, $http, $controller, DateFormatService) {
        $scope.success = true;
        $scope.isLoading = false;
        $scope.formSubmitted = false;
        $scope.additionalData;
        $scope.initForm = function(formID,apiURL,additionalData){
            //console.log(formID+' input,'+formID+' textarea');
            //console.log($(formID+' input,'+formID+' textarea'));
            $scope.additionalData = additionalData;
            $(formID+' input,'+formID+' textarea').jqBootstrapValidation({
                preventSubmit: true,
                submitError: function($form, event, errors) {
                    // additional error messages or events
                    console.log(errors);
                },
                submitSuccess: function($form, event) {
                    event.preventDefault(); // prevent default submit behaviour
                    // get values from FORM
                    $scope.submit(apiURL);
                },
                filter: function() {
                    return $(this).is(":visible");
                },
            });
        };

        $scope.initValidation = function(formID){
            //console.log(formID+' input,'+formID+' textarea');
            //console.log($(formID+' input,'+formID+' textarea'));
            $(formID+' input,'+formID+' textarea').jqBootstrapValidation("destroy");
            $(formID+' input,'+formID+' textarea').jqBootstrapValidation({
                preventSubmit: true,
                submitError: function($form, event, errors) {
                    // additional error messages or events
                    //console.log(errors);
                },
                submitSuccess: function($form, event) {
                    event.preventDefault(); // prevent default submit behaviour
                    // get values from FORM
                    //$scope.submit(apiURL);
                },
                filter: function() {
                    return $(this).is(":visible");
                },
            });
        };
        $scope.submit = function(apiUrl) {
            $scope.formSubmitted = true;
            $scope.isLoading = true;
            $http.post(apiUrl, $scope.formData
            ).success(function (data) {
                    $scope.formData = {};
                    $scope.form = {};
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
    }
]);
