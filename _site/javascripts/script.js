var app = angular.module("website", []);

function MainCtrl($scope) {
}

app.config(function ($routeProvider) {
        // configure routes
        $routeProvider.when("/", {
            templateUrl: "partials/home.html",
            // controller:"MainCtrl"
        })
            .when("/home", {
            templateUrl: "partials/home.html",
            // controller:"MainCtrl"
        })
            .when("/about", {
            templateUrl:"partials/about.html",
            // controller:"AboutCtrl"
        })
            .when("/projects", {
            templateUrl:"partials/projects.html",
            // controller:"ProjectsCtrl"
        })
            .otherwise({redirectTo:"/home", templateUrl: "partials/home.html"});
    });