def send_alert(province, risk):

    if risk > 70:
        return f"🔴 EMERGENCY ALERT: {province} severe drought risk"
    elif risk > 50:
        return f"🟠 HIGH ALERT: {province} drought developing"
    elif risk > 30:
        return f"🟡 WATCH: moderate dryness in {province}"
    else:
        return f"🟢 NORMAL: no drought risk in {province}"