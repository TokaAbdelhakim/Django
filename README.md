
Django Projects
< PROJECT ROOT >
   |
   |-- core(adminLTE)/                     # Implements app logic and serve the static assets
   |    |-- settings.py                    # Django app bootstrapper
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>          # CSS files, Javascripts files
   |    |
   |    |-- templates/                      # Templates used to render pages
   |         |
   |         |-- dash.html                  # HTML for version 1 dashboard
   |         |
   |         |-- dash3.html                 # HTML for version 3 dashboard 
   |
   |-- app(dashboard)/                     # A simple app that serve HTML files
   |    |
   |    |-- views.py                       # Serve HTML pages for authenticated users
   |    |-- urls.py                        # Define some super simple routes  
   |
   |-- manage.py                           # Start the app - Django default start script
   |
   |-- ************************************************************************
