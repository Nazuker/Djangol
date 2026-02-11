from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Roles(models.Model):
    id_role = models.AutoField(primary_key=True)
    role_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'roles'
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Goods(models.Model):
    id_good = models.AutoField(primary_key=True)
    good_name = models.TextField()
    good_description = models.TextField(blank=True, null=True)
    good_price = models.TextField()  # This field type is a guess.
    good_picture_link = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods'
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Users(models.Model):
    id_user = models.AutoField(primary_key=True)
    second_name = models.TextField()
    name = models.TextField()
    third_name = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    role = models.ForeignKey('Roles', models.DO_NOTHING)
    user_auth_name = models.TextField()
    user_auth_password = models.IntegerField()
    address_oblast = models.TextField(blank=True, null=True)
    address_town = models.TextField(blank=True, null=True)
    address_street = models.TextField(blank=True, null=True)
    address_home_number = models.TextField(blank=True, null=True)
    address_flat_number = models.IntegerField(blank=True, null=True)
    email = models.TextField()
    phone_number = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Users'
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PayList(models.Model):
    list_id = models.AutoField(primary_key=True)
    cart = models.ForeignKey('ShopCart', models.DO_NOTHING)
    total_amount = models.IntegerField()
    total_price = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'pay_list'
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ShopCart(models.Model):
    id_cart = models.AutoField(primary_key=True)
    goods = models.ForeignKey('Goods', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'shop_cart'
