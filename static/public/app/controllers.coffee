todoControllers = angular.module('todoControllers', [])

todoControllers.controller('IndexController', ['$scope', '$http', ($scope, $http) ->
    $scope.items = ["1": {name: "item no 1", descrption: "stuff to do"}]
  ])
