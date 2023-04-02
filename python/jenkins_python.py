import jenkins
from python.settings import usuario, senha, host



class jenkis_python:
    def __init__(self):
       self.server = jenkins.Jenkins(host,username=usuario, password= senha )

    def jk_status(self):
        user = self.server.get_whoami()
        version = self.server.get_version()
        print(('usuário: %s.  a versão do seu Jenkins é %s' % (user['fullName'], version)))  

    def jk_job(self):
        self.server.delete_job('python')
        self.server.create_job('python', jenkins.EMPTY_CONFIG_XML)
        self.server.build_job('python', {'param1': 'test value 1', 'param2': 'test value 2'})
        last_build_number = self.server.get_job_info('python')['lastCompletedBuild']['number']
        build_info = self.server.get_build_info('python', last_build_number)
        print (build_info)
jenkis_python().jk_job()