# django-blog
Blog website made using Django and Tailwind.

To run it in your local machine, first set SECRET_KEY, DEBUG and ENVIRONMENT as environment variables

  export SECRET_KEY='your_secret_key'
  export DEBUG=1
  export ENVIRONMENT='production'

Then run migrations and run it in your localhost:

  python3 manage.py migrate
  python3 manage.py runserver
