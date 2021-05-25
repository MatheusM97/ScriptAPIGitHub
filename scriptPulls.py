import requests
import json
import os
import csv


def conectar(arquivo,data_to_file,csv_writer):
    for linha in arquivo:
        resposta = requests.get(f'https://api.github.com/repos/'+ linha.rstrip('\n') + '/pulls?state=open')
        if resposta.status_code == 200:
            resposta = resposta.json()
            escrever_saida(resposta,data_to_file,csv_writer)
        else:
            resposta.status_code

def escrever_saida(resposta,data_to_file,csv_writer):
   
    for i in range(0,len(resposta)):
        nameLabels = ''
        data =  resposta[i]
        
        #if(str(data["labels"]) != '[]'):
         #   for j in range(0,len(data["labels"])):
          #      nameLabels = nameLabels + data["labels"][j]['name'] + '; '  

          #  csv_writer.writerow([str(i+1),data["url"],data["repository_url"],data["labels_url"],data["comments_url"],data["events_url"],data["html_url"],data["id"],data["node_id"],data["number"],data["title"],
           #                      data["user"]["login"],data["user"]["id"],data["user"]["node_id"], data["user"]["avatar_url"], data["user"]["gravatar_id"], data["user"]["url"], data["user"]["html_url"],
            #                     data["user"]["followers_url"],data["user"]["following_url"], data["user"]["gists_url"], data["user"]["starred_url"],data["user"]["subscriptions_url"], data["user"]["organizations_url"],
             #                    data["user"] ["repos_url"], data["user"]["events_url"],data["user"]["received_events_url"],data["user"]["type"], data["user"]["site_admin"],nameLabels,data["state"],data["locked"],data["assignee"],
              #                   data["assignees"],data["milestone"],data["comments"],data["created_at"],data["updated_at"],data["closed_at"], data["author_association"], data["active_lock_reason"],
               #                  data['body'].rstrip('\r\n'),data["performed_via_github_app"]]) 
        #else:
        csv_writer.writerow([str(i+1),data["url"],data["id"],data["node_id"],data["html_url"],data["diff_url"],data["patch_url"],data["issue_url"],data["commits_url"],data["review_comments_url"],data["review_comment_url"],data["comments_url"],data["statuses_url"],data["number"],data["state"],data["locked"],data["title"]])
        

def main():
    arquivo = open(os.path.dirname(os.path.realpath(__file__)) + '\\rep.txt','r')
    output_file = 'pulls.csv'
    data_to_file = open(output_file, 'w', newline='',encoding="utf-8")
    csv_writer = csv.writer(data_to_file, delimiter=";")
    csv_writer.writerow(["index-rep","url","id","node_id","html_url","diff_url","patch_url","issue_url","commits_url","review_comments_url","review_comment_url","comments_url","statuses_url","number","state","locked","title"])


    conectar(arquivo,data_to_file,csv_writer)
    data_to_file.close()
    arquivo.close()

if __name__ == "__main__":
    main()


