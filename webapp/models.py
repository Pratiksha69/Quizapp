from django.db import models

# Organizer DAta
class OrganizerData(models.Model):
	Org_ID=models.CharField(max_length=20, primary_key=True)
	Org_Name=models.CharField(max_length=100)
	Org_Ins=models.CharField(max_length=200, default='None')

	Org_Email=models.CharField(max_length=80,blank=True)

	Org_Email=models.CharField(max_length=80, blank=True)

	Org_Password=models.CharField(max_length=20)
	Status=models.CharField(max_length=10, default='Deactive')
	class Meta:
		db_table="OrganizerData"