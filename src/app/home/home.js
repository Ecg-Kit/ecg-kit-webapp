(function() {
    'use strict';

    angular
        .module('app.home')
        .controller('Home', Dashboard);

    Dashboard.$inject = ['$q', 'dataservice', 'logger'];

    function Dashboard($q, dataservice, logger) {
    }
})();
