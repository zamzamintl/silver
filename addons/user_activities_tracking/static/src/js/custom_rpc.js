odoo.define('user_activities_tracking.CustomBasicModel', function (require) {

    console.log('Hellllo')

    var FormController = require('web.FormController');
    var BasicModel = require('web.BasicModel');

//    FormController.include({
//
//        _onDeletedRecords: function () {
//
//            this._super.apply(this, arguments)
//            var self = this
//            var record = self.renderer.state
//            console.log('record',record)
//            self._rpc({
//                        model: 'user.recent.log',
//                        method: 'get_recent_log',
//                        args: [record.model, record.res_id, false,'delete'],
//                    }).then(function(){
//                        console.log('Successfully Created log');
//                    });
//
//        },
//
//
//    });

    BasicModel.include({
        _fetchRecord: function (record, options) {
            var _super = this._super.bind(this);
            var changes = window.Changes;
            window.Changes = false;
            if (changes){
                console.log("Yes")
                this._rpc({
                        model: 'user.recent.log',
                        method: 'get_recent_log',
                        args: [record.model, record.res_id, changes],
                    });
            }
            return _super(record, options);
        },

        _generateChanges: function (record, options) {
            var _super = this._super.bind(this);
            var res = _super(record, options);
            window.Changes = res
            return res
        },

    })
});
