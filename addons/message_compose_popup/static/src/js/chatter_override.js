odoo.define('message_compose_popup.mail.Chatter', function (require) {
    "use strict";

    var mailChatter = require('mail.Chatter');
    var ChatterComposer = require('mail.composer.Chatter');

    mailChatter.include({

        //--------------------------------------------------------------------------
        // Private
        //--------------------------------------------------------------------------

        /**
        * Override openComposer method
        *
        * @override
        * @private
        */
        _openComposer: function (options) {
            var self = this;
            var oldComposer = this._composer;
            // create the new composer
            this._composer = new ChatterComposer(this, this.record.model, options.suggested_partners || [], {
                commandsEnabled: false,
                context: this.context,
                inputMinHeight: 50,
                isLog: options && options.isLog,
                recordName: this.recordName,
                defaultBody: oldComposer && oldComposer.$input && oldComposer.$input.val(),
                defaultMentionSelections: oldComposer && oldComposer.getMentionListenerSelections(),
                attachmentIds: (oldComposer && oldComposer.get('attachment_ids')) || [],
            });
            if (!options.isLog)
                this._composer._onOpenFullComposer();

            this._composer.on('input_focused', this, function () {
                this._composer.mentionSetPrefetchedPartners(this._mentionSuggestions || []);
            });

            this._composer.insertAfter(this.$('.o_chatter_topbar')).then(function () {

            });

            if (!options.isLog)
                self._closeComposer(true);

        },
    });

});