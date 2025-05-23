import json
def read_credentials(path: str = "auth.json"):
    with open(path, 'r') as file:
        creds = json.loads(file.read())
        return creds


def calculate_final_score(path: str = "auth.json"):
    credentials = read_credentials()
    for dict in credentials:
        if dict['total_time']!="":
            quiz_score = dict['score'] * 5
            time = int(float(dict['total_time'].replace(":", ".")))
            time_score = (44 - time) * 3
            final_score = quiz_score + time_score
            dict['final_score'] = final_score
        else:
            dict['final_score'] = 0
    with open(path, 'w+') as f:
        f.write(json.dumps(credentials, indent=4))

def check_if_all_submitted(submision_time_name):
    credentials = read_credentials()
    k=0
    for dict in credentials:
        if dict[submision_time_name]=='':
            k+=1
    if k==0:
        return True
    else:
        return False

def read_quiz_score(username,path = 'auth.json'):
    credentials = read_credentials(path)
    for dict in credentials:
        if dict['user'] ==username:
            score = dict['score']
            return score
def read_quiz_time(username,path = 'auth.json'):
    credentials = read_credentials(path)
    for dict in credentials:
        if dict['user'] ==username:
            time = dict['total_time']
            return time


def read_ranking():
    ranking_dict = {}
    credentials = read_credentials()
    for dict in credentials:
        name = dict['user']
        ranking_dict[name] = dict['final_score']
    sorted_dict = sorted(ranking_dict.items(), key=lambda item: item[1], reverse=True)
    string = ""
    for item in sorted_dict:
        string = string + f"{item[0]}: {item[1]}\n"
    return sorted_dict


if __name__ == '__main__':
    calculate_final_score()
    print(read_ranking()[0][0])
    print(read_ranking()[0][1])
    print(check_if_all_submitted('submission_time'))

