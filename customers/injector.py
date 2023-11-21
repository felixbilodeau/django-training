from dependency_injector import containers, providers

from homepage.containers import container

from django.urls import reverse_lazy


class HomepageContainerOverride(containers.DeclarativeContainer):
    homepage_title = providers.Object("Muahahahaha")


def override():
    container.homepage_urls.add_kwargs(
        {'Customers': reverse_lazy('customers:index')}
    )
    container.override(HomepageContainerOverride())
