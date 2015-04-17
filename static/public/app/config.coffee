# - Everything that can be done with bower has been done with bower
# everything else is in /vendor/ (no registration possible).
# - Some dependencies are registered with bower but have no version "*", this
# means that future upgrade may be dangerous and break things

if window.jQuery
  define('jquery', ->
    window.jQuery
  )

if window.angular
  define('angular', ->
    window.angular
  )

require.config
  waitSeconds: 30
  deps: ["main"]

  paths:
    partials: "../partials"

    jquery: "../lib/jquery/jquery"
    underscore: "../lib/underscore/underscore"
    bootstrap: "../lib/bootstrap/dist/js/bootstrap"
    angular: "../lib/angular/angular"
    angularRoute: '../lib/angular-route/angular-route'

  shim:
    jquery:
      exports: "jQuery"
    underscore:
      exports: "_"
    angular:
      exports: "angular"
      deps: ["jquery"] # replace jqLite
    bootstrap:
      deps: ["jquery"]
    jqueryUi:
      dep: ["jquery"]
    angularRoute:
      deps: ["angular"]

