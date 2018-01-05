'use strict';

// Declare app level module which depends on views, and components
var app = angular.module('myApp', [
    'ui.router',
    'myApp.home',
    'myApp.pitchedRoofs',
    'myApp.flatRoofs',
    'myApp.groundBased',
    'myApp.productView',
    'myApp.footTrafficMap',
    'myApp.company',
    'myApp.map'
]).config(['$locationProvider', '$routeProvider', '$stateProvider', '$urlRouterProvider', function ($locationProvider, $routeProvider, $stateProvider, $urlRouterProvider) {
    //$locationProvider.hashPrefix('!');
    $routeProvider.otherwise({redirectTo: '/home'});
    $stateProvider.state("home", {
        url: "/home",
        templateUrl: "./home/home-view.html",
        controller: "HomeController"
    })
    .state("pitchedRoofs", {
        url: "/pitched-roofs",
        templateUrl: "./pitchedRoofs/pitched-roofs-view.html",
        controller: "PitchedRoofsController"
    })
    .state("flatRoofs", {
        url: "/flat-roofs",
        templateUrl: "./scripts/common/views/flat-roofs.html"
    })
    .state("GroundBased", {
        url: "/ground-based",
        templateUrl: "./scripts/common/views/ground-based.html"
    })
    .state("company", {
        url: "/company",
        templateUrl: "./company/company-view.html",
        controller: "CompanyController"
    })
    .state("contact", {
        url: "/contact",
        templateUrl: "./contact/contact-view.html",
        controller: "ContactController"
    })
    .state("map", {
        url: "/map",
        templateUrl: "./map/map-view.html",
        controller: "FootTrafficMapController"
    });
    $urlRouterProvider.otherwise('/map');
}]);
