from assets import *


@on_command('test3')
def _():
    send_photo(InputFile('assets/img.png'))
    send_document(InputFile('assets/img.png'))
