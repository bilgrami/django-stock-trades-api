# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from django.contrib.postgres.fields import JSONField
from django.core.validators import MaxValueValidator, MinValueValidator

"""
Each trade is a JSON entry with the following keys:

id: The unique ID of the trade.
type: The trade type, either buy or sell.
user: The user responsible for the trade, a JSON entry:
id: The user's unique ID.
name: The user's name.
symbol: The stock symbol.
shares: The total number of shares traded. The traded shares value is between 10 and 30 shares, inclusive.
price: The price of one share of stock at the time of the trade (up to two places of decimal). 
The stock price is between 130.42 and 195.65 inclusive.
timestamp: The timestamp for the trade creation given in the format yyyy-MM-dd HH:mm:ss. The timezone is EST (UTC -4).

{"id": 1002492, "type": "buy", "user": {"id": 4737917, "name": "Daniel"}, "stock_symbol": "ABX", "stock_quantity": 30, "stock_price": 134.26, "trade_timestamp": "2014-06-14 14:06:13"}},

"""

trade_type_choices = [
  ('buy', 'buy'),
  ('sell', 'sell'),
]


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField("name", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "user"
        db_table = 'RestAPI_user'


class Trade(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField("type", max_length=3,
                            choices=trade_type_choices)
    user = models.ForeignKey(User,
                             related_name='user_trades',
                             on_delete=models.SET_NULL,
                             null=True, blank=True)
    stock_symbol = models.CharField("stock_symbol", max_length=10)
    stock_quantity = models.SmallIntegerField("shares",
                                              validators=[MinValueValidator(10),
                                                          MaxValueValidator(30)])
                                                  
    stock_price = models.DecimalField("price", decimal_places=2,
                                      max_digits=8,
                                      validators=[MinValueValidator(130.42),
                                                  MaxValueValidator(195.65)])
    trade_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "trade"
        db_table = 'RestAPI_trade'

