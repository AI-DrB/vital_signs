import pytest
from project import resp_rate, heart_rate, blood_pres, body_tem, score_sum

def test_resp_rate():
    score = 10
    assert resp_rate(15, score)[0] == "Eupnea"
    assert resp_rate(10, score)[0] == "Bradypnea"
    assert resp_rate(22, score)[0] == "Tachypnea"
    with pytest.raises(ValueError):
        resp_rate("mom", score)
    with pytest.raises(ValueError):
        resp_rate("", score)

def test_heart_rate():
    score = 10
    assert heart_rate(80, score)[0] == "Eucardia"
    assert heart_rate(50, score)[0] == "Bradycardia"
    assert heart_rate(120, score)[0] == "Tachycardia"
    with pytest.raises(ValueError):
        heart_rate("dad", score)
    with pytest.raises(ValueError):
        heart_rate("", score)

def test_blood_pres():
    score = 10
    assert blood_pres(["120", "60"], score)[0] == "Eutention"
    assert blood_pres(["88", "60"], score)[0] == "Hypotention"
    assert blood_pres(["120", "55"], score)[0] == "Hypotention"
    assert blood_pres(["122", "60"], score)[0] == "Hypertention"
    assert blood_pres(["120", "88"], score)[0] == "Hypertention"
    with pytest.raises(ValueError):
        blood_pres(["sis", "bro"], score)
    with pytest.raises(ValueError):
        blood_pres("", score)

def test_body_tem():
    score = 10
    assert body_tem(98, score)[0] == "Euthermia"
    assert body_tem(90, score)[0] == "Hypothermia"
    assert body_tem(104, score)[0] == "Hyperthermia"
    with pytest.raises(ValueError):
        body_tem("dude", score)
    with pytest.raises(ValueError):
        body_tem("", score)

def test_score_sum():
    assert score_sum(4) == "🏥 Go to ER or Call 911 🚑"
    assert score_sum(8) == "🩺 Doctor visit is recommended 🩹"
    assert score_sum(10) == "🌿🧘 All clear - Keep it up 🏃🍎"
