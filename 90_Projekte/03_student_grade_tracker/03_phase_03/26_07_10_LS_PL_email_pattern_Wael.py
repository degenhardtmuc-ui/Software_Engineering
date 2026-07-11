Weal`s Lösungsweg:

EMAIL_PATTERN = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

=====================================================================

@pytest.mark.parametrize("email", [ 
    "Rick.Sanchez@rm.com", 
    "rick.sanchez@137.de", 
    "rick+sanchez@mail.co.uk", ]) 
def test_student_accepts_valid_emails(email): 
    student = Student( student_id="C137", first_name="Rick", last_name="Sanchez", email=email, ) 
    assert student.email == email



=======================================================================
def test_student_rejects_empty_email(): with pytest.raises(ValueError): Student( student_id="C137", first_name="Rick", last_name="Sanchez", email=" ", )

======================================================================
@pytest.mark.parametrize("email", [ 
    "Rick.Sanchezrm.com", 
    "Rick.Sanchez@", "@rm.com", 
    "Rick.Sanchez@rm", 
    "Rick.Sanchez@rm." ]) 
def test_student_rejects_invalid_email(email): with pytest.raises(ValueError): Student( student_id="C137", first_name="Rick", last_name="Sanchez", email=email, )

========================================================================





Peter`s Vorschlag:

regex_search('(?i)^dat$') -%}

/\w+/g

any word character


- email=None

=======================================================