odoo.define('user_activities_tracking.CustomUserMenu', function (require) {
var UserMenu = require('web.UserMenu');

var CustomUserMenu = UserMenu.include({
    template: 'UserMenu',

    _onMenuActivity: function () {
        var self = this;
        var session = this.getSession();
        this.trigger_up('clear_uncommitted_changes', {
            callback: function () {
                self._rpc({
                        route: "/web/action/load",
                        params: {
                            action_id: "user_activities_tracking.action_user_activity",
                        },
                    })
                    .done(function (result) {
                        result.res_id = session.uid;
                        self.do_action(result);
                    });
            },
        });
    },
})

return CustomUserMenu;

});