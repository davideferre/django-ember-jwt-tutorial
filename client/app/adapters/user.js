import ApplicationAdapter from './application';
import config from '../config/environment';

export default ApplicationAdapter.extend({
    namespace: config.APP.api_user_namespace,
});
