from .basa import set_data_in_password_base
from .generate import gen


def usr_genert(id):
    rez = gen()
    set_data_in_password_base(url="https://github.com/krlltch2909", password=rez, user_id=id)
    return rez
