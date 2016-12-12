from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    # Examples:
    url(r'^$', 'myapp.views.home', name='home'),
    url(r'^contact/$', 'myapp.views.contact', name='contact'),
    url(r'^about/$', 'mysite.views.about', name='about'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # sets up URL patterns for the views in django-registration-redux,
    url(r'^accounts/', include('registration.backends.default.urls')),
    # Sets up url for questions
    url(r'^question/$', 'questions.views.home', name='question_home'),
]
# Taking the URLs, appending and serving

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
