# Django Template

I created this template as a kickstart to more productive opinionated django projects.

I've included :

* django channels for asynchronous communication
* django-extensions
* django-rest-framework (with django-filter)
  * already plumbed in to `urls.py` at /api/ 
* pytest-describe, configured with django settings to read `*_spec.py` files
* a first application, set up as "app"
  * admin set up to automatically add all models in the app to the admin interface with a default admin
  * a home view and template that link to the API and Admin interfaces (with tests, with directory for views)
  * a models directory (add files with models, and add the models to `__init__.py`)

## Usage

```bash
$ django-admin startproject myproject -e py -e ini out/project_template.zip
```

## Build
```bash
$ make build
```