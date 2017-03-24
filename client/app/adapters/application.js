import DS from 'ember-data';
import DataAdapterMixin from 'ember-simple-auth/mixins/data-adapter-mixin';
import config from '../config/environment';

export default DS.JSONAPIAdapter.extend(DataAdapterMixin, {
    authorizer: config.APP.api_authorizer,
    host: config.APP.api_host,
    buildURL(type, id, record) {
        //call the default buildURL and then append a slash
        return this._super(type, id, record) + '/';
    }
});
