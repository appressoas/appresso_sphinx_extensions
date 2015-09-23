##################################
Extension for referencing settings
##################################


*****************
Add the extension
*****************

Add ``appresso_sphinx_extensions.settings`` to the ``extensions`` configuration
in ``conf.py`` in your Sphinx documentation.


*****************
Use the extension
*****************

To document a setting, use::

    .. settings:: MY_SETTING

        This is the docs for the setting.


To reference a setting, use::

    :setting:`MY_SETTING`
