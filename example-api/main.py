import datetime
from calendar import calendar
from typing import Dict

from dateutil.relativedelta import relativedelta
from flask import jsonify

MONTHLY = 12


def cat(request):
    json: Dict = request.get_json()
    res = first_payment_date(json.get('opened_date'), json.get('payments_frequency', MONTHLY))
    res = res.strftime('%Y-%m-%d')
    return jsonify({"first_payment_date": res})


def first_payment_date(opened_date: str, payments_frequency: int) -> datetime.date:
    if opened_date is None:
        _opened_date: datetime.date = datetime.date.today()
    else:
        _opened_date: datetime.date = datetime.datetime.strptime(opened_date, '%Y-%m-%d').date()
    if payments_frequency == MONTHLY:
        first_date = _opened_date + relativedelta(months=1)
    else:
        month_last_day = calendar.monthrange(_opened_date.year, _opened_date.month)[1]
        if month_last_day > 30:
            month_last_day = 30
        if 14 < _opened_date.day <= (month_last_day - 1):
            first_date = _opened_date.replace(
                day=calendar.monthrange(_opened_date.year, _opened_date.month)[1])
        else:
            first_date = _opened_date.replace(day=15)
            if (calendar.monthrange(_opened_date.year, _opened_date.month)[
                    1] - 1) <= _opened_date.day:
                first_date = first_date + relativedelta(months=1)
    return first_date
