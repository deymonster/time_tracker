from django.core.exceptions import ValidationError


# from .models import Company

def inn_ctrl_summ(nums, type):
    """
    Подсчет контрольной суммы
    """
    inn_ctrl_type = {
        'n2_12': [7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
        'n1_12': [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
        'n1_10': [2, 4, 10, 3, 5, 9, 4, 6, 8],
    }
    n = 0
    l = inn_ctrl_type[type]
    for i in range(0, len(l)):
        n += nums[i] * l[i]
    return n % 11 % 10


def inn_gen(l=None):
    """
    Генерация ИНН (10 или 12 значный)
    На входе указывается длина номера - 10 или 12.
    Если ничего не указано, будет выбрана случайная длина.
    """
    if not l:
        l = list((10, 12))[rnd(0, 1)]
    if l not in (10, 12):
        return None
    nums = [
        rnd(1, 9) if x == 0
        else rnd(0, 9)
        for x in range(0, 9 if l == 10 else 10)
    ]
    if l == 12:
        n2 = inn_ctrl_summ(nums, 'n2_12')
        nums.append(n2)
        n1 = inn_ctrl_summ(nums, 'n1_12')
        nums.append(n1)
    elif l == 10:
        n1 = inn_ctrl_summ(nums, 'n1_10')
        nums.append(n1)
    return ''.join([str(x) for x in nums])


def inn_check(inn):
    sinn = str(inn)
    nums = [int(x) for x in sinn]
    if len(sinn) == 10:
        n1 = inn_ctrl_summ(nums, 'n1_10')
        return n1 == nums[-1]
        #return inn
    elif len(sinn) == 12:
        n2 = inn_ctrl_summ(nums, 'n2_12')
        n1 = inn_ctrl_summ(nums, 'n1_12')
        return n2 == nums[-2] and n1 == nums[-1]
        #return inn
    else:
        return False
        

def validate_inn(value):
    if inn_check(value):
        return value
    else:
        raise ValidationError("Введите корректный номер ИНН!")