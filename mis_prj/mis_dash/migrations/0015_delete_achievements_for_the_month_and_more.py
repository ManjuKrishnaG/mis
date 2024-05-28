# Generated by Django 4.2.7 on 2024-04-30 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mis_dash', '0014_first_aid_cases_lti_manpower_mti_nearmiss_rwc_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Achievements_For_the_Month',
        ),
        migrations.DeleteModel(
            name='EmployeeData',
        ),
        migrations.DeleteModel(
            name='First_Aid_cases',
        ),
        migrations.DeleteModel(
            name='Incidents',
        ),
        migrations.DeleteModel(
            name='LTI',
        ),
        migrations.DeleteModel(
            name='Manhours',
        ),
        migrations.DeleteModel(
            name='manpower',
        ),
        migrations.DeleteModel(
            name='MTI',
        ),
        migrations.DeleteModel(
            name='Nearmiss',
        ),
        migrations.DeleteModel(
            name='Noof_EventMP_approved_and_issued',
        ),
        migrations.DeleteModel(
            name='Noof_MOCs_approved_and_issued',
        ),
        migrations.DeleteModel(
            name='Noof_observations_Action_taken_ytd',
        ),
        migrations.DeleteModel(
            name='Noof_observations_for_the_month_by_walk_throughexternal_audit',
        ),
        migrations.DeleteModel(
            name='Noof_observations_for_themonth',
        ),
        migrations.DeleteModel(
            name='Noof_observations_pending_ytd',
        ),
        migrations.DeleteModel(
            name='Noof_Road_Realated_Incidents',
        ),
        migrations.DeleteModel(
            name='Noof_Safety_Inspections_Carriedoutin_Plants_Retail',
        ),
        migrations.DeleteModel(
            name='Noofsafetyalertcard',
        ),
        migrations.DeleteModel(
            name='Noofsafetyalertcardreceived',
        ),
        migrations.DeleteModel(
            name='NumberofTrainingSessions',
        ),
        migrations.DeleteModel(
            name='Plan_for_the_Next_Month',
        ),
        migrations.DeleteModel(
            name='RWC',
        ),
        migrations.DeleteModel(
            name='Total_Noof_observations_ytd',
        ),
        migrations.DeleteModel(
            name='work_permit_issued',
        ),
        migrations.RemoveField(
            model_name='peopletrained',
            name='title',
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='Achievements_Forthe_Month',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='Cumulative_yt',
            field=models.CharField(blank=True, default=0, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='Major',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='Minor',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='No_of_EventMP_approved_and_issued',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='No_of_MOCs_approved_and_issued',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='No_of_observations_Action_taken_ytd',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='No_of_observations_pending_ytd',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='NoofRoadRealatedIncidents',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='NoofSafetyInspectionsCarriedoutinPlantsRetail',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='Noof_observations_for_the_month',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='Noof_observations_for_the_month_by_walk_through_external_audit',
            field=models.ImageField(blank=True, default=0, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='NumberofTrainingsessions',
            field=models.CharField(blank=True, default=0, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='Plan_forthe_Next_Month',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='Total_No_of_observations_ytd',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='action_taken_ytd',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='offroll_fa',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='offroll_lti',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='offroll_mp',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='offroll_mti',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='offroll_nm',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='offroll_rwc',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='offroll_sacr',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='onroll_fa',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='onroll_lti',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='onroll_mp',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='onroll_mti',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='onroll_nm',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='onroll_rwc',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='onroll_sacr',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='pending_ytd',
            field=models.CharField(blank=True, default=0, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='permanentfemale_mh',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='permanentmale_mh',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='tempfemale_mh',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='tempmale_mh',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='peopletrained',
            name='work_permit_issue',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]