'use strict';
var packagejson = require('./package.json');
 
module.exports = function (grunt) {
 
  // Configuration
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    watch: {
      coffee: {
        files: ['public/app/**/*.coffee'],
        tasks: 'newer:coffee:glob',
        options: {
          livereload: true,
          header: true,
          interrupt: true,
          atBegin: true

        }
      },
      livereload: {
        files: ['public/css/*'],
        options: {
          interrupt: true,
          livereload: true
        }
      }
    },

    coffee: {
      glob: {
        options: { header: true },
        expand: true,
        cwd: 'public/app',
        src: ['**/*.coffee'],
        dest: 'public/app',
        ext: '.js'
      }
    },

    requirejs: {
      release: {
        options: {
          // Include the main configuration file
          mainConfigFile: 'public/app/config.js',

          // Output file
          out: 'dist/debug/require.js',

          // Root application module
          name: 'config',

          // Do not wrap everything in an IIFE
          wrap: false,
          // Annotate Angular dependency injection
          onBuildRead: function (moduleName, path, contents) {
            return annotate(contents)
          },

          paths: {
            'jquery': 'empty:',
            'angular': 'empty:',
            'd3': 'empty:'
          },

          optimize: 'uglify2'
        }
      }
    },

    uglify: {
      all: {
        options: {
          // Banner that appears at the top of the require file
          banner: '/*\n*\n* <%= pkg.name %> - v<%= pkg.version %>\n*\n' +
            '* <%= pkg.description %>\n*\n' +
            '* Website: <%= pkg.homepage %>\n' +
            '* Author: <%= pkg.author.name %>\n' +
            '* Contributors: <% _.each(pkg.contributors, function(c) { %><%= c.name %>; <% }); %>\n' +
            '* Copyright (c) <%= grunt.template.today("yyyy") %>\n*\n' +
            '* Built on <%= grunt.template.today("dd-mmm-yyyy") %>\n*\n*/',
          compress: true,
          mangle: true
        },
        files: {
          'dist/build/public/built.js': ['dist/debug/full-require.js']
        }
      },
      test: {
        options: {
          // Banner that appears at the top of the require file
          banner: '/*\n*\n* <%= pkg.name %> - v<%= pkg.version %>\n*\n' +
            '* <%= pkg.description %>\n*\n' +
            '* Website: <%= pkg.homepage %>\n' +
            '* Author: <%= pkg.author.name %>\n' +
            '* Contributors: <% _.each(pkg.contributors, function(c) { %><%= c.name %>; <% }); %>\n' +
            '* Copyright (c) <%= grunt.template.today("yyyy") %>\n*\n' +
            '* Built on <%= grunt.template.today("dd-mmm-yyyy") %>\n*\n*/',
          compress: false,
          mangle: false
        },
        files: {
          'dist/build/public/built.js': ['dist/debug/full-require.js']
        }
      }
    },
  });
  
  grunt.registerTask('build', [
    'uglify',
    'requirejs:release'
  ]);
  
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-requirejs');
  grunt.loadNpmTasks('grunt-contrib-coffee');
  grunt.loadNpmTasks('grunt-newer');

};