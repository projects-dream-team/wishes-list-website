commonApp.controller('BaseModalCtrl', [ '$scope', 'ModalService',
  function ($scope, ModalService, additionalData) {

  $scope.additionalData = additionalData;

  $scope.ok = function () {
    $uibModalInstance.close($scope.selected.item);
  };

  $scope.close = function () {
    $uibModalInstance.dismiss('cancel');
  };
}]);