'use strict';

// Declare app level module which depends on views, and components
var app = angular.module('myApp', [ 'ui.router', 'ngRoute', 'myApp.home', 'myApp.map', 'myApp.footTrafficMap'])
    .config(['$locationProvider', '$routeProvider', '$stateProvider', '$urlRouterProvider', function ($locationProvider, $routeProvider, $stateProvider, $urlRouterProvider) {
    //$locationProvider.hashPrefix('!');
    $routeProvider.otherwise({redirectTo: '/home'});
    $stateProvider.state("home", {
        url: "/home",
        templateUrl: "./home/home-view.html",
        controller: "HomeController"
    })
    .state("map", {
        url: "/map",
        templateUrl: "./map/map-view.html",
        controller: "FootTrafficMapController"
    });
    $urlRouterProvider.otherwise('/map');
}]);
