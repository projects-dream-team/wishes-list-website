commonApp.directive('dDatepicker', function($timeout, $parse) {
        return {
            scope: {
                ngModel: '='
            },
            link: function($scope, element, $attrs) {
                return $timeout(function() {

                    return $(element).datetimepicker(
                        {
                            minDate:moment().add(1, 'd').toDate(),
                            sideBySide:true,
                            allowInputToggle:true,
                            locale:"pl",
                            useCurrent:false,
                            defaultDate:moment().add(1, 'd').add(1,'h')
                        }
                    ).on('dp.change', function(event) {
                            $scope.$apply(function() {
                                $scope.ngModel = event.target.value;
                            });
                    }).on('dp.update', function(event) {
                            $scope.$apply(function() {
                                $scope.ngModel = event.target.value;
                            });
                    });
                });
            }
        };
    });
