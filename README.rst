Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'blog',
    )

2. Include the myblog URLconf in your project urls.py like this::

    url(r'^blog/', include('blog.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to add a blog (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000 to see the blogs.