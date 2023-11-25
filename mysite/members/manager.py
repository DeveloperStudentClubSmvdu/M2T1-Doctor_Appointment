from django.contrib.auth.base_user import BaseUserManager

class UserManager (BaseUserManager):
    use_in_migrations=True


    def create_user(self, email, password , **extra_fieilds):

        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fieilds)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password , **extra_fieilds):
        extra_fieilds.setdefault('is_staff',True)
        extra_fieilds.setdefault('is_superuser',True)
        extra_fieilds.setdefault('is_active',True)

        if extra_fieilds.get('is_staff') is not True:
            raise ValueError(('is_staff not true'))
        
        return self.create_user(email,password, **extra_fieilds)