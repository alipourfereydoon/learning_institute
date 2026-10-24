#!/usr/bin/env python
import os, sys
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hooshnoo_core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Django نصب نیست. requirements.txt را نصب کنید.") from exc
    execute_from_command_line(sys.argv)
if __name__ == '__main__':
    main()
