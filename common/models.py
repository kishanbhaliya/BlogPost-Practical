from django.db import models

class ModelMixin(models.Model):
    '''
        Model mixin with created_at, updated_at, created_by, updated_by 
    '''
    # user
    created_by = models.UUIDField(null=True, blank=True, 
        help_text="User uuid who create records.")
    updated_by = models.UUIDField(null=True, blank=True, 
        help_text="User uuid who updated record.")
    # datetime
    created_at = models.DateTimeField(auto_now_add=True, blank=True, 
        null=True, help_text="Date and time when records created")
    updated_at = models.DateTimeField(auto_now=True, blank=True, 
        null=True, help_text="Date and time when records updated.")

    class Meta:
        abstract = True


class TimeStampMixin(models.Model):
    '''
        Timestamp mixin where created_at and update_at define.
    '''
    # datetime
    created_at = models.DateTimeField(auto_now_add=True, blank=True, 
        null=True, help_text="Date and time when records created")
    updated_at = models.DateTimeField(auto_now=True, blank=True, 
        null=True, help_text="Date and time when records updated.")

    class Meta:
        abstract = True