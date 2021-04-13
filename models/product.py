# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from datetime import timedelta, time
from odoo import api, fields, models
from odoo.tools.float_utils import float_round


class Product(models.Model):
    _inherit = 'product.product'

    brand_id = fields.Many2one('product.brand', 'Product Brand', change_default=True, default=0, required=True)

    # def _get_combination_info_variant(self, add_qty=1, pricelist=False, parent_combination=False):
    #     """Return the variant info based on its combination.
    #     See `_get_combination_info` for more information.
    #     """
    #     self.ensure_one()
    #     return self.product_tmpl_id._get_combination_info(self.product_template_attribute_value_ids, self.id, add_qty, pricelist, parent_combination)

class ProductBrand(models.Model):
    _name = 'product.brand'
    _description = 'Product Brands'
    _order = 'name,id'

    name = fields.Char(string='Brand', required=True, translate=True)
