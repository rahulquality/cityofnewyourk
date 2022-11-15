# Generated by Django 4.1.3 on 2022-11-15 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cityofnewyourk', '0003_building_attorney_group_old_building_protest_old'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='aptno',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='building',
            name='attorney_group1',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='building',
            name='condo_number',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='building',
            name='condo_sfx1',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='building',
            name='condo_sfx2',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='building',
            name='corner',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='building',
            name='protest_1',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='appt_block',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='appt_boro',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='appt_date',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='appt_lot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='attorney_group_old',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='bld_dep',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='bld_ext',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='bld_frt',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='bld_story',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='bldg_class',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='block',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='boro',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='cbnactextot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='cbnactland',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='cbnacttot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='cbnmktland',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='cbnmkttot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='cbntaxclass',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='cbntaxflag',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='cbntrnextot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='cbntrnland',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='cbntrntot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='cbntxbextot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='cbntxbtot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='coop_apts',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='coop_num',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='cpb_boro',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='cpb_dist',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='curactextot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='curactland',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='curacttot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='curmktland',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='curmkttot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='curtaxclass',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='curtaxflag',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='curtrnextot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='curtrnland',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='curtrntot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='curtxbextot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='curtxbtot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='factory_area_gross',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='finactextot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='finactland',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='finacttot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='finmktland',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='finmkttot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='fintaxclass',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='fintaxflag',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='fintrnextot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='fintrnland',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='fintrntot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='fintxbextot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='fintxbtot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='garage_area',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='gepsupport_rc',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='gross_sqft',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='hotel_area_gross',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='housenum_hi',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='housenum_lo',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='ident',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='land_area',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='loft_area_gross',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='lot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='lot_dep',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='lot_frt',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='lot_irreg',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='newdrop',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='noav',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='num_bldgs',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='office_area_gross',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='other_area_gross',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='period',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='protest_old',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='pyactextot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='pyactland',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='pyacttot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='pymktland',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='pymkttot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='pytaxclass',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='pytaxflag',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='pytrnextot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='pytrnland',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='pytrntot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='pytxbextot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='pytxbtot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='rectype',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='residential_area_gross',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='retail_area_gross',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='reuc_description',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='roll_section',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='secvol',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='storage_area_gross',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='street_name',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='subident',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='subident_reuc',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='tenactextot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='tenactland',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='tenacttot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='tenmktland',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='tenmkttot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='tentaxclass',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='tentaxflag',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='tentrnextot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='tentrnland',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='tentrntot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='tentxbextot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='tentxbtot',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='uaf_bldg',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='uaf_land',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='units',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='warehouse_area_gross',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='year',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='yralt1',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='yralt1_range',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='yralt2',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='yralt2_range',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='yrbuilt',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='yrbuilt_range',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='zip_code',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='zoning',
            field=models.CharField(default=True, max_length=10, null=True),
        ),
    ]
