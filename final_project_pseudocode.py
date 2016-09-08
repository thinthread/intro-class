'''
Create user input post web page,
    
    keep functions clean and seperate
   
    python to handle def main() base functions
        will pull code from:
            boostrap
            django
            html
            possibly CSS if there is time
        
        will need for pthon:
            under src folder:
                under posts folder:
                    python_migrations folder:
                        __init__.py
                        admin.py
                        apps.py
                        forms.py
                        models.py
                        tests.py
                        urls.py
                        views.py
            
    djando to collect & output py,html & boostrap code to web/ and address, handle urls 
        will need for django:
            under src folder:
                django folder:
                    __init__.py
                    setting.py
                        pseudocode:
                            import os
                            
                            BASE_DIR = os.path.dirname(os.pathdirname(os.path.abspath(__file__)))
                            
                            
                            #SECURITY WARNING : Don't keep secret key in production
                            SECRET_KEY = 
                            
                            # SECUTRITY WARNING: Don't run with debug turned on in production!!!
                            DEBUG = Trus
                            
                            ALLOWED_HOSTS = []
                            installed_APPS = [
                                'django.contrib.admin',
                                'django.contrib.auth',
                                'django.contrib.contenttypes',
                                'django.contrib.sessions',
                                'django.contrib.messages',
                                'django.contrib.statistcfiles',
                                ]
                                
                                
                                
                                
                                #internationalization
                                #https://docs.djangoprojects.com/en/1.9/topics/118n/
                    urls.py
                        pseudocode:
                            from django.conf import ettings
                            from django.comf.urls import include, url
                            from django.conf.urls.static import static
                            from django.contrib import admin
                            
                            urlpatters = [
                                url(r'^admin/'), admin.site.urls),
                                url(r'^POSTS/'), include("post.urls",namespace='post')),
                            ]
                            
                            if setting.DEBUG:
                                urlpatterns += static(settings.STATIV_URL, document_root=setting.STATIC_ROOT)
                    wsgi.py
                    manage.py
                    crud.md
                    db.sqlite3
                    .gitmore
                    .Python
                    LICEnse
                    pip-selfcheck.json
                    README.md
                 
    html to set formatting
        will need for html, static stuff:
            under src folder:
                under templates folder:
                    base.html
                    messages_display.html
                    post_detail.html
                    post_form.html
                    post_list.html
            
    boostrap use to assist asthetic static components

,,,
    