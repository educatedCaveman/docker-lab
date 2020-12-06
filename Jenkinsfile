pipeline {
    agent any 
    stages {
        // deploy code to VM
        stage('deploy') {
            steps {
                echo 'this is a new test' 
                echo 'testing the branch name'
                echo env.BRANCH_NAME
            }
        }
        // restart docker container
        stage('restart') {
            steps {
                echo 'this is where we restart the docker containers.  possibly a script?'
            }
        }
    }
}

