from app_demo.utils.tools import define_date, define_date_w_year

def test_define_date():
    # test a valid date in the format 'dd/mm/yyyy'
    assert define_date_w_year('01/01/2022') == '01/01/2022'

    # test a valid date in the format 'dd month yyyy'
    assert define_date_w_year('01 enero 2022') == '01/01/2022'

    # test an invalid date format
    assert define_date_w_year('2022-01-01') is None

    # test an invalid date value
    assert define_date_w_year('31 febrero 2022') is None

    # test an invalid syntax with valid date value
    assert define_date_w_year('5 de febrero de 2022') == '05/02/2022'

    # test an invalid syntax with valid date value
    assert define_date('5 de febrero') == '05/02'