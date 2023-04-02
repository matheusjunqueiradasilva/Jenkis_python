# Projeto de Integração do Jenkins para worflows que precisam rodar scripts Python 

Este é um projeto de integração do Jenkins com Python.

Imagem Docker
A imagem Docker criada neste projeto contém as seguintes ferramentas:

Ubuntu
Git
Python
Jenkins
Com essa imagem, você tem tudo o que precisa para executar o repositório com os arquivos python no meu repositorio do GitHub.

**Como executar o repositório?
Para executar o repositório do GitHub, siga as etapas abaixo:**

**Clone o repositório para o seu computador:
Copie  o codigo**

````
git clone https://github.com/matheusjunqueiradasilva/Jenkis_python.git 
````

**Navegue até o diretório clonado:**
````
cd JENKIS_PYTHON
````
**Execute o comando para construir a imagem Docker:**
Copie  o codigo:**
````
docker build -t nome/nomedoApp:versão . 
````
**Execute o Compose do Docker Docker:
### No meu compose eu coloquei um postgres de brinde ###

**Copie o codigo:**
````
docker compose up
````
**dentro do seu container do seu compose voce vai precisar inciar o jenkins com o seguinte comando: **
````
service jenkins start
````

**Agora você pode acessar o Jenkins no seu navegador na porta:**
````
http://localhost:8080 
````

**assim que voce acessar o seu local host o jenkis vai pedir pra voce pegar o código de primeiro acesso que está na seguinte pasta:**
````
/var/lib/jenkins/secrets/initialAdminPassword
````

feito isso o jenkins vai te dar opções para instar os plugins padrões ou os costumizadas.

o jenkis vai pedir para criar os usuários eu coloquei 'teste' em tudos os campos ate o email: teste@gmail.com

se caso você colocar algo diferente irá precisar mudar no seu arquivo **settings.py** do repositório que baixou, lá ta as variaveis de ambiente do código que eu criei
para acessar o jenkins e criar um job nele através da api **Python-Jenkins.**

o proximo passo é voce criar um workflow job teste e nas opções avançadas do seu job acessar a parte de pipiline, definition e escolher pipeline **script from CMS.**
feito isso coloque o link do repositório que tenha o arquivo "Jenkisfile", colocar a sua branch e buildar o pipenile.


### links úteis:

**JENKINS**
````
https://www.jenkins.io/doc/
````

**API python-jenkins**
````
https://python-jenkins.readthedocs.io/en/latest/
````

**Docker**
````
https://docs.docker.com/get-started/
````
