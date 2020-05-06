odoo.define('aspl_employee_attendance_map.view', function (require) {
"use strict";

	var core = require('web.core');
	var data = require('web.data');
	var ActionManager = require('web.ActionManager');
	var pyUtils = require('web.py_utils');
	var Context = require('web.Context');
	var rpc = require('web.rpc');
	var data_manager = require('web.data_manager');
	var ajax = require('web.ajax');
	var form_widget = require('web.Widget');
	var _t = core._t;

	ActionManager.include({
		_onExecuteAction: function (ev) {
	        ev.stopPropagation();
	        var self = this;
	        var actionData = ev.data.action_data;
	        var env = ev.data.env;
	        var context = new Context(env.context, actionData.context || {});
	        var recordID = env.currentID || null; // pyUtils handles null value, not undefined
	        var def = $.Deferred();

	        // determine the action to execute according to the actionData
	        if (actionData.special) {
	            def = $.when({type: 'ir.actions.act_window_close', infos: 'special'});
	        } else if (actionData.type === 'object') {
	            // call a Python Object method, which may return an action to execute
	            var args = recordID ? [[recordID]] : [env.resIDs];
	            if (actionData.args) {
	                try {
	                    // warning: quotes and double quotes problem due to json and xml clash
	                    // maybe we should force escaping in xml or do a better parse of the args array
	                    var additionalArgs = JSON.parse(actionData.args.replace(/'/g, '"'));
	                    args = args.concat(additionalArgs);
	                } catch (e) {
	                    console.error("Could not JSON.parse arguments", actionData.args);
	                }
	            }
	            args.push(context.eval());
	            if(actionData && actionData.name === "show_map"){
	            	return rpc.query({
		                model: 'employee.attendance.map',
		                method: 'show_map',
		                args: [recordID],
		            }, {
		            	async: false
		            }).then(function (result) {
		            	if(result && result[0]){
	                		if(!result[0].connection){
	                			alert("No inernet connection.");
	                			return false;
	                		}
	                		var lat_long = [];
		                    var str = "";
		                    for(var i=0; i<result.length; i++){
			                    	var exit = true;
				                   	if(result[i].latitude && result[i].longitude){
				                   		if(lat_long.length > 0){
				                   			_.each(lat_long, function(item){						              
				                   				if($.inArray(result[i].latitude, item) !== -1 && $.inArray(result[i].longitude,item) !== -1){
							                   		item[1] = item[1] + 1;
							                   		exit = false;
							                   		return;
				                   				}
				                   			});
				                   		}
				                   		if(exit){
					                   		if(result[i].image)
					                   		{
					                   		 str = "<img class='img-circle' src='data:image/png;base64,"+ result[i].image +"' width='50' height='50'> "
					                   		}
					                   		str += result[i].name
					                   		str += "<button style='margin-left:15px;' title='Attendance Detail' class='btnpopup btn btn-icon fa fa-lg fa-list-ul o_cp_switch_list' data-job_position="+result[i].job_position+" data-dept_id="+result[i].dept_id+" data-date="+result[i].date+" data-cust-id="+result[i].emp_id+" data-btn='30'></button>"
                                            lat_long.push([str,result[i].latitude,result[i].longitude, 0]);
				                   		}
				                   	}
			            		}
		                    if(lat_long.length > 0){
		                    	initialize_gmap(lat_long);
		                    	$('.o_statusbar_buttons > ').prop("disabled", false);
		                    	return true
		                    }else{
		                    	alert("No Record Found")
	                        	if(result && result[0].connection){
	                        		initialize_gmap([]);
	                        		$('.o_statusbar_buttons > ').prop("disabled", false);
		                		}
	                        	return false;
	                        }
	                	}
		            }).fail(function (error, event){
	                	initialize_gmap([]);
	                    if(error.code === -32098) {
	                        alert("Server closed...");
	                        event.preventDefault();
	                   }
	               });
	            }
	            def = this._rpc({
	                route: '/web/dataset/call_button',
	                params: {
	                    args: args,
	                    method: actionData.name,
	                    model: env.model,
	                },
	            });
	        } else if (actionData.type === 'action') {
	            // execute a given action, so load it first
	            def = this._loadAction(actionData.name, _.extend(pyUtils.eval('context', context), {
	                active_model: env.model,
	                active_ids: env.resIDs,
	                active_id: recordID,
	            }));
	        }

	        // use the DropPrevious to prevent from executing the handler if another
	        // request (doAction, switchView...) has been done meanwhile ; execute
	        // the fail handler if the 'call_button' or 'loadAction' failed but not
	        // if the request failed due to the DropPrevious,
	        def.fail(ev.data.on_fail);
	        this.dp.add(def).then(function (action) {
	            // show effect if button have effect attribute
	            // rainbowman can be displayed from two places: from attribute on a button or from python
	            // code below handles the first case i.e 'effect' attribute on button.
	            var effect = false;
	            if (actionData.effect) {
	                effect = pyUtils.py_eval(actionData.effect);
	            }
	            if (action && action.constructor === Object) {
	                // filter out context keys that are specific to the current action, because:
	                //  - wrong default_* and search_default_* values won't give the expected result
	                //  - wrong group_by values will fail and forbid rendering of the destination view
	                var ctx = new Context(
	                    _.object(_.reject(_.pairs(env.context), function (pair) {
	                        return pair[0].match('^(?:(?:default_|search_default_|show_).+|' +
	                                             '.+_view_ref|group_by|group_by_no_leaf|active_id|' +
	                                             'active_ids)$') !== null;
	                    }))
	                );
	                ctx.add(actionData.context || {});
	                ctx.add({active_model: env.model});
	                if (recordID) {
	                    ctx.add({
	                        active_id: recordID,
	                        active_ids: [recordID],
	                    });
	                }
	                ctx.add(action.context || {});
	                action.context = ctx;
	                // in case an effect is returned from python and there is already an effect
	                // attribute on the button, the priority is given to the button attribute
	                action.effect = effect || action.effect;
	            } 
	            else {
	                // if action doesn't return anything, but there is an effect
	                // attribute on the button, display rainbowman
	                action = {
	                    effect: effect,
	                    type: 'ir.actions.act_window_close',
	                };
	            }
	            var options = {on_close: ev.data.on_closed};
	            return self.doAction(action, options).then(ev.data.on_success, ev.data.on_fail);
	        });
	    },
	});

	form_widget.include({
		events: {
	        'click .btnpopup': '_onclick_btnpopup',
	    },
	    _onclick_btnpopup : function(event){
	    	var self = this;
	    	event.handled = false;
	    	if(event.handled !== true) // This will prevent event triggering more then once
        	{
            	event.handled = true;
            	var id = $(event.currentTarget).data('cust-id')
            	var at_date = $(event.currentTarget).data('date')
            	var btn = $(event.currentTarget).data('btn')
            	var job_position = $(event.currentTarget).data('job_position')
            	var dept_id = $(event.currentTarget).data('dept_id')
                if (id && btn){
                    $.ajax({
                        type: "GET",
                        dataType: 'json',
                        url: '/employee_attendance',
                        data: {'employee_id' : id,'date':at_date, 'dept_id':dept_id,'job_position':job_position},
                        success: function(success) {
                            if (success && success.filter_domain){
                                self.do_action({
                                    type: 'ir.actions.act_window',
                                    res_model: "hr.attendance",
                                    name: _t('Employee Attendance'),
                                    views: [[false,"list"]],
                                    domain: success.filter_domain,
                                    target: 'new',
                                });
                            }
                            else{
                                alert("No Employee Found");
                            }
                        },
                    });
				}
			}
	    },
    });
});
