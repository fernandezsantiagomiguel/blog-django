from django.db.models.signals import post_migrate
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver
from apps.Post.models import Noticia

@receiver(post_migrate)
def create_colaborador_group(sender, **kwargs):
    if sender.name == 'apps.User':
        colaborador_group, created = Group.objects.get_or_create(name='colaborador')
        noticia_content_type = ContentType.objects.get_for_model(Noticia)

        permisos = [
            Permission.objects.get(codename='add_noticia', content_type=noticia_content_type),
            Permission.objects.get(codename='change_noticia', content_type=noticia_content_type),
            Permission.objects.get(codename='delete_noticia', content_type=noticia_content_type),
            Permission.objects.get(codename='can_manage_noticias', content_type=noticia_content_type),
        ]

        colaborador_group.permissions.set(permisos)
        colaborador_group.save()
        print("Grupo 'colaborador' creado y permisos asignados.")