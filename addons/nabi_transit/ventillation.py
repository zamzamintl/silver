# -*- coding: utf-8 -*-
from openerp.osv import fields, osv


class repertoire(osv.osv):
    _name = 'repertoire'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Order Reference must be unique !'),
    ]
    _columns ={
        'state'         : fields.selection(selection = [('new',u'Nouveau'),('valide',u'Terminé'),('cancel',u'Annulé')], string="Etat", default="new", track_visibility='always'),  
        'attachment_ids': fields.many2many('ir.attachment', 'repertoire_attachments_rel', 'repertoire_id', 'attachment_id', 'Attachments',track_visibility='always'),
	    'name' 		    : fields.char(u"No. ordre" ,default="/"),
	    'declarant' 	: fields.many2one('res.users',u"Déclarant"),
	    'bureau' 		: fields.char(u"Bureau"),
	    'regime' 		: fields.char(u"Régime"),
	    'dum' 		    : fields.char(u"DUM"),
	    'lettre' 		: fields.char(u"Lettre"),
	    'selectivite' 	: fields.char(u"Sélectivité TI"),
	    'date' 		    : fields.date(u"Date",track_visibility='always'),
	    'client' 		: fields.many2one('res.partner',u"Client  ",track_visibility='always'),
	    'fournisseur' 	: fields.many2one('res.partner',u"Fournisseur",track_visibility='always'),
	    'colis' 		: fields.char(u"Colis",track_visibility='always'),
	    'p_brut' 		: fields.float(u"P.Brut",track_visibility='always'),
	    'taux' 		    : fields.float(u"Cours de change",track_visibility='always'),
	    'montant' 		: fields.float(u"Montant",track_visibility='always'),
	    'ei' 		    : fields.char(u"EI"),
	    'valeur' 		: fields.float(u"Valeur",track_visibility='always'),
	    'taxe' 		    : fields.char(u"Droits et traxes"),
	    'no_quittance' 	: fields.char(u"No. Quittance"),
	    'consignation' 	: fields.char(u"Consignation"),
	    'contravention' : fields.char(u"Infraction"),
	    'classe' 		: fields.char(u"Classe"),
	    'classement' 	: fields.char(u"No. Classement",track_visibility='always'),
	    'devise'        : fields.many2one('res.currency','Devise'),
	    'incoterm'      : fields.many2one('stock.incoterms',u'CFR/FOB'),
	    'date_quittance': fields.date(u"Date de quittance",track_visibility='always'),
	    'type'          : fields.selection(selection=[('import','Import'),('export','Export')],string=u'Type de répertoire',required=True)
	
	}
	
    def create(self, cr, uid, vals, context=None):
        if vals.get('name','/')=='/':
            vals['name'] = self.pool.get('ir.sequence').get(cr, 1, 'repertoire_%s' % vals['type']) or '/'
        order =  super(repertoire, self).create(cr, uid, vals, context=context)
        return order
