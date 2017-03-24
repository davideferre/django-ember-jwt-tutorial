import Ember from 'ember';

export default Ember.Controller.extend({
    session: Ember.inject.service(),
    notify: Ember.inject.service('notify'),
    i18n: Ember.inject.service('i18n'),
    actions: {
        authenticate() {
            let notify = this.get('notify');
            let i18n = this.get('i18n');
            let credentials = this.getProperties('identification', 'password');
            let authenticator = 'authenticator:jwt';
            this.get('session').authenticate(authenticator, credentials).catch(function(){
                notify.alert(i18n.t('login.controller.messages.authenticate_error'));
                Ember.$('#password').val('');
            });
        }
    }
});
