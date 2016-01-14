var commonApp = angular
    .module(
    'commonApp',
    ['ng', 'ngResource', 'ngTouch', 'ui.bootstrap']
)
    .config([
        '$interpolateProvider',
        function($interpolateProvider, $httpProvider) {
            $interpolateProvider.startSymbol('{$');
            $interpolateProvider.endSymbol('$}');
        }
    ])
