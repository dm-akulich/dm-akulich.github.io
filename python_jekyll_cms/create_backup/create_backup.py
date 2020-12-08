import tarfile
import os.path
from datetime import datetime as dt
import re

# Текущее время для названия бэкапа
current_dt = str(dt.now())
pattern = r'\.[\d]+'  # выбирает только милисекунды и удаляем их
current_dt = re.sub(pattern, '', current_dt)
current_dt = re.sub(r':', '-', current_dt)
current_dt = re.sub(r' ', '-', current_dt)


def make_tarfile(output_filename, source_dir, ):
    print('Backup from {0} is creating...'.format(current_dt))
    # exclude_files = ['backups']
    exclude_files = []

    def filter_function(tarinfo):
        if tarinfo.name in exclude_files:
            return None
        else:
            return tarinfo

    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir), filter=filter_function)

    return 'Backup from {0} has been created.'.format(current_dt)





if __name__ == '__main__':
    # для теста
    print(make_tarfile('/Users/dima/Desktop/pythonista-3-ipa' + ' ' + current_dt + '.tgz', '/Users/dima/Desktop/pythonista-3-ipa/'))



