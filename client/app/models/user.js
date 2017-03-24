import DS from 'ember-data';

export default DS.Model.extend({
    email: DS.attr('string'),
    password: DS.attr('string'),
    first_name: DS.attr('string'),
    last_name: DS.attr('string')
});
