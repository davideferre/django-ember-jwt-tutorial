import Ember from 'ember';

export default Ember.Controller.extend({
    actions: {
        register(){
            let form_data = this.getProperties('first_name', 'last_name', 'email', 'password');
            let user = this.get('store').createRecord('user', {
                email: form_data.email,
                password: form_data.password,
                first_name: form_data.first_name,
                last_name: form_data.last_name
            });

            let self = this;

            function transitionToLogin() {
                self.transitionToRoute('login');
            }

            function failure(reason) {
                // handle the error
                console.error(reason);
            }

            user.save().then(transitionToLogin).catch(failure);
        }
    }
});
