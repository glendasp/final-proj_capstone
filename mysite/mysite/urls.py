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
    url(r'^question/(?P<id>\d+)/$', 'questionsapp.views.quiz', name='question_quiz'),
    url(r'^question/$', 'questionsapp.views.home', name='question_home'),
    # Commenting this since I couldn't get it to work on time
    # url(r'^profile/edit/$', 'profiles.views.profile_edit', name='profile_edit'),
    # url(r'^profile/(?P<username>[\w.@+-]+)/$', 'profiles.views.profile_view', name='profile'),
    #
    # url(r'^profile/$', 'profiles.views.profile_user', name='profile_user'),
]
# Taking the URLs, appending and serving

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
