odoo.define('danfresh_extention.sysactivity', function (require) {
"use strict";

var ActivityMenu = require('mail.systray.ActivityMenu');

var core = require('web.core');
//var datepicker = require('web.datepicker');

var _t = core._t;

ActivityMenu.include({
    events: _.extend({}, ActivityMenu.prototype.events, {
        'click .o_activity_show': '_onAddActivityClick',
    }),

    _onAddActivityClick: function () {
        var self = this;
        self._rpc({
            model: "hr.employee",
            method: 'get_activity_context',
            args: []
        }).then(function (context) {
            console.log('context=',context)
             self.do_action('danfresh_extention.add_new_activity_action',{
                 additional_context: {
                        default_res_model_id: context.default_res_model_id,
                        default_res_id: context.default_res_id,
                    }
             });
        });

    },

});
});
