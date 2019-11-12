podTemplate(
    containers: [
    containerTemplate(name: 'docker', image: 'docker', ttyEnabled: true, command: 'cat')
  ], 
  volumes: [
      hostPathVolume('hostPath': '/var/run/docker.sock', 'mountPath':'/var/run/docker.sock')
      ]
) 
{
    node(POD_LABEL) {
        container('docker') {
            stage('Docker environment') {
                    sh 'docker ps'
                
            }
        }
    }
    
}
