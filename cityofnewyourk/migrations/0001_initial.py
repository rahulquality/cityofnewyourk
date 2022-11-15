# Generated by Django 4.1.3 on 2022-11-15 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parid', models.CharField(max_length=20)),
                ('boro', models.CharField(max_length=10)),
                ('block', models.CharField(max_length=10)),
                ('lot', models.CharField(max_length=10)),
                ('subident_reuc', models.CharField(max_length=10)),
                ('rectype', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=10)),
                ('ident', models.CharField(max_length=10)),
                ('subident', models.CharField(max_length=10)),
                ('roll_section', models.CharField(max_length=10)),
                ('secvol', models.CharField(max_length=10)),
                ('pymktland', models.CharField(max_length=10)),
                ('pymkttot', models.CharField(max_length=10)),
                ('pyactland', models.CharField(max_length=10)),
                ('pyacttot', models.CharField(max_length=10)),
                ('pyactextot', models.CharField(max_length=10)),
                ('pytrnland', models.CharField(max_length=10)),
                ('pytrntot', models.CharField(max_length=10)),
                ('pytrnextot', models.CharField(max_length=10)),
                ('pytxbtot', models.CharField(max_length=10)),
                ('pytxbextot', models.CharField(max_length=10)),
                ('pytaxclass', models.CharField(max_length=10)),
                ('tenmktland', models.CharField(max_length=10)),
                ('tenmkttot', models.CharField(max_length=10)),
                ('tenactland', models.CharField(max_length=10)),
                ('tenacttot', models.CharField(max_length=10)),
                ('tenactextot', models.CharField(max_length=10)),
                ('tentrnland', models.CharField(max_length=10)),
                ('tentrntot', models.CharField(max_length=10)),
                ('tentrnextot', models.CharField(max_length=10)),
                ('tentxbtot', models.CharField(max_length=10)),
                ('tentxbextot', models.CharField(max_length=10)),
                ('tentaxclass', models.CharField(max_length=10)),
                ('cbnmktland', models.CharField(max_length=10)),
                ('cbnmkttot', models.CharField(max_length=10)),
                ('cbnactland', models.CharField(max_length=10)),
                ('cbnacttot', models.CharField(max_length=10)),
                ('cbnactextot', models.CharField(max_length=10)),
                ('cbntrnland', models.CharField(max_length=10)),
                ('cbntrntot', models.CharField(max_length=10)),
                ('cbntrnextot', models.CharField(max_length=10)),
                ('cbntxbtot', models.CharField(max_length=10)),
                ('cbntxbextot', models.CharField(max_length=10)),
                ('cbntaxclass', models.CharField(max_length=10)),
                ('finmktland', models.CharField(max_length=10)),
                ('finmkttot', models.CharField(max_length=10)),
                ('finactland', models.CharField(max_length=10)),
                ('finacttot', models.CharField(max_length=10)),
                ('finactextot', models.CharField(max_length=10)),
                ('fintrnland', models.CharField(max_length=10)),
                ('fintrntot', models.CharField(max_length=10)),
                ('fintrnextot', models.CharField(max_length=10)),
                ('fintxbtot', models.CharField(max_length=10)),
                ('fintxbextot', models.CharField(max_length=10)),
                ('fintaxclass', models.CharField(max_length=10)),
                ('curmktland', models.CharField(max_length=10)),
                ('curmkttot', models.CharField(max_length=10)),
                ('curactland', models.CharField(max_length=10)),
                ('curacttot', models.CharField(max_length=10)),
                ('curactextot', models.CharField(max_length=10)),
                ('curtrnland', models.CharField(max_length=10)),
                ('curtrntot', models.CharField(max_length=10)),
                ('curtrnextot', models.CharField(max_length=10)),
                ('curtxbtot', models.CharField(max_length=10)),
                ('curtxbextot', models.CharField(max_length=10)),
                ('curtaxclass', models.CharField(max_length=10)),
                ('period', models.CharField(max_length=10)),
                ('noav', models.CharField(max_length=10)),
                ('bldg_class', models.CharField(max_length=10)),
                ('owner', models.CharField(max_length=100)),
                ('housenum_lo', models.CharField(max_length=10)),
                ('housenum_hi', models.CharField(max_length=10)),
                ('street_name', models.CharField(max_length=250)),
                ('zip_code', models.CharField(max_length=10)),
                ('gepsupport_rc', models.CharField(max_length=10)),
                ('stcode', models.CharField(max_length=20)),
                ('lot_frt', models.CharField(max_length=10)),
                ('lot_dep', models.CharField(max_length=10)),
                ('bld_frt', models.CharField(max_length=10)),
                ('bld_dep', models.CharField(max_length=10)),
                ('bld_story', models.CharField(max_length=10)),
                ('land_area', models.CharField(max_length=10)),
                ('num_bldgs', models.CharField(max_length=10)),
                ('yrbuilt', models.CharField(max_length=10)),
                ('yrbuilt_range', models.CharField(max_length=10)),
                ('yralt1', models.CharField(max_length=10)),
                ('yralt1_range', models.CharField(max_length=10)),
                ('yralt2', models.CharField(max_length=10)),
                ('yralt2_range', models.CharField(max_length=10)),
                ('coop_apts', models.CharField(max_length=10)),
                ('units', models.CharField(max_length=10)),
                ('reuc_ref', models.CharField(max_length=20)),
                ('coop_num', models.CharField(max_length=10)),
                ('uaf_land', models.CharField(max_length=10)),
                ('uaf_bldg', models.CharField(max_length=10)),
                ('gross_sqft', models.CharField(max_length=10)),
                ('hotel_area_gross', models.CharField(max_length=10)),
                ('office_area_gross', models.CharField(max_length=10)),
                ('residential_area_gross', models.CharField(max_length=10)),
                ('retail_area_gross', models.CharField(max_length=10)),
                ('loft_area_gross', models.CharField(max_length=10)),
                ('factory_area_gross', models.CharField(max_length=10)),
                ('warehouse_area_gross', models.CharField(max_length=10)),
                ('storage_area_gross', models.CharField(max_length=10)),
                ('garage_area', models.CharField(max_length=10)),
                ('other_area_gross', models.CharField(max_length=10)),
                ('reuc_description', models.CharField(max_length=250)),
                ('extracrdt', models.DateField()),
                ('pytaxflag', models.CharField(max_length=10)),
                ('tentaxflag', models.CharField(max_length=10)),
                ('cbntaxflag', models.CharField(max_length=10)),
                ('fintaxflag', models.CharField(max_length=10)),
                ('curtaxflag', models.CharField(max_length=10)),
            ],
        ),
    ]
