def uploadToArtifactory() {
    rtUpload (
    serverId: 'Artifactory-1',
    spec: '''{
          "files": [
            {
              "pattern": "Jenkins-demo/Jenkinsfile",
              "target": "example-artifactory-folder/Jenkins-demo_${BUILD_NUMBER}/"
            },
            {
              "pattern": "Jenkins-demo/main_file.py",
              "target": "example-artifactory-folder/Jenkins-demo_${BUILD_NUMBER}/"
            }
         ]
    }'''
    )
}

def publichBuildInfo() {
    rtPublishBuildInfo(serverId: 'Artifactory-1')   
}

pipeline {
    agent any
    stages {
        stage ("build") {
            steps {
                sh 'echo hello world in build stage'
            }
        }
        stage ("test") {
            steps {
                sh "echo hello in test stage!!!"
                sh "echo jenkinsfile script>jen.txt"
                  
            }
        }
        stage ("exec") {
            steps {
                sh 'python main_file.py 6'
            }
        }
        stage ("upload") {
            steps {
                uploadToArtifactory()
                publichBuildInfo()
            }
        }
    }
}
