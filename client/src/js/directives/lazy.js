/**
 * @ngdoc function
 * @name miller.directives:lazy
 * @description
 * # marked
 * transform markdown data in miller enhanced datas
 */
angular.module('miller')
  .directive('lazyImage', function ($log) {
    return {
      restrict : 'A',
      scope: {
        src: '='
      },
      link : function(scope, element, attrs) {
        $log.log(':::lazy on ',scope.src);

        element.addClass('lazy-box').css({
          'background-color': '#B7B2B2',
        }).html('<div class="loading">...</div>');
        
        function wakeup(){
          element.css({
            'background-size': attrs.size || 'cover',
            'background-position': 'center center',
            'background-repeat': 'no-repeat',
            'background-image': 'url(' + scope.src + ')'
          });
          element.find('.loading').hide();
        }

        scope.$watch('src', function(v){
          if(v)
            wakeup(); // or start watching for in page
        });

      }
    };
  })
  /*
    lazy placeholder for document or for stories, filled when needed only.
  */
  .directive('lazyPlaceholder', function($log, $rootScope, $compile, RUNTIME) {
    return {
      //transclude: true,
      scope:{
        
      },
      templateUrl: RUNTIME.static + 'templates/partials/placeholder.html',
      link : function(scope, element, attrs) {
        var slug = element.attr('lazy-placeholder'),
            type = element.attr('type');

        scope.type = type;
        
        $log.log('⏣ lazy-placeholder on type:', type, '- slug:',slug);
        
        scope.complete = function(res){
          // add to this local scope
          if(res){
            scope.resolved = res;
            $log.log('⏣ lazy-placeholder resolved for type:', type, '- slug:',slug, res);
            // force recompilation
            $compile(element.contents())(scope);
          } else {
            $log.error('⏣ lazy-placeholder cannot find', slug );
          }
        }

        if($rootScope.resolve && typeof slug=='string'){
          $rootScope.resolve(slug, type, scope.complete);
        }

        scope.fullsize = function(slug, type){
          $rootScope.fullsize(slug, type);
        }
        
      }
    }
  });