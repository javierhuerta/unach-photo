=====
Usage
=====

To use unach_photo in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'unach_photo.apps.UnachPhotoConfig',
        ...
    )

Add unach_photo's URL patterns:

.. code-block:: python

    from unach_photo import urls as unach_photo_urls


    urlpatterns = [
        ...
        url(r'^', include(unach_photo_urls)),
        ...
    ]
