# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
from openerp import api
from openerp.exceptions import except_orm, Warning, RedirectWarning

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
	    'p_brut' 		: fields.float(u"P.Brut",track_visibility='always',digits=['',3]),
	    'p_net' 		: fields.float(u"P.Net" ,track_visibility='always',digits=['',3]),
	    'taux' 		    : fields.float(u"Cours de change",track_visibility='always',digits=['',3]),
	    'montant' 		: fields.float(u"Montant",track_visibility='always',digits=['',3]),
	    'ei' 		    : fields.char(u"EI"),
	    'valeur' 		: fields.float(u"Valeur",track_visibility='always',digits=['',3]),
	    'taxe' 		    : fields.char(u"Droits et traxes"),
	    'taxe_quittance': fields.char(u"No. Quittance"),
	    'taxe_date'     : fields.date(u"Date"),
	    
	    'consignation' 	: fields.char(u"Consignation"),
	    'cons_quittance': fields.char(u"No. Quittance"),
	    'no_quittance' 	: fields.char(u"No. Quittance"),
	    'cons_date'     : fields.date(u"Date"),
	    
	    
	    'contravention' : fields.char(u"Infraction"),
	    'inf_quittance' : fields.char(u"No. Quittance"),
	    'inf_date'      : fields.date(u"Date"),
	    
	    'classe' 		: fields.char(u"Classe"),
	    'classement' 	: fields.char(u"No. Classement",track_visibility='always'),
	    'devise'        : fields.many2one('res.currency','Devise'),
	    'incoterm'      : fields.many2one('stock.incoterms',u'CFR/FOB'),
	    'date_quittance': fields.date(u"Date de quittance",track_visibility='always'),
	    'type'          : fields.selection(selection=[('import','Import'),('export','Export')],string=u'Type de répertoire',required=True),
	    'ventilation'   : fields.one2many('transit.ventilation','repertoire','Ventilations'),
	}
	
    def create(self, cr, uid, vals, context=None):
        if vals.get('name','/')=='/':
            vals['name'] = self.pool.get('ir.sequence').get(cr, 1, 'repertoire_%s' % vals['type']) or '/'
        order =  super(repertoire, self).create(cr, uid, vals, context=context)
        return order

class transit_ventilation(osv.osv):
    _name="transit.ventilation"	
    
    def _calc(self,cr,uid,ids,name,arg,context=None):
        res= {}
        for o in self.browse(cr,uid,ids):
            res[o.id] = {'coefficient'          :False,
                         'valeur'               :False,
                         'valeur_declaree'      :False,
                         'poids_net_declaree'   :False,
                        }
            valeur      = o.cours_change * o.cfr + o.reliquat + o.fret
            
            coefficient = valeur and valeur /o.cfr   or 0.0
            valeur_declaree = sum([x.valeur_dh for x in o.line])
            poids_net_declaree = sum([x.poids_net for x in o.line])
            
            res[o.id]['coefficient']        = coefficient
            res[o.id]['valeur']             = valeur
            res[o.id]['valeur_declaree']    = valeur_declaree
            res[o.id]['poids_net_declaree'] = poids_net_declaree
        return res
        
    _columns = {
    
        'repertoire'        :fields.many2one('repertoire',string=u"RÈPERTOIRE"),
        'dum'               :fields.related('repertoire','dum',type="char",string=u"DUM"),
        'date'              :fields.related('repertoire','date',type="date",string=u"DATE"),
        'expediteur'        :fields.related('repertoire','fournisseur',type="many2one",relation="res.partner",string=u"EXPEDITEUR"),
        'importateur'       :fields.related('repertoire','client',type="many2one",relation="res.partner",string=u"IMPORTATEUR"),
        'nb_colis'          :fields.float(string=u"NOMBRE DE COLIS",digits=['',3]),
        'poids_brute'       :fields.related('repertoire','p_brut',string=u"POIDS BRUT TOTAL",digits=['',3]),
        'poids_net'         :fields.related('repertoire','p_net',string=u"POIDS NET TOTAL",digits=['',3]),
        'bl'                :fields.char(string=u"B∕L"),
        'manifeste'         :fields.char(string=u"MANIFESTE"),
        'camion'            :fields.char(string=u"CAMION / REMORQUE"),
        'cfr'               :fields.related('repertoire','montant',string=u"CFR",digits=['',3]),
        'fret'              :fields.float(string=u"FRET / Reliquat",digits=['',3]),
        'reliquat'          :fields.float(string=u"Assurance",digits=['',3]), 
        'cours_change'      :fields.related('repertoire','taux',string=u"COURS DE CHANGE",digits=['',3]),
        'coefficient'       :fields.function(_calc,multi="all", store=True,string=u"COEFFICIENT ",digits=['',3]),
        'valeur'            :fields.function(_calc,multi="all", store=True,string=u"VALEUR",digits=['',3]),
        'valeur_declaree'   :fields.function(_calc,multi="all", store=True,string=u"VALEUR TOTALE DECLAREE",digits=['',3]),
        'poids_net_declaree':fields.function(_calc,multi="all", store=True,string=u"POIDS NET TOTALE",digits=['',3]),
        
        'line'              :fields.one2many('transit.ventilation.line','parent','Lignes'),
        'type'              :fields.selection(selection=[('import','Import'),('export','Export')],string=u'Type de répertoire',required=True),
        }
    
    @api.onchange('cours_change','cfr','reliquat','line')
    def _onchange_ventilation(self):
        self.valeur      = self.cours_change * self.cfr +  self.reliquat+ self.fret
        self.coefficient = self.valeur and self.valeur / self.cfr   or 0.0
        self.valeur_declaree = sum([x.valeur_dh for x in self.line])
    
    @api.onchange('repertoire')
    def _onchange_repertoire(self):
        #repertoire = self.env['repertoire'].browse(self.repertoire)
        if self.repertoire:
            self.dum        = self.repertoire.dum
            self.date       = self.repertoire.date
            self.expediteur = self.repertoire.fournisseur
            self.importateur= self.repertoire.client


    def write(self,cr,uid,ids,vals,context=None):
        
        return super(transit_ventilation,self).write(cr,uid,ids,vals,context)
        o = self.browse(cr,uid,ids)
        """ if o.valeur != o.valeur_declaree:
            raise Warning(u"La valeur déclarée n'est pas correcte !")
        if o.poids_net_declaree != o.poids_net:
            raise Warning(u"Le poids net n'est pas correct !")
        return True """

