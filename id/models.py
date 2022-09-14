from django.db import models
from PIL import Image
from django.core.validators import RegexValidator


class Department(models.Model):
    name = models.CharField(
        max_length=50,
    )
    parent_department = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, verbose_name=" უფროსი"
    )

    def __str__(self):
        if self.parent_department:
            return str(self.name + " / " + str(self.parent_department))
        else:
            return self.name


class PersonalTraits(models.Model):
    person = models.CharField(
        max_length=30,
    )

    def __str__(self):
        return self.person


###
class Id(models.Model):
    city = (
        ("Tbilisi", "თბილისი"),
        ("Batumi", "ბათუმი"),
        ("Kutaisi", "ქუთაისი"),
        ("Zestafoni", "ზესტაფონი"),
    )
    orientation = (
        ("Men", "კაცი"),
        ("Women", "ქალი"),
        ("Dont wanna say", "არ მინდა დასახელება"),
    )
    citizenship = (
        ("Georgia", "საქართველო"),
        ("Foreign country", "უცხო ქვეყნის მოქალაქე"),
    )

    ### Persons Information
    image = models.ImageField(
        default="",
        upload_to="images",
        help_text=("აირჩიეთ სურათი"),
        verbose_name=(" სურათი"),
    )
    first_name = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(r"^[a-zA-Z ]*$", message="გამოიყენეთ მხოლოდ ლათინური ასოები")
        ],
        help_text=("გამოიყენეთ მხოლოდ ასოები"),
        verbose_name=(" სახელი"),
    )
    last_name = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(r"^[a-zA-Z ]*$", message="გამოიყენეთ მხოლოდ ლათინური ასოები")
        ],
        help_text=("გამოიყენეთ მხოლოდ ასოები"),
        verbose_name=(" გვარი"),
    )
    location = models.CharField(
        max_length=100,
        choices=city,
        help_text=("აირჩიეთ ქალაქი"),
        verbose_name=(" ქალაქი"),
    )
    sex = models.CharField(
        choices=orientation,
        max_length=20,
        help_text=("აირჩიეთ სქესი"),
        verbose_name=(" სქესი"),
    )
    citizen = models.CharField(
        choices=citizenship,
        max_length=50,
        help_text=("ამოირჩიეთ ქალაქი"),
        verbose_name=(" მოქალაქეობა"),
    )
    card_num = models.CharField(
        max_length=20,
        validators=[RegexValidator(r"^[a-zA-Z0-9_]*$")],
        help_text=("გამოიყენეთ მხოლოდ ასოები და ციფრები"),
        verbose_name=(" ბარათის ნომერი"),
    )
    number_id = models.CharField(
        max_length=11,
        validators=[RegexValidator(r"^[0-9]*$")],
        help_text=("გამოიყენეთ მხოლოდ ციფრები"),
        verbose_name=(" პირადობის ნომერი"),
    )
    date_of_birth = models.DateField(verbose_name=(" დაბადების თარიღი"))
    validit_period = models.DateField(verbose_name=(" გაუქმების თარიღი"))

    dep = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="dep")

    # person = models.ManyToManyField(
    #     PersonalTraits, blank=True, null=True, related_name="pers"
    # )

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image)
        if img.height > 200 and img.width > 200:
            size = (100, 100)
            img.thumbnail(size)
            img.save(self.image.path)


class Arival_time(models.Model):
    name = models.CharField(
        verbose_name=" სახელი", max_length=20, blank=True, null=True
    )
    person_number = models.ForeignKey(
        Id,
        default=None,
        on_delete=models.CASCADE,
        related_name="ids",
    )
    comment = models.TextField(max_length=500, null=True, blank=True)
    check_in = models.TimeField(null=True)
    check_out = models.TimeField(null=True)

    def __str__(self):
        return self.name
