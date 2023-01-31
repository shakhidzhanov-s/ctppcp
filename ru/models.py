from django.db import models
from django.core.exceptions import ValidationError


class MainImage(models.Model):
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.caption


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    caption = models.CharField(max_length=200)
    def __str__(self):
        return self.caption


class Document(models.Model):
    document = models.FileField(upload_to="documents")
    title = models.CharField(max_length=200)
    date = models.DateField('date published')
    def __str__(self):
        return self.title + ', ' + str(self.date)


class Institute(models.Model):
    name = models.TextField(max_length=200)
    nameLittle = models.TextField(max_length=20)
    link1Title = models.CharField(max_length=50, blank=True)
    link1Link = models.URLField(blank=True)
    link2Title = models.CharField(max_length=50, blank=True)
    link2Link = models.URLField(blank=True)
    link3Title = models.CharField(max_length=50, blank=True)
    link3Link = models.URLField(blank=True)
    link4Title = models.CharField(max_length=50, blank=True)
    link4Link = models.URLField(blank=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if Institute.objects.exists() and not self.pk:
            raise ValidationError('You cannot add a new Institute, please change previous Institute entry')
        return super(Institute, self).save(*args, **kwargs)


class Event(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField('event text')
    date = models.DateField('date published')
    photo = models.ImageField(upload_to='images', blank=True, null=True)
    def __str__(self):
        return self.title


class Position(models.Model):
    date = models.DateField('date published')
    title = models.CharField(max_length=200)
    text = models.TextField('position description')
    def __str__(self):
        return self.title


class History(models.Model):
    text = models.TextField('history')
    def __str__(self):
        return self.text
    def save(self, *args, **kwargs):
        if History.objects.exists() and not self.pk:
            raise ValidationError('You cannot add a new History, please change previous History entry')
        return super(History, self).save(*args, **kwargs)


class Mission(models.Model):
    text = models.TextField('mission')
    def __str__(self):
        return self.text
    def save(self, *args, **kwargs):
        if Mission.objects.exists() and not self.pk:
            raise ValidationError('You cannot add a new Mission, please change previous Mission entry')
        return super(Mission, self).save(*args, **kwargs)


class Fazly(models.Model):
    text = models.TextField('about Fazly')
    def __str__(self):
        return self.text
    def save(self, *args, **kwargs):
        if Fazly.objects.exists() and not self.pk:
            raise ValidationError('You cannot add a new Fazly, please change previous Fazly entry')
        return super(Fazly, self).save(*args, **kwargs)


class Contact(models.Model):
    title = models.TextField('Title')
    address = models.TextField('Text')
    script = models.TextField('Script')
    def __str__(self):
        return self.address
    def save(self, *args, **kwargs):
        if Contact.objects.exists() and not self.pk:
            raise ValidationError('You cannot add a new Contact, please change previous Contact entry')
        return super(Contact, self).save(*args, **kwargs)


class Report(models.Model):
    document = models.FileField(upload_to="documents")
    title = models.CharField(max_length=300)
    date = models.DateField('date published')
    def __str__(self):
        return self.title + ', ' + str(self.date)


class MainDocs(models.Model):
    document = models.FileField(upload_to="documents")
    title = models.CharField(max_length=300)
    date = models.DateField('date published')
    def __str__(self):
        return self.title + ', ' + str(self.date)


class Attestation(models.Model):
    document = models.FileField(upload_to="documents")
    title = models.CharField(max_length=300)
    date = models.DateField('date published')
    def __str__(self):
        return self.title + ', ' + str(self.date)


class Laboratory(models.Model):
    name = models.CharField(max_length=80)
    prInvestigator = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    photo = models.ImageField(upload_to='images')
    def __str__(self):
        return self.name


class Staff(models.Model):
    firstname = models.CharField(max_length=35)
    lastname = models.CharField(max_length=35)
    rang = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=50)
    photo = models.ImageField(upload_to='images')
    position = models.CharField(max_length=35)
    def __str__(self):
        return self.firstname + ' ' + self.lastname


class Etics(models.Model):
    text = models.TextField('etics')
    def __str__(self):
        return self.text
    def save(self, *args, **kwargs):
        if Etics.objects.exists() and not self.pk:
            raise ValidationError('You cannot add a new Etics, please change previous Etics entry')
        return super(Etics, self).save(*args, **kwargs)


class Senate(models.Model):
    text = models.TextField('senate')
    def __str__(self):
        return self.text
    def save(self, *args, **kwargs):
        if Senate.objects.exists() and not self.pk:
            raise ValidationError('You cannot add a new Senate, please change previous Senate entry')
        return super(Senate, self).save(*args, **kwargs)


class PrInvestigator(models.Model):
    position = models.CharField('rang',max_length=35)
    firstname = models.CharField(max_length=35)
    lastname = models.CharField(max_length=35)
    nick = models.CharField(max_length=35, unique=True)
    email = models.EmailField(max_length=50)
    labpage = models.URLField(max_length=50, blank=True)
    scholar = models.URLField(max_length=50, blank=True)
    pubmed = models.URLField(max_length=50, blank=True)
    photo = models.ImageField(upload_to='images')
    profile = models.TextField('Pr Investigator profile')
    labPhoto = models.ImageField(upload_to='images', blank=True, null=True)
    def __str__(self):
        return self.firstname + ' ' + self.lastname


class Scientist(models.Model):
    position = models.CharField(max_length=35, blank=True)
    firstname = models.CharField(max_length=35)
    lastname = models.CharField(max_length=35)
    email = models.EmailField(max_length=50, blank=True)
    prInvestigator = models.ForeignKey(PrInvestigator, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.firstname + ' ' + self.lastname


class Research(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField('about research')
    prInvestigator = models.OneToOneField(PrInvestigator, on_delete=models.CASCADE, related_name='research')
    def __str__(self):
        return self.title


class Publication(models.Model):
    title = models.CharField(max_length=350)
    authors = models.CharField(max_length=500)
    journal = models.CharField(max_length=100)
    volume = models.CharField(max_length=15)
    pages = models.CharField(max_length=20)
    date = models.DateField('date published')
    pubmed = models.CharField(max_length=15, blank=True)
    prInvestigator = models.ManyToManyField(PrInvestigator, blank=True)
    def __str__(self):
        return self.title + '; ' + str(self.authors) + '; ' + str(self.journal) + '; ' + str(self.volume) + '; ' + str(self.pages) + '; ' + str(self.date)


class Course(models.Model):
    title = models.CharField(max_length=100)
    semester = models.CharField(max_length=6)
    date = models.DateField("Date")
    url = models.URLField(max_length=100)
    lecturer = models.TextField(max_length=2000)
    place = models.CharField(max_length=7)
    def __str__(self):
        return self.title + ', ' + self.lecturer + ', ' + self.place + ', ' + self.semester


class PhDProgram(models.Model):
    about = models.TextField('about program')
    def __str__(self):
        return self.about[:20] + '...'
    def save(self, *args, **kwargs):
        if PhDProgram.objects.exists() and not self.pk:
            raise ValidationError('You cannot add a new PhDProgram, please change previous PhDProgram entry')
        return super(PhDProgram, self).save(*args, **kwargs)


class Page(models.Model):
    pagename = models.CharField(max_length=40, unique=True)
    pagetext = models.TextField('Text')
    def __str__(self):
        return self.pagename