class transit_ventilation_line(osv.osv):
    _name="transit.ventilation.line"	
    
    def _calc(self,cr,uid,ids,name,arg,context=None):
        res= {}
        pu = 0.0
        vu = 0.0
        for o in self.browse(cr,uid,ids):
            res[o.id] = {'pu'       :False,
                         'vu'       :False,
                         'valeur_dh':False,
                        }
            valeur_dh = o.cours_change * o.val_euro
            if o.qte:
                pu  = o.poids_net / o.qte 
                
                vu = valeur_dh / o.qte
            
            res[o.id]['pu'] = pu
            res[o.id]['vu'] = vu
            res[o.id]['valeur_dh'] = valeur_dh
            
        return res
        
    _columns = {
        'parent'        :fields.many2one('transit.ventilation','Parent'),
        'repertoire'    :fields.related('parent','repertoire',string='Repertoire'),
        'pedido'        :fields.char(string=u"PEDIDO"),
        'of'            :fields.char(string=u"O∕F"),
        'qtite'         :fields.float(string=u"QTITE",digits=['',3]),
        'designation'   :fields.char(string=u"DESIGNATION"),
        'ngp'           :fields.char(string=u"NGP"),
        'pos'           :fields.char(string=u"POS"),
        'org'           :fields.char(string=u"ORG"),
        'qte'           :fields.float(string=u"QTÉ", default=1,digits=['',3]),
        'u'             :fields.char(string=u"U"),
        'pu'            :fields.function(_calc,multi="all", store=True,string=u"PU",digits=['',3]),
        'vu'            :fields.function(_calc,multi="all", store=True,string=u"VU",digits=['',3]),
        'poids_net'     :fields.float(string=u"POIDS NET",digits=['',3]),
        'val_euro'      :fields.float(string=u"VAL-EURO",digits=['',3]),
        'cours_change'  :fields.related('parent','coefficient',type="float",string=u"COURS",digits=['',3]),
        'valeur_dh'     :fields.function(_calc,multi="all", store=True,string=u"VALEUR-DH",digits=['',3]),
        }    
        
    @api.onchange('poids_net','qte','cours_change','val_euro')
    def _onchange_ventilation(self):
        
        
        self.valeur_dh  = self.cours_change * self.val_euro
        if self.qte:
            self.pu         = self.poids_net / self.qte 
            self.vu         = self.valeur_dh / self.qte        
         
    
            
