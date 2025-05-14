
#!/usr/bin/env bash
# exit on error
Set -o errexit
pip manage.py collectstatic --no-input
python manage.py migrate 