import re

p = re.compile(r"TC-[0-5]+1*") #match(r"TC-[0-5]+1", "TC-01") 

m = p.match("TC-11: sfkiadfj[aifjdaiofduf")

print m.group()

def validate_number_data(length, data, field_name):
    assert len(data.strip()) == length, "Expected {0} Field Length {1}, But Found {2}".format(field_name, length, len(data))
    assert re.match(r"^\d{" + str(length) + "}$", data) is not None, field_name + "Validation Failed, Expected Numbers Only, Data " + data

def validate_closed_number_range(lower, upper, data, field_name):
    length = len(data.strip())
    if length == lower or length == upper:
        assert len(data.strip()) == length, "Expected {0} Field Length {1} OR {2}, But Found {3}".format(field_name, lower, upper, length)
    elif length < lower:
        assert len(data.strip()) == lower, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    else:
        assert len(data.strip()) == upper, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    assert re.match(r"^\d{" + str(lower) + "," + str(upper) + "}$",data) is not None, " Validation Failed, Expected Number Only, Data: " + data

def validate_number(data, field_name):
    assert len(data.strip()) == 1, "Expected {0} Field Length {1}, But Found {2}".format(field_name, 1, len(data))
    assert re.match(r"^\d$", data) is not None, field_name + " Validation Failed, Expected Number Only, Data: " + str(data)

def validate_char(data, field_name):
    assert len(data.strip()) == 1, "Expected {0} Field Length {1}, But Found {2}".format(field_name, 1, len(data))
    assert re.match(r"^\w$", data) is not None, field_name + " Validation Failed, Expected Alpha Numeric Only, Data: " + data

def validate_data(length, data, field_name):
    assert len(data.strip()) == length, "Expected {0} Field Length {1}, But Found {2}".format(field_name, length, len(data))
    assert re.match(r"^\w{" + str(length) + "}$", data) is not None, field_name + " Validation Failed, Expected Alpha Numeric Only, Data: " + data

def validate_close_range(lower, upper, data, field_name):
    length = len(data.strip())
    if lower == length or upper == length:
        assert len(data.strip()) == length, "Expected {0} Field Length {1} OR {2}, But Found {3}".format(field_name, lower, upper, length)
    elif length < lower:
        assert len(data.strip()) == lower, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    else:
        assert len(data.strip()) == upper, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    assert re.match(r"^\w{" + str(lower) + "," + str(upper) + "}$", data) is not None, field_name + " Validation Failed, Expected Alpha Numeric Only, Data: " + data

def validate_ranges(lower, upper, data, field_name):
    length = len(data.strip())
    if lower <= length <= upper:
        assert len(data.strip()) == length, "Expected {0} Field Length {1} OR {2}, But Found {3}".format(field_name, lower, upper, length)
    elif len < lower:
        assert len(data.strip()) == lower, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    else:
        assert len(data.strip()) == upper, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    assert re.match(r"^\w{" + str(lower) + "," + str(upper) + "}$", data) is not None, field_name + " Validation Failed, Expected Alpha Numeric Only, Data: " + data

def validate_number_range(lower, upper, data, field_name):
    length = len(data.strip())
    if lower <= length <= upper:
        assert len(data.strip()) == length, "Expected {0} Field Length {1} OR {2}, But Found {3}".format(field_name, lower, upper, length)
    elif len < lower:
        assert len(data.strip()) == lower, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    else:
        assert len(data.strip()) == upper, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    assert re.match(r"^\d{" + str(lower) + "," + str(upper) + "}$", data) is not None, " Validation Failed, Expected Number Only, Data: " + data

def validate_float_number_range(lower, upper, f_lower, f_upper, data, field_name):
    length = len(data.strip())
    if lower <= length <= upper:
        assert len(data.strip()) == length, "Expected {0} Field Length {1} OR {2}, But Found {3}".format(field_name, lower, upper, length)
    elif length < lower:
        assert len(data.strip()) == lower, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    else:
        assert len(data.strip()) == upper, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    assert re.match(r"^\d{" + str(lower) + "," + str(upper) + "}\.\d{" + str(f_lower) + "," + str(f_upper) + "}$", data) is not None, " Validation Failed, Expected Float Number Only, Data: " + data

def validate_amount(lower, upper, data, field_name):
    length = len(data.strip())
    if lower <= length <= upper:
        assert len(data.strip()) == length, "Expected {0} Field Length {1} OR {2}, But Found {3}".format(field_name, lower, upper, length)
    elif length < lower:
        assert len(data.strip()) == lower, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    else:
        assert len(data.strip()) == upper, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    assert re.match(r"^\d{1,10}.\d{2}$", data) is not None, field_name + " Validation Failed, Expected Amount In Floating Points Only, Data: " + data

def validate_ranges_data(lower, upper, data, field_name):
    length = len(data.strip())
    if lower <= length <= upper:
        assert len(data.strip()) == length, "Expected {0} Field Length {1} OR {2}, But Found {3}".format(field_name, lower, upper, length)
    elif length < lower:
        assert len(data.strip()) == lower, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    else:
        assert len(data.strip()) == upper, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    assert re.match(r"^[\w,%]{" + str(lower) + "," + str(upper) + "}$", data) is not None, field_name + " Validation Failed, Expected Alpha Numeric Only, Data: " + data

