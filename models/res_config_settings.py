# -*- coding: utf-8 -*-
from odoo import models, fields, Command


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    ecommerce_discount = fields.Integer(string="E-Commerce Discount",
                                        config_parameter='ecommerce_discount.ecommerce_discount')
    enable_ecommerce_discount = fields.Boolean(string="Set E-commerce discount",
                                               config_parameter='ecommerce_discount.enable_ecommerce_discount')
    ecommerce_discount_apply = fields.Boolean(string="compute",
                                              compute="compute_ecommerce_discount_apply")

    def compute_ecommerce_discount_apply(self):
        if self.enable_ecommerce_discount:
            self.ecommerce_discount_apply = True

            discount_program = self.env.ref(
                'ecommerce_discount.e_commerce_discount_promotion')
            id = discount_program.reward_ids.id

            discount_program.update({
                'active': True,
                'reward_ids': [(Command.update(id, {
                    'discount': self.ecommerce_discount,
                }))]
            })
        else:
            self.ecommerce_discount_apply = False
            discount_program = self.env.ref(
                'ecommerce_discount.e_commerce_discount_promotion')
            discount_program.update({
                'active': False})
