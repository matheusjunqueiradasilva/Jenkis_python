import jenkins
from settings import usuario, senha, host



class jenkis_python:
    def __init__(self):
       self.server = jenkins.Jenkins(host,username=usuario, password= senha )

    def jk_status(self):
        user = self.server.get_whoami()
        version = self.server.get_version()
        print(('usuário: %s.  a versão do seu Jenkins é %s' % (user['fullName'], version)))  

    def jk_job(self):
        self.server.create_job('python', jenkins.EMPTY_CONFIG_XML)
        self.server.delete_job('python')
        self.server.create_job('python', jenkins.EMPTY_CONFIG_XML)       
        self.server.build_job('python')
        print ("job python criado")
jenkis_python().jk_job()