def validate_name(lower, upper, data, field_name):
    length = len(data.strip())
    if lower <= length <= upper:
        assert len(data.strip()) == length, "Expected {0} Field Length {1} OR {2}, But Found {3}".format(field_name, lower, upper, length)
    elif length < lower:
        assert len(data.strip()) == lower, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    else:
        assert len(data.strip()) == upper, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    assert re.match(r"^[\w,\s, .]{" + str(lower) + "," + str(upper) + "}$", data) is not None, field_name + " Validation Failed, Expected Alphanumeric Only, Data: " + data

def validate_text(lower, upper, data, field_name):
    length = len(data.strip())
    if lower <= length <= upper:
        assert len(data.strip()) == length, "Expected {0} Field Length {1} OR {2}, But Found {3}".format(field_name, lower, upper, length)
    elif length < lower:
        assert len(data.strip()) == lower, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    else:
        assert len(data.strip()) == upper, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    assert re.match(r"^[\w, \s]{" + str(lower) + "," + str(upper) + "}$", data) is not None, field_name + " Validation Failed, Expected Alpha Numeric Only, Data: " + data

def validate_card_data(lower, upper, data, field_name):
    length = len(data.strip())
    if lower <= length <= upper:
        assert len(data.strip()) == length, "Expected {0} Field Length {1} OR {2}, But Found {3}".format(field_name, lower, upper, length)
    elif length < lower:
        assert len(data.strip()) == lower, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    else:
        assert len(data.strip()) == upper, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    assert re.match(r"^[\d, x, X, -]{" + str(lower) + "," + str(upper) + "}$", data) is not None, field_name + " Validation Failed, Expected Alpha Numeric Only, Data: " + data

def validate_email(email):
    length = len(email.strip())
    if 7 <= length <= 50:
        assert len(email.strip()) == length, "Expected Email Length between 7 - 50, But Found " + str(length)
    elif length < 7:
        assert len(email.strip()) == 7, "Expected Email Length between 7 - 50, But Found " + str(length)
    else:
        assert len(email.strip()) == 50, "Expected Email Length between 7 - 50, But Found " + str(length)
    assert re.match(r"^[_A-Za-z0-9-\+]+(\.[_A-Za-z0-9-]+)*@" + "[A-Za-z0-9-]+(\.[A-Za-z0-9]+)*(\.[A-Za-z]{2,})$", email) is not None, "Email Validation Failed, Data: " + email

def validate(lower, upper, data, field_name):
    length = len(data.strip())
    if lower <= length <= upper:
        assert len(data.strip()) == length, "Expected {0} Field Length {1} OR {2}, But Found {3}".format(field_name, lower, upper, length)
    elif length < lower:
        assert len(data.strip()) == lower, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    else:
        assert len(data.strip()) == upper, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    assert re.match(r"^(.){" + str(lower) + "," + str(upper) + "}$", data) is not None, " Validation Failed, Expected Alpha Numeric Only, Data: " + data

def validate_cashout_amount(lower, upper, data, field_name):
    length = len(data.strip())
    if lower <= length <= upper:
        assert len(data.strip()) == length, "Expected {0} Field Length {1} OR {2}, But Found {3}".format(field_name, lower, upper, length)
    elif length < lower:
        assert len(data.strip()) == lower, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    else:
        assert len(data.strip()) == upper, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    assert re.match(r"^-?\d{1,10}\.\d{2}$", data) is not None, " Validation Failed, Expected Amount in Floating Points Only, Data: " + data

def validate_ip_address(data, field_name):
    length = len(data.strip())
    if 7 <= length <= 15:
        assert len(data.strip()) == length, "Expected {0} Field Length {1} OR {2}, But Found {3}".format(field_name, 7, 15, length)
    elif length > 15:
        assert len(data.strip()) == 15, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, 7, 15, length)
    else:
        assert len(data.strip()) == 7, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, 7, 15, length)
    assert re.match(r"^\d{1,3}(.)\d{1,3}(.)\d{1,3}(.)\d{1,3}$", data) is not None, field_name + " Validation Failed, Expected IP Address Only, Data: " + data

def validate_app_name(lower, upper, data, field_name):
    length = len(data)
    if lower <= length <= upper:
        assert len(data) == length, "Expected {0} Field Length {1} OR {2}, But Found {3}".format(field_name, lower, upper, length)
    elif length < lower:
        assert len(data) == lower, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    else:
        assert len(data) == upper, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    assert re.match(r"^[\w,.,_,-]{" + str(lower) + "," + str(upper) + "}$", data) is not None, " Validation Failed, Expected Alpha Numeric Only, Data: " + data

def validate_app_path(lower, upper, data, field_name):
    length = len(data)
    if lower <= length <= upper:
        assert len(data) == length, "Expected {0} Field Length {1} OR {2}, But Found {3}".format(field_name, lower, upper, length)
    elif length < lower:
        assert len(data) == lower, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    else:
        assert len(data) == upper, "Expected {0} Field Length In Range {1}-{2}, But Found {3}".format(field_name, lower, upper, length)
    assert re.match(r"^[\w,/]{" + str(lower) + "," + str(upper) + "}$", data) is not None, " Validation Failed, Expected Alpha Numeric Only, Data: " + data

# validate_cashout_amount(1, 10, "3.50", "field_name")
# validate_email("bborade.bam@example.com")
# validate_app_name(0, 100, "abc.1.2_3.4", "field_name")
# validate_app_path(0, 100, "data/dfds/fgf/", "field_name")