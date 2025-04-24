import sys

def main():
    score = 10
    try:
        r = int(input("What's the respiratory rate per min? "))
        if r == 0:
            sys.exit("🚨 Start CPR(30:2) 🧰")
        h = int(input("What's the heart rate per min? "))
        if h == 0:
            sys.exit("🚨 Start CPR(30:2) 🧰")
        p = input("What's the blood pressure? ").split("/")
        if len(p) != 2:
            raise ValueError
        try:
            p = int(p[0]), int(p[1])
        except ValueError:
            sys.exit("Oops! Invalid value")
        t = float(input("What's the body temperature in °F? "))

        resp_r, score = resp_rate(r, score)
        heart_r, score = heart_rate(h, score)
        blood_p, score = blood_pres(p, score)
        body_t, score = body_tem(t, score)

        print(resp_r)
        print(heart_r)
        print(blood_p)
        print(body_t)
        print(score_sum(score))
    except ValueError:
        sys.exit("Oops! Invalid value")

def resp_rate(r, score):
    if 0 < int(r) < 12:
        score -= 5
        return "Bradypnea", score
    elif int(r) > 20:
        score -= 3
        return "Tachypnea", score
    else:
        score = score
        return "Eupnea", score

def heart_rate(h, score):
    if 0 < int(h) < 60:
        score -= 5
        return "Bradycardia", score
    elif int(h) > 100:
        score -= 3
        return "Tachycardia", score
    else:
        score = score
        return "Eucardia", score

def blood_pres(p, score):
    p_s, p_d = p
    if int(p_s) < 90 or int(p_d) < 60:
        score -= 5
        return "Hypotention", score
    elif int(p_s) > 120 or int(p_d) > 80:
        score -= 3
        return "Hypertention", score
    else:
        score = score
        return "Eutention", score

def body_tem(t, score):
    if float(t) < 95:
        score -= 3
        return "Hypothermia", score
    elif float(t) > 100.4:
        score -= 5
        return "Hyperthermia", score
    else:
        score = score
        return "Euthermia", score

def score_sum(score):
    if score < 6:
        return "🏥 Go to ER or Call 911 🚑"
    elif 5 < score < 10:
        return "🩺 Doctor visit is recommended 🩹"
    else:
        return "🌿🧘 All clear - Keep it up 🏃🍎"


if __name__ == "__main__":
    main()
