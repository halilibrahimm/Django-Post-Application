from django.db import models
from django.urls import reverse
from django.utils.text import slugify #küçük harfe çevirecek
from ckeditor.fields import RichTextField




# Create your models here.
class Post(models.Model):
    user=models.ForeignKey('auth.User',verbose_name='Yazar')#yazar post ilişkisi
    title=models.CharField(max_length=120, verbose_name='Başlık')
    content=RichTextField(verbose_name='İçerik')
    publishingDate=models.DateTimeField(verbose_name='Yayınlanma Tarihi',auto_now_add=True)
    image=models.ImageField(null=True, blank=True)
    slug=models.SlugField(unique=True, editable=False,max_length=130)#bu alana url kısmında rakam yerine başlık bilgisi gelecek ,editable=false demek o alanı gizle demek otomatik değer atanır
    from ckeditor.fields import RichTextField #ckeditor için


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ('post:detail',kwargs={'slug':self.slug})

    def get_create_url(self):
        return reverse ('post:create')

    def get_update_url(self):
        return reverse ('post:update',kwargs={'slug':self.slug})


    def get_delete_url(self):
        return reverse ('post:delete',kwargs={'slug':self.slug})


    def get_unique_slug(self):#aynı slugları(urlde gözükecek başlıklar) önlemek için fonksiyon
        slug=slugify(self.title.replace('ı','i'))
        unique_slug=slug#orijinal slug ı başka değişkende tuttuk
        counter=1
        while Post.objects.filter(slug=unique_slug).exists():#veritabanına bakıldı eşleşme var mı diye
            unique_slug='{}-{}'.format(slug,counter)#varsa slugın sonuna rakam eklenerek ayırt edildi
            counter+=1
        return unique_slug

    def save(self,*args,**kwargs):# slug içindeki türkçe karakterleri değiştirme işlemi
        self.slug=self.get_unique_slug()
        return super(Post,self).save(*args,**kwargs)#orijinal metottaki save metodu çalıştırıldı

    class Meta:
        ordering=['-publishingDate','id']

class Comment(models.Model): #yorum için model oluşturuluyor

    post=models.ForeignKey('post.Post',related_name='comments',on_delete=models.CASCADE)#sonuncu parametre post silinince yorumları da silmek için

    name=models.CharField(max_length=120,verbose_name='İsim')
    content=models.TextField(verbose_name='Yorum')

    created_date=models.DateTimeField(auto_now_add=True)

