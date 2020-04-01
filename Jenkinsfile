def uploadToArtifactory() {
    rtUpload (
    serverId: 'Artifactory-1',
    spec: '''{
          "files": [
            {
              "pattern": "Jenkins-demo/*",
              "target": "example-artifactory-folder/Jenkins-demo_${BUILD_NUMBER}/"
            }
         ]
    }'''
    )
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
            }
        }
    }
}
