import requests
import json
import os
import csv


def conectar(arquivo,data_to_file,csv_writer):
    for linha in arquivo:
        resposta = requests.get(f'https://api.github.com/repos/'+ linha.rstrip('\n') + '/issues?state=open')
        if resposta.status_code == 200:
            resposta = resposta.json()
            escrever_saida(resposta,data_to_file,csv_writer)
        else:
            resposta.status_code

def escrever_saida(resposta,data_to_file,csv_writer):
   
    for i in range(0,len(resposta)):
        nameLabels = ''
        data =  resposta[i]
        
        if(str(data["labels"]) != '[]'):
            for j in range(0,len(data["labels"])):
                nameLabels = nameLabels + data["labels"][j]['name'] + '; '  

            csv_writer.writerow([str(i+1),data["url"],data["repository_url"],data["labels_url"],data["comments_url"],data["events_url"],data["html_url"],data["id"],data["node_id"],data["number"],data["title"],
                                 data["user"]["login"],data["user"]["id"],data["user"]["node_id"], data["user"]["avatar_url"], data["user"]["gravatar_id"], data["user"]["url"], data["user"]["html_url"],
                                 data["user"]["followers_url"],data["user"]["following_url"], data["user"]["gists_url"], data["user"]["starred_url"],data["user"]["subscriptions_url"], data["user"]["organizations_url"],
                                 data["user"] ["repos_url"], data["user"]["events_url"],data["user"]["received_events_url"],data["user"]["type"], data["user"]["site_admin"],nameLabels,data["state"],data["locked"],data["assignee"],
                                 data["assignees"],data["milestone"],data["comments"],data["created_at"],data["updated_at"],data["closed_at"], data["author_association"], data["active_lock_reason"],
                                 data['body'].rstrip('\r\n'),data["performed_via_github_app"]]) 
        else:
            csv_writer.writerow([str(i+1),data["url"],data["repository_url"],data["labels_url"],data["comments_url"],data["events_url"],data["html_url"],data["id"],data["node_id"],data["number"],data["title"],
                                 data["user"]["login"],data["user"]["id"],data["user"]["node_id"], data["user"]["avatar_url"], data["user"]["gravatar_id"], data["user"]["url"], data["user"]["html_url"],
                                 data["user"]["followers_url"],data["user"]["following_url"], data["user"]["gists_url"], data["user"]["starred_url"],data["user"]["subscriptions_url"], data["user"]["organizations_url"],
                                 data["user"] ["repos_url"], data["user"]["events_url"],data["user"]["received_events_url"],data["user"]["type"], data["user"]["site_admin"],"",data["state"],data["locked"],data["assignee"],
                                 data["assignees"],data["milestone"],data["comments"],data["created_at"],data["updated_at"],data["closed_at"], data["author_association"], data["active_lock_reason"],
                                 data['body'].rstrip('\r\n'),data["performed_via_github_app"]])
        

def main():
    arquivo = open(os.path.dirname(os.path.realpath(__file__)) + '\\rep.txt','r')
    output_file = 'issues.csv'
    data_to_file = open(output_file, 'w', newline='',encoding="utf-8")
    csv_writer = csv.writer(data_to_file, delimiter=";")
    csv_writer.writerow(["index-rep","url","repository_url","labels_url","comments_url","events_url","html_url","id","node_id","number","title","user-login","user-id","user-node_id","user-avatar_url","user-gravatar_id","user-url",
                         "user-html_url","user-followers_url","user-following_url","user-gists_url","user-starred_url","user-subscriptions_url","user-organizations_url","user-repos_url","user-events_url","user-received_events_url","user-type",
                         "user-site_admin","labels-name","state","locked","assignee", "assignees","milestone","comments","created_at","updated_at","closed_at","author_association","active_lock_reason","body","performed_via_github_app"])


    conectar(arquivo,data_to_file,csv_writer)
    data_to_file.close()
    arquivo.close()

if __name__ == "__main__":
    main()


