todoApp = angular.module('todoApp', [
  'ngRoute',
  'todoControllers',
])

todoApp.config(['$routeProvider',
  ($routeProvider) ->
    $routeProvider.
      when('/', {
        templateUrl: 'partials/base.html',
        controller: 'IndexController'
      }).
      otherwise({
        redirectTo: '/'
      });
  ]);