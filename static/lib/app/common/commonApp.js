
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

commonApp.filter('isAfter', function(){
  return function(items, field, isEnabled, dateAfter){
    if (dateAfter == undefined){
        dateAfter = Date.now();
    }
    return isEnabled? items.filter(function(item){
      return moment(item[field]).isAfter(dateAfter);
    }) : items;
  };
});