def get_model_status(accuracy):
    if accuracy>=0.90:
        return "Excellent"
    else:
        return "Needs imporvement"
    