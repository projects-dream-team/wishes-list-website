var commonApp = angular
    .module(
    'commonApp',
    ['ng', 'ngResource', 'ngTouch', 'ui.bootstrap']
)
    .config([
        '$interpolateProvider', '$httpProvider',
        function($interpolateProvider, $httpProvider) {
            $interpolateProvider.startSymbol('{$');
            $interpolateProvider.endSymbol('$}');
            $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        }
    ]);
