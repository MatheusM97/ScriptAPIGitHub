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
    csv_writer.writerow(["repository_url","user-login","title","labels","state","milestones","number-comments","created_at","updated_up"])
    for i in range(0,len(resposta)):
        data = resposta[i] 
        csv_writer.writerow([data["repository_url"],data["user"]["login"],data["title"],data["labels"],data["state"],data["milestone"],data["comments"],data["created_at"],data["updated_at"]])

def main():
    arquivo = open(os.path.dirname(os.path.realpath(__file__)) + '\\rep.txt','r')
    output_file = 'issues.csv'
    data_to_file = open(output_file, 'w', newline='')
    csv_writer = csv.writer(data_to_file, delimiter=";")
    
 
    conectar(arquivo,data_to_file,csv_writer)
    data_to_file.close()
    arquivo.close()

if __name__ == "__main__":
    main()


