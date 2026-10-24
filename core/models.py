from django.db import models
class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100, default='آموزشگاه هوش نو')
    tagline = models.CharField(max_length=200, default='آینده را با خلاقیت بساز!')
    phone = models.CharField(max_length=30, default='۰۲۱-۱۲۳۴۵۶۷۸')
    email = models.EmailField(default='hello@hooshno.academy')
    address = models.CharField(max_length=250, default='تهران، خیابان خلاقیت، پلاک ۱۲')
    about_text = models.TextField(default='فضایی برای یادگیری، تجربه و ساختن آینده با فناوری.')
    class Meta: verbose_name='تنظیمات سایت'; verbose_name_plural='تنظیمات سایت'
    def __str__(self): return self.site_name
    def save(self,*args,**kwargs):
        self.pk=1
        super().save(*args,**kwargs)
