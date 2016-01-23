commonApp.controller('FriendsCtrl',
    ['$rootScope', '$http', '$scope', '$window', '$filter', 'CurrentUserService', 'FriendsService',
    function($rootScope, $http, $scope, $window, $filter, CurrentUserService, FriendsService) {


        $scope.requests = [];
        $scope.friends = [];
        $scope.users = [];
        $scope.loadFailed = false;
        $scope.gatheringData = true;
        $scope.limitFriends = 10;
        $scope.limitRequests = 10;
        $scope.searchString = '';
        $scope.initData = function(userId){
                $scope.userId = userId;
                $scope.loadLists();
            };

        $scope.loadRequests = function(){
            $scope.gatheringData = true;
            FriendsService.getRequests().success(function(data){
                $scope.requests = data;

                $scope.gatheringData = false;
            }).error(function(error){
                $scope.loadFailed = true;
            });
        };

        $scope.searchFriends = function(){
            $scope.gatheringData = true;
            FriendsService.getRequests().success(function(data){
                $scope.requests = data;

                $scope.gatheringData = false;
            }).error(function(error){
                $scope.loadFailed = true;
            });
        };

        $scope.loadFriends = function(){
            $scope.gatheringData = true;
            FriendsService.getFriends().success(function(data){
                $scope.friends = data;

                $scope.gatheringData = false;
            }).error(function(error){
                $scope.loadFailed = true;
            });
        };

        $scope.accept = function(friendship) {
            $scope.gatheringData = true;
            friendship.is_active=true;
            console.log(friendship);
            FriendsService.accept(friendship.id,friendship).success(function(data){
                $rootScope.$broadcast('frendship-changed');

                $scope.gatheringData = false;
            }).error(function(error){
                $scope.loadFailed = true;
            });
        };

        $scope.decline = function(friendship) {
            FriendsService.decline(friendship.id).success(function(data){
                $rootScope.$broadcast('frendship-changed');
                $scope.success = true;
                $scope.gatheringData = false;
            }).error(function(error){
                $scope.loadFailed = true;
            });
        };


        $scope.$on('frendship-changed', function(data){
            $scope.loadRequests();
            $scope.loadFriends();
        });

        $scope.showMoreFriends = function(){
            $scope.limit+=10;
        };

        $scope.showMoreRequests = function(){
            $scope.limit+=10;
        };

         $scope.searchSpecyfic = function(item){
            if ( (item.friend_nick.indexOf($scope.query) != -1) || (item.owner_nick.indexOf($scope.query) != -1) ){
                return true;
            }
            return false;
         };
    }]);
