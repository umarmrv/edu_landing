from django.db import models

# Create your models here.

class SiteSettings(models.Model):
    site_name = models.CharField("Название сайта", max_length=100)
    logo = models.ImageField("Логотип", upload_to="logos/", blank=True, null=True)
    phone = models.CharField("Телефон", max_length=50, blank=True)
    email = models.EmailField("Email", blank=True)
    address = models.CharField("Адрес", max_length=200, blank=True)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SiteSettings, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"
    
    def __str__(self):
        return "Настройки сайта"



class HomePageContent(models.Model):
    main_title = models.CharField("Главный заголовок", max_length=200)
    subtitle = models.CharField("Подзаголовок", max_length=300, blank=True)
    description = models.TextField("Описание", blank=True)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(HomePageContent, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        pass

    class Meta:
        verbose_name = "Контент главной страницы"
        verbose_name_plural = "Контент главной страницы"
    
    def __str__(self):
        return "Главная страница"
    


class AboutPageContent(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    content = models.TextField('Текст страницы "О нас"')

    def save(self, *args, **kwargs):
        self.pk = 1
        super(AboutPageContent, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        pass

    class Meta:
        verbose_name = "Контент станицы 'О нас'"
        verbose_name_plural = "Контент станицы 'О нас'"

    def __str__(self):
        return "Страница 'О нас'"