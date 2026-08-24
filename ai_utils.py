def calculate_accuracy(correct,total):
    accuracy=correct/total
    return accuracy

def get_status(accuracy):
    if accuracy>=0.90:
        return "Ready for deployment"
    else:
        return "Needs improvement"

if __name__ == "__main__":
    accuracy = calculate_accuracy(95, 100)
    print(accuracy)
    print(get_status(accuracy))
    
