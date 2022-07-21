def get_complaints(filename , lim=50000):
    '''
    This function takes the file name of the complaint csv,
    and returns a list of complaints where each complaint
    is a dictionary.
    '''
    import csv
    with open("complaints.csv", 'r') as f:
        headers = next(f).strip().split(",")
        filereader = csv.reader(f, delimiter=',')
        complaints = []
        for i, line in enumerate(filereader):
            if i >= lim:
                break
            complaints.append(dict(zip(headers, line)))
    return complaints

def count_complaints_about(complaints, company_name):
    '''
    Takes a list of complaints (which are dictionaries) and counts how many of the
    complaints are about the given company
    Input: list of dictionaries, string
    Return: int
    '''
    count = 0
    for complaint in complaints:
        #print(complaint['Company'])
        if complaint['Company'] == company_name:
            count+=1
            #print("yes")
    return count

def count_state_complaints(complaints):
    '''
    Takes a list of complaints (which are dictionaries) and returns a dictionary with the number 
    of complains for each state
    Input: list of dictionaries
    Return: dictionary
    '''
    by_state = {}
    for complaint in complaints:
        state = complaint['State']
        if state not in by_state:
            by_state[state] = 0
        by_state[state] += 1
    return by_state

def main():
    complaints = get_complaints("complaints.csv")
    print(complaints[0])
    print(count_complaints_about(complaints, 'EQUIFAX, INC.'))
    print(count_state_complaints(complaints))

if __name__ == "__main__":
    main()

