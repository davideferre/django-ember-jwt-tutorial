/* jshint node: true */

module.exports = function(environment) {
    var ENV = {
        modulePrefix: 'client',
        environment: environment,
        rootURL: '/',
        locationType: 'auto',
        EmberENV: {
            FEATURES: {
            // Here you can enable experimental features on an ember canary build
            // e.g. 'with-controller': true
            },
            EXTEND_PROTOTYPES: {
            // Prevent Ember Data from overriding Date.parse.
                Date: false
            }
        },

        APP: {
            api_authorizer: 'authorizer:token',
            api_host: 'http://localhost:8000',
            api_user_namespace: 'account',
        }
    };

    ENV['ember-simple-auth'] = {
        authorizer: 'authorizer:token',
        crossOriginWhitelist:['*'],
    };

    ENV['ember-simple-auth-token'] = {
        serverTokenEndpoint: 'http://localhost:8000/account/token-auth/',
        identificationField: 'email',
        passwordField: 'password',
        tokenPropertyName: 'token',
        authorizationPrefix: 'JWT ',
        authorizationHeaderName: 'Authorization',
        headers: {},
        refreshAccessTokens: true,
        serverTokenRefreshEndpoint: 'http://localhost:8000/account/token-refresh/',
        tokenExpireName: 'exp',
        refreshLeeway: 600,
        timeFactor: 1000,  // example - set to "1000" to convert incoming seconds to milliseconds.
        crossOriginWhitelist:['*'],
    };

    ENV.i18n = {
        defaultLocale: 'en'
    };

  if (environment === 'development') {
    // ENV.APP.LOG_RESOLVER = true;
    // ENV.APP.LOG_ACTIVE_GENERATION = true;
    // ENV.APP.LOG_TRANSITIONS = true;
    // ENV.APP.LOG_TRANSITIONS_INTERNAL = true;
    // ENV.APP.LOG_VIEW_LOOKUPS = true;
  }

  if (environment === 'test') {
    // Testem prefers this...
    ENV.locationType = 'none';

    // keep test console output quieter
    ENV.APP.LOG_ACTIVE_GENERATION = false;
    ENV.APP.LOG_VIEW_LOOKUPS = false;

    ENV.APP.rootElement = '#ember-testing';
  }

  if (environment === 'production') {

  }

  return ENV;
};
