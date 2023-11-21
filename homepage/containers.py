from dependency_injector import containers, providers

from django.urls import reverse_lazy


class HomepageContainer(containers.DeclarativeContainer):
    homepage_urls = providers.Dict({'Home': reverse_lazy('home:homepage')})
    homepage_title = providers.Object("Homepage")


container = HomepageContainer()
