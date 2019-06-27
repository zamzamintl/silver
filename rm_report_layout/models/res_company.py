



from odoo import fields, models,api,_
from odoo.tools import consteq, float_round, image_resize_images, image_resize_image, ustr
from odoo.tools import config, human_size, ustr, html_escape
from PIL import Image
import base64
import codecs
import io
from odoo.exceptions import ValidationError



class ResCompany(models.Model):
    _inherit = 'res.company'



    header_image=fields.Binary('Company Header Image',attachment=True)
    footer_image = fields.Binary('Company Footer Image', attachment=True)
    # external_report_layout = fields.Selection(selection_add=[
    #     ('company', 'Use Header and Footer'),
    # ])

    # @api.constrains('header_image')
    # def check_image_size(self):
    #     print('iam in  check image size')
    #     if not self.header_image:
    #         return False
    #     base64_image=self.header_image
    #
    #     image_stream = io.BytesIO(codecs.decode(base64_image, 'base64'))
    #     image = Image.open(image_stream)
    #     print('image size is',image.size)
    #
    #     width, height = image.size
    #
    #     if int(width) > 1024 or int(height) > 480 :
    #         raise ValidationError(_('Uploaded Header Image Exceeded 1024x480'))
    #     print (image.format)
    #
    #     if image.format not in ['PNG','JPG','JPEG']:
    #         raise ValidationError(_('Uploaded Header Image must be .png or .jpg image format'))




    # @api.constrains('footer_image')
    # def check_image_size(self):
    #     print('iam in  check image size')
    #     if not self.footer_image:
    #         return False
    #     base64_image=self.header_image
    #
    #     image_stream = io.BytesIO(codecs.decode(base64_image, 'base64'))
    #     image = Image.open(image_stream)
    #     print('image size is',image.size)
    #
    #     width, height = image.size
    #
    #     if int(width) > 1024 or int(height) > 480 :
    #         raise ValidationError(_('Uploaded Footer Image Exceeded 1024x480'))
    #     print (image.format)
    #
    #     if image.format not in ['PNG','JPG','JPEG']:
    #         raise ValidationError(_('Uploaded Footer Image must be .png or .jpg image format'))
    #






