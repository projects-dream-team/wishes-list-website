commonApp.controller('EventListCtrl',
    ['$rootScope', '$http', '$scope', '$window', '$filter', 'CurrentUserService', 'DateFormatService', 'EventService',
    function($rootScope, $http, $scope, $window, $filter, CurrentUserService, DateFormatService, EventService) {


        $scope.lists = [];
        $scope.loadFailed = false;
        $scope.gatheringData = true;
        $scope.showFuture = true;
        $scope.limit = 10;
        $scope.initData = function(userId){
                $scope.userId = userId;
                $scope.loadLists();
            };

        $scope.loadLists = function(){
            $scope.gatheringData = true;
            EventService.getEventsForUser($scope.userId).success(function(data){
                $scope.lists = data;

                $scope.gatheringData = false;
            }).error(function(error){
                $scope.loadFailed = true;
            });
        };

        $scope.$on('event-changed', function(data){
            $scope.loadLists();
        });

        $scope.showMore = function(){
            $scope.limit+=10;
        }

    }]);
