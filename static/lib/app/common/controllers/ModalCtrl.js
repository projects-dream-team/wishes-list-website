commonApp.controller('ModalCtrl', [
    '$scope', '$rootScope', '$uibModal',
    function($scope, $rootScope, $uibModal) {

        $scope.showModal = function(template, params) {
            $('.collapse.in').collapse('hide');
            $scope.is_active = template;
            if (!params) params = {};
            $scope.additionalData = params.additionalData;
            var modalInstance = $uibModal.open({
                controller: params.controller ? params.controller : 'BaseModalCtrl',
                templateUrl: staticAngular(template + '.html?bust=' + Math.random().toString(36).slice(2)),
                backdropClass: (params.backdropClass ? params.backdropClass : 'portfolio-modal-backdrop'),
                windowClass: (params.windowClass ? params.windowClass: 'portfolio-modal'),
                backdrop: (typeof params.backdrop === 'undefined') ? 'true' : params.backdrop,
                keyboard:(typeof params.keyboard === 'undefined') ? 'true' : params.keyboard,
                size: params.size,
                link: params.link
            });
            modalInstance.extData = params.additionalData;
            modalInstance.result.then(function (data) {
                if(data!=undefined){
                    if(data.callback){
                        data.callback();
                    }
                    $rootScope.$broadcast(data.action, {objType: data.objType, detail: data.detail});
                }
            }, function () {
                //console.log('Modal dismissed at: ' + new Date());
            });
        };

    }
]);
