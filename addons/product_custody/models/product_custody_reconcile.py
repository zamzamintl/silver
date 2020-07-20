import json
import time
from datetime import date
from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.tools.float_utils import float_compare, float_is_zero, float_round
from odoo.exceptions import UserError ,ValidationError



class ProductCustodyReconcile(models.Model):
    _name= "product.custody.reconcile"
    _inherit = ['mail.thread']
    name = fields.Char(string='Custody #', size=64,readonly=True, default=lambda *a: '/')
    product_id = fields.Many2one('product.product', string="Product Name" , required=True)
    quantity = fields.Float()
    custody_id = fields.Many2one("product.custody",required=True,domain="[('employee_id','=',employee_id),('state','=','Assigned')]")
    state = fields.Selection([('New', 'New'),('Sent / Waiting','Sent & Waiting'),
                              ('Delivered', 'Delivered'), ('Canceled', 'Canceled') ], track_visibility='onchange',default ='New')
    company_id = fields.Many2one('res.company',string='Company', readonly=True, copy=False,
        default=lambda self: self.env['res.company']._company_default_get(),)
    location_id = fields.Many2one('stock.location',string="Location SRC")
    # location = fields.Many2one('stock.location',string="Location",domain="[('usage','=','view')]")
    location_dst_id = fields.Many2one('stock.location','Location Dst')
    picking_type_id = fields.Many2one('stock.picking.type',)
    used_by = fields.Selection([('Employee', 'Employee'), ('Department', 'Department'), ],  default='Employee')
    employee_id = fields.Many2one("hr.employee",required=True)
    department_id = fields.Many2one('hr.department', string='Department')
    technician = fields.Many2one('res.users',string="Requested By",default=lambda self :self.env.uid , readonly=True)
    # d_date = fields.Date(readonly=True)
    request_date = fields.Date(readonly=True , default= date.today())
    note = fields.Text(string="Description")

     
    def unlink(self):
        for rec in self.filtered(lambda custody: custody.state not in ['Draft']):
            raise UserError(_('You can not delete a custody which is in "Not Draft" state !!'))
        return super(ProductCustodyReconcile, self).unlink()

    def get_domain(self):
        if self.employee_id.id:
            domain = "[('employee_id','=',employee_id)]"
            return domain
        else:
            return "[]"

    @api.model
    def create(self, vals):
        sequence = self.env['ir.sequence'].next_by_code('product.custody.reconcile')
        vals['name'] = sequence
        custody = super(ProductCustodyReconcile, self).create(vals)
        return custody

    @api.constrains('quantity')
    def _check_quantity(self):
        if self.quantity <= 0:
            raise ValidationError(_('You cannot create request with  " quantity < 0 " . '))

    def send_stock_req(self):
        # self.get_inventory_locations()
        print("i am in stock ")
        user_id = self.env['res.partner'].search([('name', 'ilike', self.technician.name)],limit=1)
        product_id = self.product_id
        print("before create",self.picking_type_id.id,self.location_id.id, self.location_dst_id.id)
        picking_out = self.env['stock.picking'].create({
            'partner_id': user_id.id,
            'state': 'draft',
            'origin':self.name,
            'picking_type_id': self.picking_type_id.id,
            'location_id': self.location_id.id,
            'location_dest_id': self.location_dst_id.id,
            'move_lines': [],
        })
        print("after create")
        self.env['stock.move'].create({
            'name': product_id.name,
            'product_id': product_id.id,
            'product_uom_qty': self.quantity,
            'product_uom': product_id.uom_id.id,
            'picking_id': picking_out.id,
            'location_id': self.location_id.id,
            'location_dest_id': self.location_dst_id.id,
        })
        picking_out.action_confirm()
        self.state = "Sent / Waiting"

    def check_delivering(self):
        stock_req = self.env['stock.picking'].search([('origin','like',self.name)])
        print(stock_req.state)
        if stock_req.state == 'done':
            self.state = 'Delivered'
            self.set_reconcile_custody()

        else:
            self.state = "Sent / Waiting"
            print(" i am in run")
            view = self.env.ref('product_custody.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = "your request is sent and the product is reviewing"
            return {
                'name': "Success",
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'sh.message.wizard',
                'views': [(view.id, 'form')],
                'view_id': view.id,
                'target': 'new',
                'context': context,
            }

    def set_reconcile_custody(self):
        custody_id = self.env['product.custody'].search([('id','=',self.custody_id.id),('company_id','=',self.company_id.id)])
        custody_id.write({'state':"Reconciled"
                          })
    def receive_product(self):
        self.state = "Delivered"

    def cancel_progress(self):
        self.state = "Canceled"

    def get_inventory_locations(self):
        user_company = self.env.user.company_id.id
        print(user_company, self.env.user.company_id, self.env.user.company_id.name)
        company_partner = self.env['res.company'].search([('id', '=', user_company)], limit=1)
        print(company_partner, "company_partner")
        warehouse_id = self.env['stock.warehouse'].search([('company_id', '=', company_partner.id)], limit=1)
        print("wearwhouse id ", warehouse_id)
        operation_type_ids = self.env['stock.picking.type'].search([('warehouse_id', '=', warehouse_id.id)])
        operation_id = self.env['stock.picking.type']
        # for op in operation_type_ids:
        #     print(op.id)
        #     print(op.name)
            # if op.name == 'Receipts':
            #     print("i am in delivery order")
            #     operation_id = op.id
            #     self.picking_type_id = operation_id
            #     if op.custody_stock_src_id:
            #         self.location_id = op.custody_stock_src_id.id
            #     else:
            #         raise ValidationError(_('you should add default custody Source Location'))
            #     if op.custody_stock_dst_id.id:
            #         self.location_dst_id = op.custody_stock_dst_id.id
            #     else:
            #         raise ValidationError(_('you should add default custody Destination Location'))

    @api.onchange('custody_id')
    def custody_id_onchange(self):
        if self.custody_id :
            self.product_id = self.custody_id.product_id
            self.employee_id = self.custody_id.employee_id
            self.quantity = self.custody_id.quantity
            self.location_dst_id = self.custody_id.location_id
            self.location_id = self.custody_id.location_dst_id


class StockPickingCustody(models.Model):
    _inherit = "stock.picking"

    
    def action_done(self):
        """Changes picking state to done by processing the Stock Moves of the Picking

        Normally that happens when the button "Done" is pressed on a Picking view.
        @return: True
        """
        # TDE FIXME: remove decorator when migration the remaining
        todo_moves = self.mapped('move_lines').filtered(
            lambda self: self.state in ['draft', 'waiting', 'partially_available', 'assigned', 'confirmed'])
        # Check if there are ops not linked to moves yet
        for pick in self:
            # # Explode manually added packages
            # for ops in pick.move_line_ids.filtered(lambda x: not x.move_id and not x.product_id):
            #     for quant in ops.package_id.quant_ids: #Or use get_content for multiple levels
            #         self.move_line_ids.create({'product_id': quant.product_id.id,
            #                                    'package_id': quant.package_id.id,
            #                                    'result_package_id': ops.result_package_id,
            #                                    'lot_id': quant.lot_id.id,
            #                                    'owner_id': quant.owner_id.id,
            #                                    'product_uom_id': quant.product_id.uom_id.id,
            #                                    'product_qty': quant.qty,
            #                                    'qty_done': quant.qty,
            #                                    'location_id': quant.location_id.id, # Could be ops too
            #                                    'location_dest_id': ops.location_dest_id.id,
            #                                    'picking_id': pick.id
            #                                    }) # Might change first element
            # # Link existing moves or add moves when no one is related
            for ops in pick.move_line_ids.filtered(lambda x: not x.move_id):
                # Search move with this product
                moves = pick.move_lines.filtered(lambda x: x.product_id == ops.product_id)
                moves = sorted(moves, key=lambda m: m.quantity_done < m.product_qty, reverse=True)
                if moves:
                    ops.move_id = moves[0].id
                else:
                    new_move = self.env['stock.move'].create({
                        'name': _('New Move:') + ops.product_id.display_name,
                        'product_id': ops.product_id.id,
                        'product_uom_qty': ops.qty_done,
                        'product_uom': ops.product_uom_id.id,
                        'location_id': pick.location_id.id,
                        'location_dest_id': pick.location_dest_id.id,
                        'picking_id': pick.id,
                        'picking_type_id': pick.picking_type_id.id,
                    })
                    ops.move_id = new_move.id
                    new_move._action_confirm()
                    todo_moves |= new_move
                    # 'qty_done': ops.qty_done})
        todo_moves._action_done()
        self.set_reconciliation_delivered()
        self.write({'date_done': fields.Datetime.now()})
        return True

    def set_reconciliation_delivered(self):
        print("calling reconicle deleveer")
        reconcile_obj= self.env['product.custody.reconcile'].search([('name','=',self.origin),('company_id','=',self.company_id.id)])
        if reconcile_obj:
            print(reconcile_obj.name,reconcile_obj.product_id)
            reconcile_obj.state = "Delivered"
            reconcile_obj.set_reconcile_custody()

