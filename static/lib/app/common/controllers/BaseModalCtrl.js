commonApp.controller('BaseModalCtrl', [ '$scope', '$uibModalInstance',
  function ($scope,  $uibModalInstance) {

  $scope.ok = function () {
    $uibModalInstance.close($scope.selected.item);
  };

  $scope.close = function () {
    $uibModalInstance.dismiss('cancel');
  };
}]);