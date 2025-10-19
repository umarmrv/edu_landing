from django.db import models

# Create your models here.

class SiteSettings(models.Model):
    site_name = models.CharField("Name of the site", max_length=100)
    logo = models.ImageField("Logo", upload_to="logos/", blank=True, null=True)
    phone = models.CharField("Phone", max_length=50, blank=True)
    email = models.EmailField("Email", blank=True)
    address = models.CharField("Address", max_length=200, blank=True)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SiteSettings, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    class Meta:
        verbose_name = "Settings"
        verbose_name_plural = "Settings"
    
    def __str__(self):
        return "Settings"



class HomePageContent(models.Model):
    main_title = models.CharField("Main header", max_length=200)
    subtitle = models.CharField("Subtitle", max_length=200, blank=True)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(HomePageContent, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        pass

    class Meta:
        verbose_name = "Home page content"
        verbose_name_plural = "Home page content"
    
    def __str__(self):
        return "Home page"
    


class AboutPageContent(models.Model):
    title = models.CharField("Header", max_length=200)
    subtitle = models.CharField("Subtitle", max_length=300,)
    content = models.TextField('"About us" text')

    def save(self, *args, **kwargs):
        self.pk = 1
        super(AboutPageContent, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        pass

    class Meta:
        verbose_name = '"About us" page content'
        verbose_name_plural = '"About us" page content'

    def __str__(self):
        return '"About us" page'
    


class HomePageTexts(models.Model):
    text = models.TextField()

    class Meta:
        verbose_name = "Home page texts"
        verbose_name_plural = "Home page texts"

    def __str__(self):
        return f"Text №{self.id}"
    


class Course(models.Model):
    title = models.CharField("Course name", max_length=200)
    short_description = models.CharField("Short description", max_length=300)   
    full_description = models.TextField("Full description")
    image = models.ImageField("Course image", upload_to="courses/", blank=True, null=True)
    price = models.DecimalField("Price", max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    schedule = models.CharField(max_length=100, blank=True, null=True)    
    goal = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    level = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = "Courses"
        verbose_name_plural = "Courses"
    
    def __str__(self):
        return self.title