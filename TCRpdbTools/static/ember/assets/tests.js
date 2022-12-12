'use strict';

define("tcrpdb/tests/helpers/index", ["exports", "ember-qunit"], function (_exports, _emberQunit) {
  "use strict";

  Object.defineProperty(_exports, "__esModule", {
    value: true
  });
  _exports.setupApplicationTest = setupApplicationTest;
  _exports.setupRenderingTest = setupRenderingTest;
  _exports.setupTest = setupTest;
  0; //eaimeta@70e063a35619d71f0,"ember-qunit"eaimeta@70e063a35619d71f
  // This file exists to provide wrappers around ember-qunit's / ember-mocha's
  // test setup functions. This way, you can easily extend the setup that is
  // needed per test type.

  function setupApplicationTest(hooks, options) {
    (0, _emberQunit.setupApplicationTest)(hooks, options);

    // Additional setup for application tests can be done here.
    //
    // For example, if you need an authenticated session for each
    // application test, you could do:
    //
    // hooks.beforeEach(async function () {
    //   await authenticateSession(); // ember-simple-auth
    // });
    //
    // This is also a good place to call test setup functions coming
    // from other addons:
    //
    // setupIntl(hooks); // ember-intl
    // setupMirage(hooks); // ember-cli-mirage
  }

  function setupRenderingTest(hooks, options) {
    (0, _emberQunit.setupRenderingTest)(hooks, options);

    // Additional setup for rendering tests can be done here.
  }

  function setupTest(hooks, options) {
    (0, _emberQunit.setupTest)(hooks, options);

    // Additional setup for unit tests can be done here.
  }
});
define("tcrpdb/tests/integration/components/pdb-choices-test", ["@ember/template-factory", "qunit", "tcrpdb/tests/helpers", "@ember/test-helpers"], function (_templateFactory, _qunit, _helpers, _testHelpers) {
  "use strict";

  0; //eaimeta@70e063a35619d71f0,"qunit",0,"tcrpdb/tests/helpers",0,"@ember/test-helpers",0,"ember-cli-htmlbars"eaimeta@70e063a35619d71f
  (0, _qunit.module)('Integration | Component | pdb-choices', function (hooks) {
    (0, _helpers.setupRenderingTest)(hooks);
    (0, _qunit.test)('it renders', async function (assert) {
      // Set any properties with this.set('myProperty', 'value');
      // Handle any actions with this.set('myAction', function(val) { ... });

      await (0, _testHelpers.render)((0, _templateFactory.createTemplateFactory)(
      /*
        <PdbChoices />
      */
      {
        "id": "aWoiJ/WQ",
        "block": "[[[8,[39,0],null,null,null]],[],false,[\"pdb-choices\"]]",
        "moduleName": "(unknown template module)",
        "isStrictMode": false
      }));
      assert.dom(this.element).hasText('');

      // Template block usage:
      await (0, _testHelpers.render)((0, _templateFactory.createTemplateFactory)(
      /*
        
            <PdbChoices>
              template block text
            </PdbChoices>
          
      */
      {
        "id": "ZbCMjFeM",
        "block": "[[[1,\"\\n      \"],[8,[39,0],null,null,[[\"default\"],[[[[1,\"\\n        template block text\\n      \"]],[]]]]],[1,\"\\n    \"]],[],false,[\"pdb-choices\"]]",
        "moduleName": "(unknown template module)",
        "isStrictMode": false
      }));
      assert.dom(this.element).hasText('template block text');
    });
  });
});
define("tcrpdb/tests/integration/components/protein-viewer-test", ["@ember/template-factory", "qunit", "tcrpdb/tests/helpers", "@ember/test-helpers"], function (_templateFactory, _qunit, _helpers, _testHelpers) {
  "use strict";

  0; //eaimeta@70e063a35619d71f0,"qunit",0,"tcrpdb/tests/helpers",0,"@ember/test-helpers",0,"ember-cli-htmlbars"eaimeta@70e063a35619d71f
  (0, _qunit.module)('Integration | Component | protein-viewer', function (hooks) {
    (0, _helpers.setupRenderingTest)(hooks);
    (0, _qunit.test)('it renders', async function (assert) {
      // Set any properties with this.set('myProperty', 'value');
      // Handle any actions with this.set('myAction', function(val) { ... });

      await (0, _testHelpers.render)((0, _templateFactory.createTemplateFactory)(
      /*
        <ProteinViewer />
      */
      {
        "id": "lvWJQe9Z",
        "block": "[[[8,[39,0],null,null,null]],[],false,[\"protein-viewer\"]]",
        "moduleName": "(unknown template module)",
        "isStrictMode": false
      }));
      assert.dom(this.element).hasText('');

      // Template block usage:
      await (0, _testHelpers.render)((0, _templateFactory.createTemplateFactory)(
      /*
        
            <ProteinViewer>
              template block text
            </ProteinViewer>
          
      */
      {
        "id": "FSNpvEVi",
        "block": "[[[1,\"\\n      \"],[8,[39,0],null,null,[[\"default\"],[[[[1,\"\\n        template block text\\n      \"]],[]]]]],[1,\"\\n    \"]],[],false,[\"protein-viewer\"]]",
        "moduleName": "(unknown template module)",
        "isStrictMode": false
      }));
      assert.dom(this.element).hasText('template block text');
    });
  });
});
define("tcrpdb/tests/integration/components/tcrrequest-form-test", ["@ember/template-factory", "qunit", "tcrpdb/tests/helpers", "@ember/test-helpers"], function (_templateFactory, _qunit, _helpers, _testHelpers) {
  "use strict";

  0; //eaimeta@70e063a35619d71f0,"qunit",0,"tcrpdb/tests/helpers",0,"@ember/test-helpers",0,"ember-cli-htmlbars"eaimeta@70e063a35619d71f
  (0, _qunit.module)('Integration | Component | tcrrequest-form', function (hooks) {
    (0, _helpers.setupRenderingTest)(hooks);
    (0, _qunit.test)('it renders', async function (assert) {
      // Set any properties with this.set('myProperty', 'value');
      // Handle any actions with this.set('myAction', function(val) { ... });

      await (0, _testHelpers.render)((0, _templateFactory.createTemplateFactory)(
      /*
        <TcrrequestForm />
      */
      {
        "id": "bCU3qpJi",
        "block": "[[[8,[39,0],null,null,null]],[],false,[\"tcrrequest-form\"]]",
        "moduleName": "(unknown template module)",
        "isStrictMode": false
      }));
      assert.dom(this.element).hasText('');

      // Template block usage:
      await (0, _testHelpers.render)((0, _templateFactory.createTemplateFactory)(
      /*
        
            <TcrrequestForm>
              template block text
            </TcrrequestForm>
          
      */
      {
        "id": "xofOY04C",
        "block": "[[[1,\"\\n      \"],[8,[39,0],null,null,[[\"default\"],[[[[1,\"\\n        template block text\\n      \"]],[]]]]],[1,\"\\n    \"]],[],false,[\"tcrrequest-form\"]]",
        "moduleName": "(unknown template module)",
        "isStrictMode": false
      }));
      assert.dom(this.element).hasText('template block text');
    });
  });
});
define("tcrpdb/tests/test-helper", ["tcrpdb/app", "tcrpdb/config/environment", "qunit", "@ember/test-helpers", "qunit-dom", "ember-qunit"], function (_app, _environment, QUnit, _testHelpers, _qunitDom, _emberQunit) {
  "use strict";

  0; //eaimeta@70e063a35619d71f0,"tcrpdb/app",0,"tcrpdb/config/environment",0,"qunit",0,"@ember/test-helpers",0,"qunit-dom",0,"ember-qunit"eaimeta@70e063a35619d71f
  (0, _testHelpers.setApplication)(_app.default.create(_environment.default.APP));
  (0, _qunitDom.setup)(QUnit.assert);
  (0, _emberQunit.start)();
});
define("tcrpdb/tests/unit/controllers/index-test", ["qunit", "tcrpdb/tests/helpers"], function (_qunit, _helpers) {
  "use strict";

  0; //eaimeta@70e063a35619d71f0,"qunit",0,"tcrpdb/tests/helpers"eaimeta@70e063a35619d71f
  (0, _qunit.module)('Unit | Controller | index', function (hooks) {
    (0, _helpers.setupTest)(hooks);

    // TODO: Replace this with your real tests.
    (0, _qunit.test)('it exists', function (assert) {
      let controller = this.owner.lookup('controller:index');
      assert.ok(controller);
    });
  });
});
define("tcrpdb/tests/unit/routes/account-test", ["qunit", "tcrpdb/tests/helpers"], function (_qunit, _helpers) {
  "use strict";

  0; //eaimeta@70e063a35619d71f0,"qunit",0,"tcrpdb/tests/helpers"eaimeta@70e063a35619d71f
  (0, _qunit.module)('Unit | Route | account', function (hooks) {
    (0, _helpers.setupTest)(hooks);
    (0, _qunit.test)('it exists', function (assert) {
      let route = this.owner.lookup('route:account');
      assert.ok(route);
    });
  });
});
define("tcrpdb/tests/unit/routes/admin-test", ["qunit", "tcrpdb/tests/helpers"], function (_qunit, _helpers) {
  "use strict";

  0; //eaimeta@70e063a35619d71f0,"qunit",0,"tcrpdb/tests/helpers"eaimeta@70e063a35619d71f
  (0, _qunit.module)('Unit | Route | admin', function (hooks) {
    (0, _helpers.setupTest)(hooks);
    (0, _qunit.test)('it exists', function (assert) {
      let route = this.owner.lookup('route:admin');
      assert.ok(route);
    });
  });
});
define("tcrpdb/tests/unit/routes/index-test", ["qunit", "tcrpdb/tests/helpers"], function (_qunit, _helpers) {
  "use strict";

  0; //eaimeta@70e063a35619d71f0,"qunit",0,"tcrpdb/tests/helpers"eaimeta@70e063a35619d71f
  (0, _qunit.module)('Unit | Route | index', function (hooks) {
    (0, _helpers.setupTest)(hooks);
    (0, _qunit.test)('it exists', function (assert) {
      let route = this.owner.lookup('route:index');
      assert.ok(route);
    });
  });
});
define("tcrpdb/tests/unit/routes/not-found-test", ["qunit", "tcrpdb/tests/helpers"], function (_qunit, _helpers) {
  "use strict";

  0; //eaimeta@70e063a35619d71f0,"qunit",0,"tcrpdb/tests/helpers"eaimeta@70e063a35619d71f
  (0, _qunit.module)('Unit | Route | not-found', function (hooks) {
    (0, _helpers.setupTest)(hooks);
    (0, _qunit.test)('it exists', function (assert) {
      let route = this.owner.lookup('route:not-found');
      assert.ok(route);
    });
  });
});
define('tcrpdb/config/environment', [], function() {
  var prefix = 'tcrpdb';
try {
  var metaName = prefix + '/config/environment';
  var rawConfig = document.querySelector('meta[name="' + metaName + '"]').getAttribute('content');
  var config = JSON.parse(decodeURIComponent(rawConfig));

  var exports = { 'default': config };

  Object.defineProperty(exports, '__esModule', { value: true });

  return exports;
}
catch(err) {
  throw new Error('Could not read config from meta tag with name "' + metaName + '".');
}

});

require('tcrpdb/tests/test-helper');
EmberENV.TESTS_FILE_LOADED = true;
//# sourceMappingURL=tests.map
